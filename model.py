import os
from dotenv import load_dotenv
import streamlit as st
from langchain_mistralai import ChatMistralAI  # LangChain uyumlu wrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the .env file
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize chat history
chat_history = []

# Initialize the Mistral model - DÜZELTME: ChatMistralAI kullan
model = ChatMistralAI(
    model="mistral-large-latest",  # veya "mistral-medium" gibi bir model
    mistral_api_key=api_key,
    temperature=0.7
)

def get_response(user_query, chat_history):
    """
    Generate a response based on user query and chat history using Mistral AI.
    """
    template = """
    You are a helpful assistant. Answer the following questions considering the history of the conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """

    # Create a prompt template
    prompt = ChatPromptTemplate.from_template(template)

    # Define the chain with the prompt, model, and output parser
    chain = prompt | model | StrOutputParser()

    with st.spinner("Preparing response, please wait..."):
        # Invoke the chain with the chat history and user query
        return chain.invoke({
            "chat_history": chat_history,
            "user_question": user_query,
        })









