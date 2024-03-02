import logging
import streamlit as st

from frontend.src.components.Header import AppHeader
from frontend.src.components.User_Input import UserInput
from frontend.src.components.Message import Message
    
def RenderMessages():
    try:
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hey there!"},
                {"role": "assistant", "content": "I'm Cognitive Operating Genius Navigating Intelligence - CogniTalk..."},
                {"role": "assistant", "content": "How can help you with Analyzing your Datasets through my Cognitive Skills?"}
            ]
            
        for message in st.session_state.messages:
            if message["role"] == "user":
                Message(message["content"], is_user=True)
            else:
                Message(message["content"])
    except Exception as e:
        logging.error('An Error Occured: ', exc_info=e)
        raise e
    
def main():
    try:
        AppHeader()
        RenderMessages()
        UserInput()      
    except Exception as e:
        logging.error('An Error Occured: ', exc_info=e)
        raise e
    
if __name__=='__main__':
    main()