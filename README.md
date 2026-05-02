# 🧠 Multi-Agent Research System

An AI-powered research assistant that autonomously gathers, expands, and synthesizes information into structured reports — built using **Streamlit + LangChain + Ollama (Mistral)**.

---

## 🚀 Features

* 🔍 Intelligent research pipeline (multi-step reasoning)
* 📄 Automated report generation (structured + detailed)
* 🧠 Critic agent for evaluation and feedback
* ⚡ Fully local LLM support (no API cost)
* 🌐 Deployable with Streamlit + Ngrok

---

## 🏗 Architecture

```
User Input
    ↓
Search (LLM-based)
    ↓
Content Expansion
    ↓
Writer Agent (Report Generation)
    ↓
Critic Agent (Evaluation)
    ↓
Final Output
```

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Ollama (Mistral / Phi)**
* **dotenv**

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-research-system.git
cd multi-agent-research-system
```

### 2. Create virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🌐 Share the App (Optional)

```bash
ngrok http 8501
```

Use the generated link to share with others.

---

## ⚙️ Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here   # optional (if using OpenAI)
```

⚠️ This project is designed to work **without paid APIs** using Ollama.

---

## 📁 Project Structure

```
├── agents.py        # Agent definitions
├── pipeline.py      # Research workflow
├── app.py           # Streamlit UI
├── tools.py         # Tools (search, scrape)
├── requirements.txt
└── .env             # Environment variables (ignored)
```

---

## 📌 Key Highlights

* Works with **local LLM (Mistral via Ollama)**
* No dependency on paid APIs
* Modular multi-agent architecture
* Easy to extend (add real search, RAG, etc.)

---

## 🚧 Future Improvements

* 🌍 Real-time web search integration
* 📚 RAG (Retrieval-Augmented Generation)
* 💬 Chat-style UI
* ☁️ Cloud deployment
* 📊 Source citations with links

---

## 🤝 Contributing

Feel free to fork this repo and improve the system.

---

## ⭐ Show your support

If you like this project:

👉 Star ⭐ the repository
👉 Share it

---

## 📬 Contact

Created by **[JISHNU KUMAR ]**

---

## 🏆 Why this project matters

This project demonstrates:

* Multi-agent system design
* LLM orchestration
* Real-world AI application development
* Deployment and sharing workflow

---
<img width="1914" height="965" alt="Screenshot 2026-05-02 120940" src="https://github.com/user-attachments/assets/c17506e0-38f4-43cc-808d-9604f3dc0972" />
<img width="1891" height="966" alt="Screenshot 2026-05-02 120900" src="https://github.com/user-attachments/assets/fcbaddc9-528b-42c0-8a26-4352fd1225b3" />



