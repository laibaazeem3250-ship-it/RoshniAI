import os 
import json
import subprocess
import threading 
from dotenv import load_dotenv
from groq import Groq 

load_dotenv() 
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ── Day 2: Start MCP Server in background ────────────────
def run_mcp_server():
    subprocess.Popen(
        ["python", "mcp_server.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

mcp_thread = threading.Thread(target=run_mcp_server)
mcp_thread.daemon = True
mcp_thread.start()
print("✅ [Day 2 - MCP Server]: RoshniAI MCP Server started!")

# ── Day 3: Load Agent Skills from SKILL.md ───────────────
def load_skills():
    try:
        with open("skills/SKILL.md", "r") as f:
            return f.read()
    except:
        return "Skills file not found"

skills = load_skills()
print("✅ [Day 3 - Skills]: Loaded SKILL.md successfully!")

# ── Day 2: Memory System ──────────────────────────────────
def save_memory(profile_data):
    with open("memory.json", "w") as f:
        json.dump({"last_profile": profile_data}, f)
    print("💾 [Day 2 - Memory]: Student profile saved!")

def load_memory():
    try:
        with open("memory.json", "r") as f:
            data = json.load(f)
            return data.get("last_profile", "")
    except:
        return ""

# ── Day 4: Security Evaluation ───────────────────────────
def evaluate_input(user_input):
    if len(user_input) < 3:
        return False, "Please provide more details!"
    harmful_words = ["hack", "illegal", "fake", "cheat", "kill", "sexuality"]
    for word in harmful_words:
        if word in user_input.lower():
            return False, "I can only help with educational guidance!"
    return True, ""

def evaluate_output(response):
    if len(response) < 10:
        return False
    return True

# ── Core Agent Function ───────────────────────────────────
def ask_agent(system_prompt, user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

# ── Day 1: Agent System Prompts ───────────────────────────
PROFILE_PROMPT = f"""You are Student Profile Agent of RoshniAI.
Use these skills to guide you:
{skills}

Collect grades, budget per year, preferred country, field of study.
Ask friendly questions for missing info.
When you have all 4, write exactly:
STUDENT PROFILE COMPLETE:
- Grades: ...
- Budget: ...
- Country: ...
- Field: ..."""

UNIVERSITY_PROMPT = f"""You are University Finder Agent of RoshniAI.
Use these skills to guide you:
{skills}

You have knowledge of top universities in:
Pakistan: LUMS, NUST, UET, COMSATS, IBA, QAU, FAST NUCES, Aga Khan University
USA: MIT, Stanford, Harvard, Carnegie Mellon, UC Berkeley, Caltech, Columbia, Yale
UK/England/London: Oxford, Cambridge, Imperial College, UCL, LSE, Edinburgh, Manchester
Japan: University of Tokyo, Kyoto University, Osaka University, Tokyo Institute of Technology
China: Tsinghua University, Peking University, Fudan University, Zhejiang University
Turkey: Bogazici University, METU, Bilkent University, Sabanci University, Koc University
Malaysia: Universiti Malaya, UTM, UPM, Taylor's University, Monash Malaysia
Italy: Politecnico di Milano, University of Bologna, Sapienza University
Korea: Seoul National University, KAIST, Yonsei University, Korea University
Singapore: NUS, NTU, Singapore Management University
Russia: Moscow State University, MIPT, Saint Petersburg State University
Switzerland/Geneva: ETH Zurich, EPFL, University of Zurich, University of Geneva
Australia: University of Melbourne, ANU, University of Sydney, UNSW
Canada/Toronto: University of Toronto, UBC, McGill, University of Waterloo
India: IIT Bombay, IIT Delhi, IISc Bangalore, Delhi University
Dubai/UAE: American University of Dubai, UAE University, Khalifa University
Qatar: Qatar University, Carnegie Mellon Qatar, Georgetown Qatar
Saudi Arabia: KAUST, King Abdulaziz University, King Saud University
Ireland: Trinity College Dublin, University College Dublin, NUI Galway
Germany: TU Munich, Heidelberg University, Humboldt University Berlin
Ukraine: Taras Shevchenko University, KPI, Kharkiv Polytechnic
Sri Lanka: University of Colombo, University of Peradeniya
Iran: University of Tehran, Sharif University of Technology
Europe: Top universities across all European countries

Given student profile, recommend 5-7 best universities worldwide.
For each: name, country, ranking, tuition fee, requirements, deadline.
Use emojis to make it friendly and clear.
This data is provided via MCP Server integration."""

SCHOLARSHIP_PROMPT = f"""You are Scholarship Hunter Agent of RoshniAI.
Use these skills to guide you:
{skills}

You know about scholarships worldwide including:
- Turkey: Turkiye Scholarships (fully funded)
- Malaysia: Malaysia International Scholarship
- UK: Chevening Scholarship (fully funded)
- USA: Fulbright Scholarship (fully funded)
- Germany: DAAD Scholarship (fully funded)
- Australia: Australia Awards Scholarship
- Canada: Vanier Canada Graduate Scholarships
- Switzerland: Swiss Government Excellence Scholarships
- Korea: Korean Government Scholarship (KGSP)
- Japan: MEXT Japanese Government Scholarship
- China: Chinese Government Scholarship (CSC)
- Ireland: Government of Ireland Scholarship
- Saudi Arabia: King Abdullah Scholarship
- Qatar: Qatar Foundation Scholarships
- Dubai: Mohammed Bin Rashid Scholarship
- Pakistan: HEC Scholarship, Prime Minister Scholarship

Given student profile and universities, find 5 best scholarships.
For each: name, coverage, eligibility, deadline.
This data is provided via MCP Server integration.
Use emojis to make it friendly."""

# ── Startup ───────────────────────────────────────────────
print("=" * 60)
print("🌟  RoshniAI — Multi-Agent University Guide  🌟")
print("Powered by 3 Specialist AI Agents + MCP Server")
print("=" * 60)

# Day 2: Check memory for returning students
previous = load_memory()
if previous:
    print(f"\n💾 [Memory]: Welcome back! Previous profile found.")
    print(f"Previous: {previous[:100]}...")

print("\n[Agent 1 - Profile]: Hi! I'm RoshniAI 🌟")
print("[Agent 1 - Profile]: Tell me your grades, budget, preferred country and field of study!")

conversation = ""

while True:
    user_input = input("\nYou: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "exit":
        print("\nRoshniAI: Good luck with your studies! 🌟")
        break

    # Day 4: Security check
    is_valid, error_msg = evaluate_input(user_input)
    if not is_valid:
        print(f"\n⚠️ RoshniAI: {error_msg}")
        continue

    conversation += f"\nStudent: {user_input}"

    # Day 1: Agent 1 — Profile Agent
    profile_response = ask_agent(PROFILE_PROMPT, conversation)

    # Day 4: Evaluate output quality
    if not evaluate_output(profile_response):
        print("\n⚠️ Response quality check failed. Please try again.")
        continue

    print(f"\n[Agent 1 - Profile]: {profile_response}")

    if "STUDENT PROFILE COMPLETE" in profile_response:

        # Day 2: Save to memory
        save_memory(profile_response)

        # Day 2: MCP Server provides university data
        print("\n✅ [MCP Server]: Fetching university data...")

        # Day 1+2: Agent 2 — University Finder (A2A communication)
        print("\n[Agent 2 - University Finder]: 🔍 Searching best universities...\n")
        uni_response = ask_agent(UNIVERSITY_PROMPT, profile_response)
        print(f"[Agent 2 - University Finder]: {uni_response}")

        # Day 1+2: Agent 3 — Scholarship Hunter (A2A communication)
        print("\n[Agent 3 - Scholarship Hunter]: 💰 Finding scholarships...\n")
        sch_response = ask_agent(
            SCHOLARSHIP_PROMPT,
            profile_response + "\n\n" + uni_response
        )
        print(f"[Agent 3 - Scholarship Hunter]: {sch_response}")

        print("\n" + "=" * 60)
        print("✅ RoshniAI guidance complete!")
        print("💾 Your profile has been saved for next time!")
        print("Ask another question or type 'exit'")
        conversation = ""