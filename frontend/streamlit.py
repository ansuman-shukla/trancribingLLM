import streamlit as st
import requests

# Set the page title
st.set_page_config(page_title="Local LLM")

# Create a title for the Streamlit app
st.title("Local LLM")

# Function to make the API request
def get_api_info(question):
    base_url = "https://magical-famous-emu.ngrok-free.app/"
    params = {"question": question}
    response = requests.get(base_url, params=params)
    return response.json() if response.status_code == 200 else None

# Create an input field for the question
user_question = st.text_input("Enter your question:")

# Create a button to submit the question
if st.button("Submit"):
    if user_question:
        # Make the API request
        result = get_api_info(user_question)
        
        if result:
            # Display the API response
            st.subheader("LLM Response:")
            st.markdown(result)
        else:
            st.error("Failed to fetch data from the API. Please try again.")
    else:
        st.warning("Please enter a question.")

# Add some information about the app
st.sidebar.header("About")
st.sidebar.info("This Streamlit app makes a GET request to the specified Locally hosted LLM and displays the response.")