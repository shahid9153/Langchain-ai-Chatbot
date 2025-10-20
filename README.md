<h1 align="center">🤖 LangChain + Google Gemini 2.5 Flash Chatbot 💬</h1>

<p align="center">
A lightweight, interactive command-line chatbot powered by <b>LangChain</b> and <b>Google Gemini 2.5 Flash</b>.  
Built for learners who want to explore LLMs, APIs, and intelligent text interactions in Python.  
</p>

---

## 🌟 Overview

This project is a **beginner-friendly chatbot** that runs entirely in the **terminal**.  
It uses **LangChain** to connect with **Google Gemini 2.5 Flash**, one of Google’s latest Large Language Models (LLMs).  

With this simple yet powerful setup, you can:
- Chat with Gemini directly from your console 🧠  
- Understand how LangChain manages LLMs ⚙️  
- Learn secure API key handling using `.env` 🔒  

---

## 🚀 Features

✨ Interactive chat in terminal  
⚡ Powered by **Gemini 2.5 Flash** (fast and efficient)  
🧩 Uses **LangChain** for simple LLM integration  
🔐 Secure API management using `.env`  
👨‍💻 Beginner-friendly and easy to extend  

---

## 🧠 Tech Stack

| Technology | Purpose |
|-------------|----------|
| 🐍 **Python** | Core language |
| 🧠 **LangChain** | LLM orchestration framework |
| 🌐 **Google Gemini 2.5 Flash** | Large Language Model |
| 🔒 **python-dotenv** | Environment variable management |
| ⚙️ **os module** | System environment handling |

---

## ⚙️ Installation & Setup

1️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows

source venv/bin/activate   # On macOS/Linux

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Your Gemini API Key

Create a file named .env in the project root and add:

GOOGLE_API_KEY=your_api_key_here

4️⃣ Run the Chatbot
python app.py

💬 Example Interaction
You: Hello!
AI: Hi there! How can I assist you today?

You: Summarize what LangChain does.
AI: LangChain connects language models with data and tools to build intelligent applications.

You: exit
Chat ended.

🧩 Project Structure
📦 langchain-gemini-chatbot
 ┣ 📜 app.py              # Main chatbot logic
 ┣ 📜 .env                # Stores API key securely
 ┣ 📜 requirements.txt    # Dependencies
 ┗ 📜 README.md           # Documentation

🧠 How It Works

1️⃣ The ChatGoogleGenerativeAI class from langchain_google_genai connects to the Gemini model.

2️⃣ User input is captured and sent to Gemini using .invoke().

3️⃣ Gemini processes your query and returns a smart, contextual response.

4️⃣ The chat continues until the user types exit.

🚧 Future Enhancements

🔹 Add memory to retain previous chat context
🔹 Build a Streamlit-based web UI
🔹 Integrate PDF/Text summarization
🔹 Add voice input & speech response


