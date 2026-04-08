from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
st.title("🔍 Chatbot")
st.write("welcome to chatbot, your personal research assistant powered by Google's Gemini-2.5-flash model. Ask me anything!")

model = GoogleGenerativeAI(model = 'gemini-2.5-flash', 
                        temperature = 0.7,
                        max_output_tokens = 2048,
                        top_p = 0.95,

                        api_key = os.getenv("google_api_key")
                        )

# while True:
#     if st.button("Ask AI"):
#         QUERY = st.text_input("enter your query:" , key="query_input")
#         if QUERY.lower() == 'exit':
#             st.write("Goodbye! 👋")
#         break
# else:
#     st.spinner("Generating response...")
#     try:
#         st.response = model.invoke(QUERY)
#         st.write("AI:" + st.response)
#     except Exception as e:
#         st.write(f"Error: {e}")

def get_ai_response(query):
    try:

        response = model.invoke(query)
        return response
    except Exception as e:
        return f"Error: {e}"

QUERY = st.text_input("Enter your query:", key="query_input")

if st.button("Ask AI"):
    if QUERY:
        if QUERY.lower() == 'exit':
            st.write("Goodbye! 👋")
        else:
            with st.spinner("Generating response..."):
                answer = get_ai_response(QUERY)
                st.write(f"**AI:** {answer}")
    else:
        st.warning("Please enter a query first!")
