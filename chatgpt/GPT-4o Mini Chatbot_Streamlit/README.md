# GPT-4o Mini Chatbot 🤖

This repository contains a simple AI chatbot built using GPT-4o Mini and Streamlit. The chatbot allows users to interact with an AI model, providing responses based on user inputs. It demonstrates how to integrate OpenAI's GPT-4o Mini model with a user-friendly web interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Project Overview
The GPT-4o Mini Chatbot allows users to interact with OpenAI's GPT-4o Mini model through a simple web interface built using Streamlit. It can understand user prompts, provide responses, and maintain conversational context. The app is ideal for those looking to create their own AI-powered applications.

## Features
- Easy setup and deployment with Python and Streamlit.
- Real-time responses using OpenAI's GPT-4o Mini model.
- Customizable prompts and model behavior.
- User-friendly interface for interacting with the chatbot.

## Prerequisites
- Python 3.7 or higher
- An OpenAI API key. You can obtain it by creating an account at [OpenAI Platform](https://platform.openai.com/).
- Streamlit for building the web UI.

## Installation

1. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```
2.Install the required packages:
```bash
pip install -r requirements.txt

```
Ensure requirements.txt includes the following:
```bash
openai
streamlit
python-dotenv
tiktoken

```
3. Add your OpenAI API key:
Create a .env file in the root of the project with the following content
```bash
OPENAI_API_KEY=your-openai-api-key-here

```

4. Building theChatbot.
   create a file for the Python script. You can call it chatbot.py

```bash
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

   ```
   # Usage
  1. Run the chatbot:
```bash
streamlit run chatbot.py
```
This will start a local server, typically at http://localhost:8501.

2. Interact with the chatbot:

Open the provided URL in your browser and start chatting with the AI by typing your prompts.

# Project Structure
```bash
gpt4o_chatbot/
│
├── chatbot.py            # Main Python script for the chatbot
├── requirements.txt      # List of required Python packages
├── README.md             # Project documentation
```
# Google slides link
https://npuniversityedu-my.sharepoint.com/:p:/r/personal/rkamble2949_student_sfbu_edu/Documents/Presentation2.pptx?d=w8375b0ca0f0b4389a128a6dab8e5dc86&csf=1&web=1&e=2JxW9x



   


