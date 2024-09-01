import os
import logging
import requests
import streamlit as st
from dotenv import load_dotenv
from frontend.src.Components.Header import AppHeader
from frontend.src.Components.Message import Message

# Load Environment Variables
load_dotenv(".env")

# Set Up Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChatbotUI:

    def __init__(self):
        self.title = os.getenv("TITLE", "KnowGenius (AI-Chatbot)")
        self.chatbot_api = os.getenv("CHATBOT_API", "")
        self.AppHeader = AppHeader
        self.Message = Message

    def Initialize_Messages(self):
        """Initialize Session State Messages."""
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hey there!"},
                {"role": "assistant", "content": "I'm General Expertise & Navigation Intelligence Utility System! KnowGenius..."},
                {"role": "assistant", "content": "I'm a General Knowledge Expert."},
                {"role": "assistant", "content": "Ask your question?"}
            ]
            logging.info("Session state messages initialized.")

    def Messages(self):
        """Render All Messages from Session State."""
        try:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    self.Message(message["content"], is_user=True)
                else:
                    self.Message(message["content"])
        except Exception as e:
            logging.error('An error occurred while rendering messages', exc_info=True)
            st.error("An Error Occured!")

    def User_Input(self):
        """Capture and Handle User Input."""
        try:
            prompt = st.chat_input("Message KnowGenius...")
            if prompt:
                self.Message(prompt, is_user=True)
                st.session_state.messages.append({"role": "user", "content": prompt})

                with st.spinner("Thinking..."):
                    try:
                        response = requests.post(self.chatbot_api, json={'query': prompt})
                        response_json = response.json()
                        response_text = response_json.get('response', "An Error Occured!")
                    except Exception as e:
                        logging.error("Error while communicating with Chatbot API", exc_info=True)
                        response_text = "An Error Occured!"

                self.Message(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
        except Exception as e:
            logging.error('An error occurred while handling user input', exc_info=True)
            st.error("An Error Occured!")

    def run(self):
        """Run the Chatbot UI."""
        try:
            self.AppHeader(self.title)
            self.Initialize_Messages()
            self.Messages()
            self.User_Input()
        except Exception as e:
            logging.error('An error occurred during application execution', exc_info=True)
            st.error("An Error Occured!")

if __name__ == '__main__':
    app = ChatbotUI()
    app.run()