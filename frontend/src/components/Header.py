import logging
import streamlit as st
from ..Utils import bootstrap_utils

# Configure Logging
logging.basicConfig(level=logging.INFO)

def AppHeader(title):
    try:
        # Initialize Utilities
        bootstrap_utils()
        
        # Define Custom CSS Style
        custom_css = """
        <style>
            .fs {
                font-size: 45px;
                font-weight: bold;
            }
            @media screen and (max-width: 650px) {
                .fs {
                    font-size: 30px;
                }
            }
            @media screen and (max-width: 400px) {
                .fs {
                    font-size: 20px;
                }
            }
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)
        
        # Display Title
        st.markdown(f'''<p class="fs">{title}</p>''', unsafe_allow_html=True)
    
    except Exception:
        logging.error('An error occurred while rendering the AppHeader:', exc_info=True)
        raise