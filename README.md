![Chatbot Screenshot](https://github.com/user-attachments/assets/2c830cf5-9c16-42be-ae19-b78c2aa320cf)


# 🤖 LLM-Powered Chatbot with Mistral AI, LangChain, and Streamlit

This project demonstrates how to build a chatbot that uses a Large Language Model (LLM) via the **Mistral AI API**, **LangChain** for conversation flow management, and **Streamlit** for a simple and interactive web interface.

---

## 📌 Author Note

These are **my personal learning notes and implementation details**, shared to help others and for personal reference.  
Created by *Yılmaz KARATAŞ*.

---

## 🚀 Introduction

Chatbots are increasingly common in customer support, education, and online services. Building a chatbot that feels natural and provides quick responses requires both a powerful language model and a user-friendly interface.

In this project, I created a chatbot using Mistral AI's language model API, along with the LangChain and Streamlit Python libraries. Mistral AI provides advanced language generation capabilities through its API, which allows the chatbot to understand and respond to user inputs effectively. LangChain helps manage the conversation flow and logic, making it easier to build flexible and robust chatbot workflows. Streamlit makes it simple to create an interactive web interface, so users can chat with the bot in real time through their browser.

By combining the strengths of Mistral AI, LangChain, and Streamlit, I was able to build a chatbot that is both intelligent and easy to use. This paper explains how I developed the chatbot, the main features of the system, and how these tools make it easier for anyone to build their own chatbot application.

In this project, I created a chatbot using:
- **Mistral AI** for natural response generation,
- **LangChain** for conversational logic,
- **Streamlit** for a simple web UI.


---

## 🔗 What is LCEL (LangChain Expression Language)?

**LCEL** stands for **LangChain Expression Language**. It is a declarative and composable way to build, connect, and run language model operations (blocks) inside the LangChain framework. LCEL lets you create advanced pipelines for LLMs (Large Language Models) using simple, chainable building blocks—making the workflow easier to understand, extend, and maintain.

Example usage:
```python
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | model | output_parser
result = chain.invoke({"topic": "programming"})
print(result)
```


LCEL is a way to connect your chatbot’s logic blocks together in a clear, flexible, and powerful way—making it easier to build, test, and update your chatbot workflows. You can learn more about it in the LangChain documentation.

---

## 📡 How to Stream a Response from Your LLM

Usually, when you create a chain in LangChain, you use the `.invoke()` method to generate the output.  
This method returns the full result after the entire chain is executed.

Below is a basic example using LangChain with OpenAI:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Create components
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

# Create chain using pipe syntax
chain = prompt | model | output_parser

# Invoke the chain
result = chain.invoke({"topic": "programming"})
print(result)
```

This code makes a joke bot. It has three parts: a question template, an AI brain, and a text cleaner. You connect them with pipe symbols (|) like building blocks. When you ask for a programming joke, it creates the question, sends it to AI, gets a joke back, makes it clean text, and shows it to you. It's like a simple assembly line for making jokes.

## 💬 A Regular Streamlit Chatbot

Now that we’ve seen how to stream a response from the LLM using LangChain, let’s look at how to do it in **Streamlit**.  
Streamlit is a great way to create simple web applications in Python with minimal code.

Let’s build the structure of a simple chatbot that is already working.

### 🔧 Streamlit Chatbot Setup

```python
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_mistralai import ChatMistralAI  # LangChain-compatible wrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the .env file
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize chat history
chat_history = []

# Initialize the Mistral model
model = ChatMistralAI(
    model="mistral-large-latest",  # or use "mistral-medium" etc.
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

# Title
st.title("AI Chatbot with Mistral AI")

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a bot. How can I help you?"),
    ]

# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = get_response(user_query, st.session_state.chat_history)
        st.write(response)

    st.session_state.chat_history.append(AIMessage(content=response))
```

The code above is a user-friendly chatbot application that enables real-time conversations between the user and an AI assistant powered by Mistral AI. Built with Streamlit for the interface and LangChain for managing the conversational logic, the application handles user messages, maintains conversation history, and generates context-aware responses. It demonstrates how to combine prompt templates, a language model, and an output parser into a modular pipeline, while Streamlit’s session state ensures the conversation flows naturally across messages.



##Conclusion
In this article we saw how to create a very simple LLM-powered chatbot that uses streaming to improve the user experience. To do this, we used LangChain and Streamlit to make the development as fast and simple as possible.





