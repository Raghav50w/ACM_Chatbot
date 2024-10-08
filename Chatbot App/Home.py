import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Homepage styling
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        margin-bottom: 20px;
        font-size: 4rem;
        font-weight: bold, italic;        
    }
    </style> """, unsafe_allow_html=True)

st.markdown("<h1 class='centered-title'> <i><b>DLama</b></i> <span style='color: red;'>GPT</span></h1>", unsafe_allow_html=True)
st.subheader("Select a model from the sidebar to start chatting or click on the below options.")

st.write("The available models are:")
st.page_link("pages/Gemma 2.py", label="Gemma 2", icon="1️⃣")
st.page_link("pages/Llama 2.py", label="Llama 2", icon="2️⃣")
st.page_link("pages/Llama 3.py", label="Llama 3", icon="3️⃣")

with st.sidebar:
        st.write("Welcome to DLama GPT(Dalai Llama GPT). This is a AI powered chatbot using various aspects from Langchain and Streamlit using varioius open source LLM's of Ollama ran locally.")
        st.link_button("Github Repo", "https://github.com/Raghav50w/ACM_Chatbot")


