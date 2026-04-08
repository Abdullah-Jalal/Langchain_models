# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# st.header("Research Tool", anchor="research-tool" , help="This tool allows you to ask questions and get answers using the Gemini-2.5-flash model." , icon="🔍" )

# query = st.text_input("enter your query")
# # genai.configure(api_key="AIzaSyBByxKqfsBwy8NM9bXbRMWRvqfiNqpQLiQ")
# model= genai.GenerativeModel("gemini-2.5-flash")

# if st.button("Generate"):
#     response = model.generate_content(query)
#     st.write(response.text)

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Fixed: Icon moved inside the header string
st.header("🔍 Research Tool", anchor="research-tool", help="This tool uses Gemini to answer queries.")

query = st.text_input("Enter your query")

# Securely get API key from .env
api_key = os.getenv("google_api_key") 

    
# Use 'latest' to avoid 404 version errors
model = genai.GenerativeModel("gemini-flash-latest")

if st.button("Generate"):
    if query:
        with st.spinner("Searching..."):
            response = model.generate_content(query)
            st.markdown(response.text)
    else:
        st.warning("Please enter a query first!")