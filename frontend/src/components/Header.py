import logging
import streamlit as st

from ..Utils import bootstrap_utils

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)

def AppHeader(title):
    try:
        bootstrap_utils()
        
        st.markdown(
            """
            <style>
                .fs {
                    font-size: 50px;
                    font-weight: bold;
                }
                
                @media screen and (max-width: 650px) {
                    .fs {
                        font-size: 30px;
                    }
                }
                
                @media screen and (max-width: 400px) {
                    .fs {
                        font-size: 15px;
                    }
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(f'''<p class="container fs text-center">{title}</p>''', unsafe_allow_html=True)
    except Exception as e:
        logging.error('An Error Occured: ', exc_info=e)
        raise e
