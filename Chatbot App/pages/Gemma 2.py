from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os

# Creating chat history
if "chat_history_gemma2" not in st.session_state:
    st.session_state.chat_history_gemma2 = []

# Promp Template
def get_prompt(chat_history):
    chat_history_text = ""
    for entry in chat_history:
        chat_history_text += f"\nUser: {entry['user']}\nAssistant: {entry['assistant']}"
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", f"You are a multipurpose, kind, and smart bot. Below is the conversation so far:{chat_history_text}"),
            ("user", "Question:{question}")
        ]
    )
    return prompt

# Custom styling
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

st.markdown("<h1 class='centered-title'> <i><b>DLama</b></i> <span style='color: red;'>GPT</span></h1>", unsafe_allow_html=True)
st.subheader("Current Model: Gemma 2:2B")

# Initialize the selected LLM model
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()

# Chat history saving
chat_history = st.session_state.chat_history_gemma2

# User's input
input_text = st.chat_input("Talk with your bot")

# LLM processing
if input_text:
    prompt = get_prompt(chat_history)
    chain = prompt | llm | output_parser
    response = chain.invoke({"question": input_text})
    chat_history.append({"user": input_text, "assistant": response})

# Message styling
for entry in chat_history:
    # Users message
    st.markdown(f"""
    <div style='background-color: #231f2d; color: white; padding: 10px; border-radius: 10px; 
                margin-bottom: 10px; float: right; clear: both; display: inline-block; max-width: 70%;'>
        {entry['user']}""", unsafe_allow_html=True)

    # Chatbots message
    with st.chat_message("assistant"):
        st.markdown(f"""
        <div style='background-color: #231f2d; color: white; padding: 10px; border-radius: 10px; 
                margin-bottom: 10px; float: left; clear: both; display: inline-block; max-width: 90%;'>
            {entry['assistant']}""", unsafe_allow_html=True)
