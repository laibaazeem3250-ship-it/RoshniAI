from flask import Flask, render_template, request, jsonify
import os
import json
import subprocess
import threading
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app = Flask(__name__)

def load_skills():
    try:
        with open("skills/SKILL.md", "r") as f:
            return f.read()
    except:
        return ""

skills = load_skills()

def save_memory(profile_data):
    with open("memory.json", "w") as f:
        json.dump({"last_profile": profile_data}, f)

def evaluate_input(user_input):
    if len(user_input) < 3:
        return False, "Please provide more details!"
    harmful_words = ["hack", "illegal", "fake", "cheat", "kill"]
    for word in harmful_words:
        if word in user_input.lower():
            return False, "I can only help with educational guidance!"
    return True, ""

def ask_agent(system_prompt, user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

PROFILE_PROMPT = f"""You are Student Profile Agent of RoshniAI.
Use these skills: {skills}
Collect grades, budget per year, preferred country, field of study.
Ask friendly questions for missing info.
When you have all 4, write exactly:
STUDENT PROFILE COMPLETE:
- Grades: ...
- Budget: ...
- Country: ...
- Field: ..."""

UNIVERSITY_PROMPT = f"""You are University Finder Agent of RoshniAI.
Use these skills: {skills}
You know universities in Pakistan, USA, UK, Japan, China, Turkey, 
Malaysia, Italy, Korea, Singapore, Russia, Switzerland, Australia, 
Canada, India, Dubai, Qatar, Saudi Arabia, Germany, Ireland, Ukraine,
Sri Lanka, Iran, Europe and worldwide.
Recommend 5-7 best universities for the student profile.
For each: name, country, ranking, tuition fee, requirements, deadline.
Use emojis."""

SCHOLARSHIP_PROMPT = f"""You are Scholarship Hunter Agent of RoshniAI.
Use these skills: {skills}
Find 5 best scholarships matching student profile.
Include: Fulbright, Chevening, DAAD, Turkiye, MEXT, CSC, KGSP and more.
For each: name, coverage, eligibility, deadline.
Use emojis."""

conversations = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '').strip()
    session_id = data.get('session_id', 'default')

    is_valid, error_msg = evaluate_input(user_input)
    if not is_valid:
        return jsonify({'response': f'⚠️ {error_msg}', 'agent': 'System'})

    if session_id not in conversations:
        conversations[session_id] = ""

    conversations[session_id] += f"\nStudent: {user_input}"
    profile_response = ask_agent(PROFILE_PROMPT, conversations[session_id])

    if "STUDENT PROFILE COMPLETE" in profile_response:
        save_memory(profile_response)
        uni_response = ask_agent(UNIVERSITY_PROMPT, profile_response)
        sch_response = ask_agent(SCHOLARSHIP_PROMPT, profile_response + "\n\n" + uni_response)
        
        full_response = f"""✅ Profile collected!

{profile_response}

---

🔍 **Agent 2 - University Finder:**

{uni_response}

---

💰 **Agent 3 - Scholarship Hunter:**

{sch_response}

---
✅ RoshniAI guidance complete! Your profile has been saved."""
        conversations[session_id] = ""
        return jsonify({'response': full_response, 'agent': 'RoshniAI'})

    return jsonify({'response': profile_response, 'agent': 'Agent 1 - Profile'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)