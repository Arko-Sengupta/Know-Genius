import logging
import streamlit as st
from .Message import Message

def UserInput():
    try:
        if prompt := st.chat_input("Message CogniTalk..."):
            Message(prompt, is_user=True)
            st.session_state.messages.append({"role": "user", "content": prompt})
        
            response = 'This is a Demo Response...!'
 
            Message(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    except Exception as e:
        logging.error('An Error Occured: ', exc_info=e)
        raise e