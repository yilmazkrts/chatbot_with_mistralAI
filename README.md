https://github.com/user-attachments/assets/2c830cf5-9c16-42be-ae19-b78c2aa320cf


# 🤖 LLM-Powered Chatbot with Mistral AI, LangChain, and Streamlit

This project demonstrates how to build a chatbot that uses a Large Language Model (LLM) via the **Mistral AI API**, **LangChain** for conversation flow management, and **Streamlit** for a simple and interactive web interface.

---

## 📌 Author Note

These are **my personal learning notes and implementation details**, shared to help others and for personal reference.  
Created by *[Your Name]*.

---

## 🚀 Introduction

Chatbots are increasingly common in customer support, education, and online services. Building a chatbot that feels natural and provides quick responses requires both a powerful language model and a user-friendly interface.

In this project, I created a chatbot using:
- **Mistral AI** for generating natural responses,
- **LangChain** for managing prompt templates and chaining model logic,
- **Streamlit** for building a responsive chat interface in the browser.

---

## 🔗 What is LCEL (LangChain Expression Language)?

**LCEL** stands for **LangChain Expression Language**. It is a declarative and composable way to build and connect language model operations in LangChain. LCEL makes it easy to build, test, and extend pipelines for LLMs.

Example usage:
```python
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | model | output_parser
result = chain.invoke({"topic": "programming"})
print(result)
