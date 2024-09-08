from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables (e.g., API keys)
load_dotenv()

# Initialize chat history in session state if it doesn't exist for each model
if "chat_history_gemma2" not in st.session_state:
    st.session_state.chat_history_gemma2 = []

if "chat_history_llama2" not in st.session_state:
    st.session_state.chat_history_llama2 = []

if "chat_history_llama3" not in st.session_state:
    st.session_state.chat_history_llama3 = []

# Function to generate the prompt template with conversation history
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

# Inject custom CSS to center the title
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

# Sidebar for selecting the LLM model
st.sidebar.title("Your LLM Models")
llm_options = ["gemma2:2b", "llama2", "llama3"]
selected_model = st.sidebar.radio("Available models", llm_options)

st.sidebar.markdown("Welcome to Dlama GPT(Dalai Lama GPT!). Select from the available models and chat with your choosen bot.")

# Initialize the selected LLM model
llm = Ollama(model=selected_model)
output_parser = StrOutputParser()

# Get chat history based on selected model
if selected_model == "gemma2:2b":
    chat_history = st.session_state.chat_history_gemma2
elif selected_model == "llama2":
    chat_history = st.session_state.chat_history_llama2
elif selected_model == "llama3":
    chat_history = st.session_state.chat_history_llama3

# User input for asking a question
input_text = st.chat_input("Talk with your bot")

# Process input text when the user submits a question
if input_text:
    prompt = get_prompt(chat_history)
    chain = prompt | llm | output_parser
    response = chain.invoke({"question": input_text})
    
    # Append the user input and assistant response to the appropriate chat history
    chat_history.append({"user": input_text, "assistant": response})

# Display the chat history sequentially (conversational style)
for entry in chat_history:
    # User's message (right-aligned with bubble, limited width)
    st.markdown(f"""
    <div style='background-color: #231f2d; color: white; padding: 10px; border-radius: 10px; 
                margin-bottom: 10px; float: right; clear: both; display: inline-block; max-width: 70%;'>
        {entry['user']}
    </div>
    <div style='clear: both;'></div>""", unsafe_allow_html=True)

    # Assistant's message (left-aligned with bubble, limited width)
    with st.chat_message("assistant"):
        st.markdown(f"""
        <div style='background-color: #231f2d; color: white; padding: 10px; border-radius: 10px; 
                margin-bottom: 10px; float: left; clear: both; display: inline-block; max-width: 90%;'>
            {entry['assistant']}
        </div>
        """, unsafe_allow_html=True)
