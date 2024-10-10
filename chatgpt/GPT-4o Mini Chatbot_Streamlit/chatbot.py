import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

st.title("My GPT-4o Mini Chatbot 🤖")

# Initialize messages in the session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input and process it
if user_prompt := st.chat_input("Your Prompt:"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        chatbot_msg = st.empty()
        full_response = ""
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": msg["role"], "content": msg["content"]}
                for msg in st.session_state["messages"]
            ],
            stream=True,
        )

        for chunk in stream:
            token = chunk.choices[0].delta.content
            if token is not None:
                full_response += token
                chatbot_msg.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})

