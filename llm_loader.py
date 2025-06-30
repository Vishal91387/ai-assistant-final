import streamlit as st
from langchain_community.llms import Ollama

@st.cache_resource
def load_llama():
    return Ollama(model="llama3:8b")
