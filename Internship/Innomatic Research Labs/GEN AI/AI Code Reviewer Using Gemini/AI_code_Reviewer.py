import streamlit as st
import google.generativeai as genai
import re
from typing import Dict, Tuple

# Set your Gemini API key directly
GEMINI_API_KEY = ""  # Replace with your API key

class CodeReviewer:
    def __init__(self):
        """Initialize the CodeReviewer with Gemini AI."""
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def review_code(self, code: str) -> Tuple[Dict, str]:
        """
        Review the provided code using Gemini AI.
        Returns a tuple of (issues_dict, fixed_code).
        """
        try:
            prompt = f"""
            Please review the following Python code and provide:
            1. A list of potential bugs and issues
            2. Code quality improvements
            3. A corrected version of the code
            
            Here's the code to review:
            ```python
            {code}
            ```
            
            Please format your response exactly as shown below:
            ISSUES:
            - [issue description]
            
            IMPROVEMENTS:
            - [improvement suggestion]
            
            FIXED_CODE:
            ```python
            [corrected code]
            ```
            
            Please ensure to maintain this exact format in your response.
            """
            
            response = self.model.generate_content(prompt)
            response_text = response.text
            
            # Initialize dictionary to store issues
            issues = {'bugs': [], 'improvements': []}
            
            # Extract issues
            issues_match = re.findall(r'ISSUES:\n(.*?)(?=IMPROVEMENTS:|FIXED_CODE:|$)', response_text, re.DOTALL)
            if issues_match:
                issues['bugs'] = [bug.strip() for bug in issues_match[0].split('\n') if bug.strip()]

            # Extract improvements
            improvements_match = re.findall(r'IMPROVEMENTS:\n(.*?)(?=FIXED_CODE:|$)', response_text, re.DOTALL)
            if improvements_match:
                issues['improvements'] = [imp.strip() for imp in improvements_match[0].split('\n') if imp.strip()]
            
            # Extract fixed code
            fixed_code_match = re.findall(r'```python\n(.*?)```', response_text, re.DOTALL)
            fixed_code = fixed_code_match[-1].strip() if fixed_code_match else ""
            
            return issues, fixed_code
        
        except Exception as e:
            st.error(f"Error during code review: {str(e)}")
            return {"bugs": [], "improvements": []}, ""


def main():
    st.set_page_config(
        page_title="AI Code Reviewer",
        page_icon="🔍",
        layout="wide"
    )
    
  # Display an image with title and description
    st.image("AI Code Review With Gemini.png")
    st.markdown("""
    💻 **Submit your Python code for an AI-powered review using Google's Gemini AI.**
    """)

    
    # Sidebar for user input
    st.sidebar.title("AI Code Reviewer 🤖 ")
    st.sidebar.markdown("""
    💻 **Submit your Python code**<br>
    ⚙️ **Get instant feedback**<br>
    🐛 **Potential bugs**<br>
    💡 **Improvements**<br>
    ✨ **Suggested fixes!**
     """, unsafe_allow_html=True)



    # Sidebar for user input
    st.sidebar.header("📝 Enter Your Code")
    user_code = st.sidebar.text_area(
        "Paste your Python code here",
        height=200,
        placeholder="# Paste your Python code here..."
    )
    
    if st.sidebar.button("Review Code", type="primary"):
        if not user_code.strip():
            st.sidebar.warning("Please enter some code to review.")
        else:
            with st.spinner("Reviewing your code..."):
                reviewer = CodeReviewer()
                issues, fixed_code = reviewer.review_code(user_code)
                
                st.session_state.issues = issues
                st.session_state.fixed_code = fixed_code

    # Main area for results
    st.header("📊 Review Results")
    if 'issues' in st.session_state and st.session_state.issues:
        # Display issues and improvements
        st.subheader("🐛 Potential Bugs")
        for bug in st.session_state.issues['bugs']:
            st.markdown(f"- {bug.strip('- ')}")
        
        st.subheader("💡 Suggested Improvements")
        for improvement in st.session_state.issues['improvements']:
            st.markdown(f"- {improvement.strip('- ')}")
        
        # Display fixed code
        st.subheader("✨ Improved Code")
        if 'fixed_code' in st.session_state:
            st.code(st.session_state.fixed_code, language="python")
    else:
        st.info("Submit your code in the sidebar to get review results.")


def initialize_session_state():
    """Initialize session state variables."""
    if 'issues' not in st.session_state:
        st.session_state.issues = {'bugs': [], 'improvements': []}
    if 'fixed_code' not in st.session_state:
        st.session_state.fixed_code = ""


if __name__ == "__main__":
    initialize_session_state()
    main()
