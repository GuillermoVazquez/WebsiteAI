import os
import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from streamlit_chat import message

SHEET_ID = '1fI_qEk2Bu0fR79NZvFjmEOUf1BfPSACcLwpZslz6fHU'
SHEET_NAME = 'SampleData'

url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)

chat  = ChatOpenAI(model_name="gpt-3.5-turbo",temperature = 0.0)
agent = create_pandas_dataframe_agent(chat, df, verbose=True)

# Initialize the chat history in the session_state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Enter your question:", key="input_field")

if user_input:
    answer = agent.run(user_input)
    # Add the question and answer to the chat_history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("agent", answer))

# Display the chat_history in a chat-like format using streamlit-chat
for i, (sender, message_text) in enumerate(st.session_state.chat_history):
    if sender == "user":
        message(message_text, is_user=True, key=f"{i}_user")
    else:
        message(message_text, key=f"{i}")
