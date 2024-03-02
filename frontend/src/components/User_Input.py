import os
import sys
import logging
import streamlit as st

from .Message import Message

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.Chatbot import Chatbot

def UserInput():
    try:        
        if prompt := st.chat_input("Message KnowGenius..."):
            Message(prompt, is_user=True)
            st.session_state.messages.append({"role": "user", "content": prompt})
        
            response = Chatbot().run(prompt)
 
            Message(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    except Exception as e:
        logging.error('An Error Occured: ', exc_info=e)
        raise e