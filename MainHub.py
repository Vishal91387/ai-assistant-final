import streamlit as st
from PIL import Image
import os
import requests
import yfinance as yf

# Your internal modules
from llm_loader import load_llama
from rag_chat import ask_question_from_docs
from ingest_docs import ingest_uploaded_docs
from utils import summarize_answer
from agent_chat import ask_agent


# Load LLaMA model once
llm = load_llama()

st.set_page_config(page_title="🧠 AI Toolbox", layout="wide")
st.title("🧠 My Local AI Toolbox")

st.markdown("""
### 👋 Welcome to Your AI Toolbox

This is your unified interface to access all your local AI tools. Use the tabs below to:

- **📄 RAGdoc** — Ask questions from your uploaded documents or from live web sources
- **📈 Real-Time AI Watch** — Track news and stock prices using live APIs

Select a tab to get started 👇
""")
st.markdown("---")

tabs = st.tabs(["📄 RAGdoc", "📈 Real-Time AI Watch"])

# ---------------------
# 📄 Tab 1: RAGdoc
# ---------------------
with tabs[0]:
    st.header("📄 Ask Questions from Your Documents or the Web")

    mode = st.radio("Choose your data source:", ["📄 My Documents", "🌐 Web Sources"], horizontal=True)

    if mode == "📄 My Documents":
        st.sidebar.title("📄 Upload & Ingest Docs")
        uploaded_files = st.sidebar.file_uploader(
            "Choose files (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"], accept_multiple_files=True
        )

        if uploaded_files:
            filepaths = []
            for file in uploaded_files:
                path = os.path.join("docs", file.name)
                with open(path, "wb") as f:
                    f.write(file.getbuffer())
                filepaths.append(path)
            ingest_uploaded_docs(filepaths)
            st.sidebar.success("Documents uploaded and processed!")

        question = st.text_input("Ask a question about your documents:")
        if question:
            answer = ask_question_from_docs(question)
            st.markdown("### 🧠 Answer")
            st.write(answer)

            # TL;DR Summary
            summary = summarize_answer(answer)
            if summary and any(summary):
                st.markdown("### 🔍 TL;DR Summary")
                st.markdown("<ul style='padding-left: 20px; font-size: 15px;'>", unsafe_allow_html=True)
                for point in summary:
                    st.markdown(f"<li>{point.strip()}</li>", unsafe_allow_html=True)
                st.markdown("</ul>", unsafe_allow_html=True)
            else:
                st.info("No summary available.")

    elif mode == "🌐 Web Sources":
        question = st.text_input("Ask a web-connected question:")
        if question:
            response = ask_agent(question)
            st.markdown("### 🌐 Web Response")
            st.write(response)
# ---------------------
# 📈 Tab 2: Real-Time AI Watch
# ---------------------
with tabs[2]:
    st.header("📈 Real-Time News and Stock Tracking")

    tab1, tab2 = st.tabs(["📰 News", "📊 Stock Price"])

    with tab1:
        topic = st.text_input("Enter a news topic (e.g., NATO, Elections, AI)")
        if topic:
            st.info(f"Fetching news for: {topic}")
            api_key = "18f6428e440f51409c62889f5bfeed0a"  # Replace with your actual Mediastack key
            url = "http://api.mediastack.com/v1/news"
            params = {
                "access_key": api_key,
                "keywords": topic,
                "languages": "en",
                "limit": 5,
                "sort": "published_desc"
            }
            response = requests.get(url, params=params)
            news_list = response.json().get("data", [])

            if news_list:
                for article in news_list:
                    st.markdown(f"**{article['title']}**\n\n{article['description']}\n\n[Read more]({article['url']})")
            else:
                st.warning("No news found.")

    with tab2:
        symbol = st.text_input("Enter stock symbol (e.g., AAPL, TSLA, GOOGL)")
        if symbol:
            stock = yf.Ticker(symbol)
            hist = stock.history(period="1d")
            if not hist.empty:
                latest = hist.tail(1)
                st.dataframe(latest)
            else:
                st.warning("No data found for this symbol.")
