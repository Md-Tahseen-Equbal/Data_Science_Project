import streamlit as st
import google.generativeai as ai

# Configure the AI model with API key
ai.configure(api_key="Your Api Key")

# Define system prompt
sys_prompt = """You are a helpful AI Tutor for Data Science. 
                Students will ask you doubts related to various topics in data science.
                You are expected to reply in as much detail as possible. 
                Make sure to take examples while explaining a concept.
                In case if a student ask any question outside the data science scope, 
                politely decline and tell them to ask the question from data science domain only."""

# Initialize the AI model
model = ai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                          system_instruction=sys_prompt)

# Display the GIF at the top
st.image(r"C:\Users\91771\Desktop\Innomatic\Internship\Data Science AI Tutor\Banner Data Tutor.gif", use_column_width=True)


# Main app title with emoji
st.title("Data Science :blue[Tutor] :teacher:")

# Sidebar with information about the AI Tutor
st.sidebar.title("About the Tutor 🤖")
st.sidebar.info(
    """
    Welcome to the Data Science Tutor! 
    This AI Tutor is here to help you understand various concepts in Data Science. 
    You can ask questions on topics like:
    
    - :bar_chart: Data Analysis
    - 🤖 Machine Learning
    - :chart_with_upwards_trend: Statistics
    - :brain: Deep Learning
    
    **Please note**: Questions outside the scope of Data Science will be politely declined. :blush:
    """
)

# User prompt input with emoji
user_prompt = st.text_input(
    "Enter Your Query: :speech_balloon:", 
    placeholder="Type Your Text Here..."
)

# Button to generate answer
btn_click = st.button("Generate Answer :tada:")

# Generate and display the response when the button is clicked
if btn_click:
    response = model.generate_content(user_prompt)
    st.write("### Answer :pencil:")
    st.write(response.text)
