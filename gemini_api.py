import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Function to load OpenAI model and get response
def get_gemini_response(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if image:
        response = model.generate_content([image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

# Input field for Google API key
google_api_key = st.text_input("Enter your Google API Key:")

# Check if API key is provided
if google_api_key:
    # Configure Gemini API with the provided API key
    genai.configure(api_key=google_api_key)

    # File upload section
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = None

    # Display uploaded image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Button to generate response
    submit = st.button("Tell me about the image")

    # Handle button click event
    if submit:
        if image is not None:
            response = get_gemini_response(image)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.warning("Please upload an image first.")
else:
    st.warning("Please enter your Google API Key.")
