# 🌟 RoshniAI — Multi-Agent Global University Guide

> Illuminating Every Student's Path Worldwide

## 📌 Problem Statement
Millions of students worldwide lack access to proper university 
guidance and scholarship information. RoshniAI solves this using 
3 AI agents working together.

## 🤖 Solution
RoshniAI is a multi-agent AI system that helps students find:
- Best universities worldwide matching their profile
- Fully funded and partial scholarships
- Career guidance and study roadmaps

## 🏗️ Architecture
3 Specialist AI Agents working together:
- **Agent 1 — Profile Agent**: Collects student information
- **Agent 2 — University Finder**: Searches 30+ countries
- **Agent 3 — Scholarship Hunter**: Finds best funding options

## 📚 5-Day Concepts Used
- ✅ Day 1: Multi-agent system (3 specialist agents)
- ✅ Day 2: MCP Server + Agent Memory + A2A communication
- ✅ Day 3: Agent Skills (SKILL.md)
- ✅ Day 4: Security evaluation + input/output validation
- ✅ Day 5: Web deployment with Flask

## 🌍 Countries Covered
Pakistan, USA, UK, Turkey, Malaysia, Germany, Japan, China, 
Korea, Singapore, Australia, Canada, India, Dubai, Qatar, 
Saudi Arabia, Ireland, Switzerland, and more!

## 🚀 How To Run

### Install dependencies:
pip install groq flask python-dotenv mcp

### Set up API key in .env:
GROQ_API_KEY=your_groq_api_key_here

### Run web app:
python app.py

### Open browser:
http://localhost:5000

## 🛠️ Tech Stack
- Python, Flask, Groq API (Llama 3.3 70B)
- MCP Server for university data
- Agent Memory (JSON storage)
- Security evaluation system
- Agent Skills (SKILL.md)

## 📁 Project Structure
RoshniAI/
├── app.py              # Flask web app + 3 agents
├── main.py             # Terminal version
├── mcp_server.py       # MCP Server
├── skills/SKILL.md     # Agent Skills (Day 3)
├── agents/             # Individual agent files
├── templates/          # Web interface
└── README.md

## 🎯 Track
Agents for Good — Helping students worldwide find education opportunities

## Author
Laiba Azeem 