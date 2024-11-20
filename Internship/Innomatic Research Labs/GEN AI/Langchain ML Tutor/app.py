### Building The Generative AI Model
### Develop a Comprehensive application that serves as a repository of code implementation for machine learning algorithms, 
### design to support and enhance the learning experience of students currently studying data science.

import streamlit as st

name_of_ml_algo = st.selectbox(
    "Select the Machine Learning Algorithm",
    ("KNN", "Linear Regression", "SVM", "LogisticRegression"),

)


from langchain_google_genai import ChatGoogleGenerativeAI

# Set your Gemini API key directly
GEMINI_API_KEY = "Your API Key"

# Set the OpenAI Key and initialize a ChatModel
chat_model = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model="gemini-1.5-flash")

from langchain_core.prompts import ChatPromptTemplate

# Compoling Chat Prompt
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly AI Tutor with expertise in Data Science and Artificial Intelligence, Who tells step by step python Implementation for Machine Learning Algorithm asked by user. "),
    ("human", "Tell me a python implementation for {topic_name}?"),
])

from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

chain = chat_prompt_template | chat_model | output_parser

user_input = {"topic_name": name_of_ml_algo}

btn_click = st.button("Submit")

if btn_click == True:
    st.write(chain.invoke(user_input))


