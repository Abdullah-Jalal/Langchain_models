from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()


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
chat_history = []
# def get_ai_response(query):
#     try:
#         response = model.invoke(query)
#         # chat_history.append({"role": "assistant", "content": response})
#         chat_history.append(AIMessage(content=response))
#         result = model.invoke(chat_history)
#         chat_history.append(HumanMessage(content=query))
#         return result
#     except Exception as e:
#         return f"Error: {e}"

# QUERY = st.text_input("Enter your query:", key="query_input")

# if st.button("Ask AI"):
#     if QUERY:
#         if QUERY.lower() == 'exit':
#             st.write("Goodbye! 👋")
#         else:
#             with st.spinner("Generating response..."):
#                 answer = get_ai_response(QUERY)
#                 st.write(f"**AI:** {answer}")
#     else:
#         st.warning("Please enter a query first!")

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("Mega Mind AI Assistant 🤖")

model = GoogleGenerativeAI(
    model='gemini-2.5-flash', 
    temperature=0.7,
    google_api_key=os.getenv("google_api_key")
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

def get_ai_response(query):
    try:
        st.session_state.chat_history.append(HumanMessage(content=query))
        
        response = model.invoke(st.session_state.chat_history)
        
        ai_content = response if isinstance(response, str) else response.content
        
        st.session_state.chat_history.append(AIMessage(content=ai_content))
        
        return ai_content
    except Exception as e:
        return f"Error: {e}"

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

if user_input := st.chat_input("Type your message here..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(user_input)
            st.markdown(ai_response)
