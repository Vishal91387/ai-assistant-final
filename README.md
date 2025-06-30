# 🧠 AI Suite Home

A personal, local AI assistant built using **Llama 3**, **LangChain**, and **Streamlit**, with real-time access to:
- 📄 Your own documents (RAG-based retrieval)
- 🌐 Live web search (via external APIs)
- 🗂️ File upload, document parsing, and chunk preview
- 📤 Chat log export to PDF or Word

---

## 🚀 Features

- 🔍 **RAG (Retrieval-Augmented Generation):**
  - Ask questions based on PDFs, Word, and text files from your local `docs/` folder
  - Extract answers with source tracking and chunk previews

- 🌐 **Web Agent Integration:**
  - Fetch and summarize content from sources like Wikipedia, Serper, or Arxiv

- 🧾 **Chat Export:**
  - Download your Q&A session as a formatted PDF or Word file

- 🧠 **Powered by Llama 3:**
  - Local inference via `Ollama`, using `llama3:8b` for privacy and speed

---

## 📁 Project Structure

```
my_ai_suite/
├── streamlit_app.py         # Main Streamlit UI
├── ingest_docs.py           # Document loader and chunker
├── rag_chat.py              # Handles RAG-style QA
├── agent_chat.py            # Web-based agent
├── tools/                   # Custom tools (Wikipedia, Serper, Arxiv)
├── utils.py                 # PDF/Word export, summarizers
├── docs/                    # Upload your reference files here
├── requirements.txt         # Python dependencies
├── start.sh                 # Optional startup script
└── .gitignore               # Tracks only what matters
```

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Vishal91387/ai-suite-home.git
cd ai-suite-home
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Streamlit app

```bash
streamlit run streamlit_app.py
```

---

## 📂 Upload Your Files

Drag and drop `.pdf`, `.docx`, or `.txt` files into the Streamlit sidebar, or place them directly into the `/docs` folder. The app will auto-ingest and chunk the content for RAG search.

---

## 📄 Export Options

- Click `📄 PDF` or `📝 Word` to export your full chat history
- TL;DR summaries and bullet points are included in export

---

## 🧠 LLM Setup (Ollama)

Make sure Ollama is installed and running locally:

```bash
ollama run llama3:8b
```

You can change models by editing the embedding and agent files (`rag_chat.py`, `agent_chat.py`).

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) – feel free to fork, modify, and build on it!

---

## 🙌 Credits

Built by [Vishal Sharma](https://github.com/Vishal91387)  
Powered by **LangChain**, **Streamlit**, and **Llama 3**
