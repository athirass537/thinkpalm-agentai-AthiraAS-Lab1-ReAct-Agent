# thinkpalm-agentai-AthiraAS-Lab1-ReAct-Agent
Old Car Resale ReAct Agent 🚗🤖

A simple Python project demonstrating a ReAct (Reasoning + Acting) Agent that helps users estimate old car resale prices, find nearby inspection branches, answer FAQs, and book inspection slots interactively.

📌 Overview

This project takes car details such as make, model, year, kilometers driven, and city as input, then provides an estimated resale value along with the nearest branch location.

It’s a beginner-friendly example to understand:

Tool usage in Python
Decision-based logic
Slot filling & information extraction
Interactive chatbot workflow
Basic ReAct agent concept
✨ Features
🚘 Accepts car details interactively
💰 Estimates resale value using mock pricing logic
📍 Suggests nearest inspection branch
📅 Books inspection slots
❓ Handles common FAQs
🧠 Demonstrates reasoning + acting workflow
🔁 Interactive conversation-based experience
🛠️ Tech Stack
Python
Built-in libraries:
re (Regular Expressions)
📂 Project Structure
old-car-resale-agent/
│── main.py
│── README.md
⚙️ How It Works
User enters car details
Agent extracts important information:
Car make
Model
Manufacturing year
Kilometers driven
City
Missing details are requested interactively
Resale price is calculated using depreciation logic
Nearest branch is suggested
User can optionally book an inspection slot

💡 Future Improvements
🌐 Integrate real car resale APIs
🤖 Add AI/NLP-based intent recognition
📊 Improve price prediction using ML models
📱 Build a web app using Flask or Streamlit
🗺️ Add real-time branch locator with maps
💬 Integrate voice/chat support
🙌 Conclusion

This project is a simple introduction to building an intelligent conversational assistant using Python. It combines logic, reasoning, slot filling, and tool execution to simulate a real-world old car resale assistant using the ReAct agent concept.
