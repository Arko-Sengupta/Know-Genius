import logging
import streamlit as st

def bootstrap_utils():
    try:
        st.markdown("""
            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            
            <!-- jQuery -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            
            <!-- Popper.js -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            
            <!-- Bootstrap Bundle with Popper -->
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        logging.error('An error occurred while loading Bootstrap Utilities:', exc_info=e)
        raise e
