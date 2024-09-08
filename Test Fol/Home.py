import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables (e.g., API keys)
load_dotenv()

# Title and description for the main page
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        font-size: 4rem;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Centered title
st.markdown("<h1 class='centered-title'> <i><b>DLama</b></i> <span style='color: red;'>GPT</span></h1>", unsafe_allow_html=True)
st.subheader("Select a model from the sidebar to start chatting.")
st.write("The available models are:")

st.page_link("pages/Gemma 2.py", label="Gemma 2", icon="1️⃣")
st.page_link("pages/Llama 2.py", label="Llama 2", icon="2️⃣")
st.page_link("pages/Llama 3.py", label="Llama 3", icon="3️⃣")

