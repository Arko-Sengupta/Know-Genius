import logging
import streamlit as st
from datetime import datetime
from ..Utils import bootstrap_utils

# Configure Logging
logging.basicConfig(level=logging.INFO)

def Message(chat, is_user=False):
    try:
        # Initialize Utilities
        bootstrap_utils()

        # Get the Current Date and Time
        current_time = datetime.now().strftime('%H:%M')

        # Define Custom CSS Style
        custom_css = """
        <style>
            .user, .bot {
                min-width: fit-content;  
                display: inline-block;
                position: relative;
                padding: 5px 10px;
                padding-bottom: 15px;
                margin-top: 10px;
                border-radius: 10px;
                font-family: sans-serif;
                font-size: 17px;
                overflow: hidden;
                word-wrap: break-word;
                white-space: normal;
                transition: transform 0.3s ease-in-out, background-color 0.3s ease-in-out;
            }
            .user {
                margin: 0 10px 0 auto;
                background: #262730;
                border-top-right-radius: 0px;
            }
            .bot {
                margin: 0 auto 0 10px;
                background: linear-gradient(135deg, #6c00a5, #b92b81);
                border-top-left-radius: 0px;
            }
            .user:hover, .bot:hover {
                cursor: pointer;
                transform: scale(1.05);
                background-color: #3b3b3b;
            }
            .timestamp {
                right: 10px;
                bottom: 5px;
                color: white;
                position: absolute;
                font-size: 8px;
            }
            /* Responsive Design */
            @media screen and (max-width: 700px) {
                .user, .bot { 
                    font-size: 15px; 
                    margin: 0 5px;
                }
                .timestamp { 
                    font-size: 9px; 
                }
            }
            @media screen and (max-width: 570px) {
                .user, .bot {
                    font-size: 12px;
                    min-width: 100px;
                    max-width: 100%;
                }
                .timestamp { 
                    font-size: 8px; 
                }
            }
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)

        # Determine Message Class (user or bot)
        message_class = "user" if is_user else "bot"

        # Display Chat Message with Timestamp
        st.markdown(f'''
            <div class="d-flex flex-row{'-reverse' if is_user else ''} my-0 py-0">
                <div class="row {message_class}">
                    <div>{chat}</div>
                    <div class="timestamp">{current_time}</div>
                </div>
            </div>
        ''', unsafe_allow_html=True)

    except Exception as e:
        logging.error(f'An Error Occurred while rendering the Message Component: {e}', exc_info=True)
        raise