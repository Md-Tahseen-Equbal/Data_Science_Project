### Building The Generative AI Model
### Develop a Comprehensive application that serves as a repository of code implementation for machine learning algorithms, 
### design to support and enhance the learning experience of students currently studying data science.

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Set your Gemini API key
GEMINI_API_KEY = "AIzaSyCNWcREa6fS9Ph9nzcDM8W2CCGnrcZLxVE"

# Initialize ChatModel
chat_model = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model="gemini-1.5-flash")

# Compile Chat Prompt
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an AI tutor who explains Machine Learning concepts by:\n"
     "1. Providing step-by-step Python implementations when requested, with comments explaining each step.\n"
     "2. Offering theoretical overviews when needed, with real-world examples and applications."),
    
    ("human", 
     "Please explain {topic_name} with a focus on {focus_type}.")
])

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an advanced Generative AI model designed to assist students in learning Machine Learning by:\n"
     "1. Providing clear, well-documented code implementations for Machine Learning algorithms in Python.\n"
     "2. Offering conceptual overviews with step-by-step explanations for each algorithm.\n"
     "3. Suggesting use cases, advantages, limitations, and variations of algorithms to deepen understanding.\n"
     "4. Recommending real-world datasets or examples to apply the concepts.\n"
     "5. Explaining relevant mathematical foundations when requested, with simple derivations and visuals."),
    
    ("human", 
     "Please explain {topic_name} with a focus on {focus_type}. Include:\n"
     "- Python code\n"
     "- Mathematical foundation\n"
     "- Real-world applications\n"
     "- Advantages and limitations.")
])


output_parser = StrOutputParser()
chain = chat_prompt_template | chat_model | output_parser

# Streamlit UI
st.image(
    r"C:\Users\91771\Desktop\Innomatic\Internship\GEN AI and LLM\Lagnchain Ml Algorithms\Heading.png",
)
st.title("📚 ML Tutor: Your AI-Powered Guide to Machine Learning")

# About Section
st.subheader("ℹ️ About ML Tutor")
st.markdown("""
Welcome to **ML Tutor**! This tool is your interactive guide to understanding Machine Learning concepts:
- 🤖 **AI-Powered Explanations**: Personalized teaching, tailored to your choices.
- 🐍 **Python Implementations**: Step-by-step coding tutorials with extensive comments.
- 📖 **Theory Overviews**: Engaging analogies and stories to simplify ML concepts.
""")

# Sidebar for Input
st.sidebar.image(
    r"C:\Users\91771\Desktop\Innomatic\Internship\GEN AI and LLM\Lagnchain Ml Algorithms\Logo.png",
    width=250
)
st.sidebar.header("⚙️ Machine Learning Options")

# Step 1: ML Type Selection
ml_type = st.sidebar.selectbox(
    "Select the type of Machine Learning",
    ("Supervised", "Unsupervised", "Reinforcement", "Semi-supervised"),
)

# Step 2: Algorithm Selection (dependent on ML type)
if ml_type == "Supervised":
    algorithm = st.sidebar.selectbox(
        "Select an Algorithm",
        ("KNN", "Linear Regression", "Logistic Regression", "SVM"),
    )
elif ml_type == "Unsupervised":
    algorithm = st.sidebar.selectbox(
        "Select an Algorithm",
        ("K-Means", "PCA", "Hierarchical Clustering"),
    )
elif ml_type == "Reinforcement":
    algorithm = st.sidebar.selectbox(
        "Select an Algorithm",
        ("Q-Learning", "SARSA", "Deep Q-Learning"),
    )
else:  # Semi-supervised
    algorithm = st.sidebar.selectbox(
        "Select an Algorithm",
        ("Label Propagation", "Self-training"),
    )

# Step 3: Focus Type (Theory or Implementation)
focus_type = st.sidebar.radio(
    "What do you want to focus on?",
    ("Theory", "Python Implementation"),
)

# Submit button
btn_click = st.sidebar.button("Submit")

# Main Area for Results
if btn_click:
    # Prepare user input for the chain
    user_input = {"topic_name": algorithm, "focus_type": focus_type}
    
    # Fetching the result using the chain
    with st.spinner("Generating results..."):
        try:
            result = chain.invoke(user_input)

            # Display the chosen focus
            if focus_type == "Python Implementation":
                st.subheader(f"🐍 Python Implementation for {algorithm}")
                st.code(result, language="python")
            else:
                st.subheader(f"📖 Theory for {algorithm}")
                st.write(result)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
