# 🏥 MediAssist — Intelligent Medical Support Chatbot

> An AI-powered medical assistant built with **LangChain**, **Groq (LLaMA 3.3 70B)**, and **ChromaDB**.  
> Final project for the *Generative AI Systems* course — Agent IA option (/20)

---

## 📌 Overview

MediAssist is an autonomous AI agent that helps patients navigate medical concerns through natural conversation. It reasons step by step to understand symptoms, identify the right specialist, and book an appointment — just like a real clinic receptionist would.

**Example flow:**
```
User: "I've had chest pain since this morning"
  → Agent searches medical knowledge base (RAG)
  → Agent identifies specialty: Cardiologist
  → Agent finds available doctor: Dr. Trabelsi
  → Agent books appointment: June 10 at 09:00
  → Agent responds with full summary + source citations
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Symptom Analysis** | RAG over medical knowledge base with source citations |
| 👨‍⚕️ **Doctor Finder** | Matches symptoms to available specialists |
| 📅 **Appointment Booking** | Books real slots from a mock calendar |
| 🧠 **Multi-turn Memory** | Remembers context across the full conversation |
| 🤖 **Autonomous Reasoning** | Multi-step agent decides which tools to call |
| 💬 **Gradio UI** | Clean chat interface with conversation history |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│              Gradio UI                  │
│   (chat interface + history display)    │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│           LangChain Agent               │
│        (ReAct + Groq LLaMA 3.3)         │
│      + ConversationBufferMemory         │
└────┬──────────────┬──────────────┬──────┘
     │              │              │
┌────▼────┐  ┌──────▼──────┐ ┌────▼──────┐
│symptom  │  │   doctor    │ │appoint-   │
│rag_tool │  │finder_tool  │ │ment_tool  │
└────┬────┘  └──────┬──────┘ └────┬──────┘
     │              │              │
┌────▼────┐  ┌──────▼──────┐ ┌────▼──────┐
│ChromaDB │  │ doctors.json│ │calendar   │
│(med docs│  │             │ │  .json    │
└─────────┘  └─────────────┘ └───────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | Groq — LLaMA 3.3 70B Versatile |
| Agent Framework | LangChain AgentExecutor (ReAct) |
| RAG | LangChain + ChromaDB |
| Embeddings | all-MiniLM-L6-v2 (local, no API cost) |
| UI | Gradio |
| Memory | LangChain ConversationBufferMemory |

---

## 📁 Project Structure

```
mediassist/
│
├── app.py                  # Gradio UI — entry point
├── agent.py                # LangChain agent setup + tool binding
├── memory.py               # Conversation memory management
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
│
├── rag/
│   ├── loader.py           # Loads PDF/TXT files from data/
│   ├── chunker.py          # Splits documents into overlapping chunks
│   ├── embedder.py         # Local embedding model (MiniLM)
│   ├── vectorstore.py      # ChromaDB build & load
│   └── init_rag.py         # One-time RAG initialization script
│
├── tools/
│   ├── symptom_rag.py      # Tool 1 — searches medical knowledge base
│   ├── doctor_finder.py    # Tool 2 — finds doctors by specialty
│   └── appointment.py      # Tool 3 — books appointment slots
│
└── data/
    ├── medical_faq.txt     # Medical knowledge base (fiches)
    ├── doctors.json        # Mock doctor database
    └── calendar.json       # Mock appointment calendar
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/iyadhbf/MediAssist.git
cd MediAssist
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```



### 4. Initialize the RAG pipeline (run once)
```bash
python -m rag.init_rag
```

### 5. Launch the app
```bash
python app.py
```

---

## 🤖 Agent Tools

### Tool 1 — `symptom_rag_tool`
Searches the medical knowledge base using semantic similarity.  
Triggered when: user describes symptoms or asks a health question.

### Tool 2 — `doctor_finder_tool`
Matches a medical specialty to available doctors.  
Triggered when: a specialty has been identified from symptoms.

### Tool 3 — `appointment_tool`
Books the first available slot for a given doctor ID.  
Triggered when: user confirms they want to book an appointment.

---



## ⚠️ Limitations & Future Improvements

- **Mock data** — doctors and calendar use static JSON files; a real system would use a database
- **Language** — currently optimized for French; could be extended to Arabic/English
- **Knowledge base** — medical_faq.txt is limited; could be enriched with real clinical PDFs
- **Authentication** — no patient login system; could add session management
- **Real booking** — appointment_tool simulates booking; could integrate with Google Calendar API

