import os
import logging
import requests
import streamlit as st
from dotenv import load_dotenv

from frontend.src.Components.Header import AppHeader
from frontend.src.Components.Message import Message

load_dotenv(".env")

class Chatbot_UI:
    
    def __init__(self):
        self.title = os.getenv("TITLE")
        self.ERROR_MESSAGE = os.getenv("ERROR_MESSAGE")
        self.CHATBOT_API = os.getenv("CHATBOT_API")
        self.AppHeader = AppHeader
        self.Message = Message
        
    def RenderMessages(self):
        try:
            if "messages" not in st.session_state:
                st.session_state.messages = [
                    {"role": "assistant", "content": "Hey there!"},
                    {"role": "assistant", "content": "I'm General Expertise & Navigation Intelligence Utility System! KnowGenius..."},
                    {"role": "assistant", "content": "I'm a General Knowledge Expert."},
                    {"role": "assistant", "content": "Ask your question?"}
                ]
                
            for message in st.session_state.messages:
                if message["role"] == "user":
                    self.Message(message["content"], is_user=True)
                else:
                    self.Message(message["content"])
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
        
    def UserInput(self):
        try:        
            if prompt := st.chat_input("Message KnowGenius..."):
                self.Message(prompt, is_user=True)
                st.session_state.messages.append({"role": "user", "content": prompt})
                
                with st.spinner():
                    try:
                        response = requests.post(self.CHATBOT_API, json={'query': prompt}).json()
                    except:
                        response = {
                            'response': self.ERROR_MESSAGE
                        }
     
                self.Message(response['response'])
                st.session_state.messages.append({"role": "assistant", "content": response['response']})
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
    
    def run(self):
        try:
            self.AppHeader(self.title)
            self.RenderMessages()
            self.UserInput()      
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
    
if __name__=='__main__':
    
    App = Chatbot_UI()
    App.run()
