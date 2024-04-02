import logging
import streamlit as st
from datetime import datetime

from ..Utils import bootstrap_utils

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)

def Message(chat, is_user=False):
    try:
        bootstrap_utils()
        
        st.markdown(
            """
            <style>
                .user {
                    background: #262730;  
                    padding-top: 5px;
                    padding-left: 10px;
                    padding-right: 10px;
                    padding-bottom: 5px;
                    margin-left: 200px;
                    margin-right: 10px;
                    border-radius: 10px;
                    border-top-right-radius: 0px;
                    font-family: sans-serif;
                    font-size: 17px;
                  }
                      
                  .bot {
                      background: linear-gradient(rgb(0, 0, 128), rgb(255, 105, 180));
                      padding-top: 5px;
                      padding-left: 10px;
                      padding-right: 10px;
                      padding-bottom: 5px;
                      margin-left: 10px;
                      margin-right: 200px;
                      border-radius: 10px;
                      border-top-left-radius: 0px;
                      font-family: sans-serif;
                      font-size: 17px;
                  }
                  
                  @media screen and (max-width: 700px) {
                    .user {
                        font-size: 15px;
                       }
                           
                       .bot {
                           font-size: 15px;
                       }
                   }
                   
                   @media screen and (max-width: 570px) {
                    .user {
                        font-size: 12px;
                       }
                           
                       .bot {
                           font-size: 12px;
                       }
                   }
                   
                   @media screen and (max-width: 470px) {
                    .user {
                        font-size: 10px;
                       }
                           
                       .bot {
                           font-size: 10px;
                       }
                   }
                   
                   @media screen and (max-width: 400px) {
                    .user {
                        font-size: 7px;
                       }
                           
                       .bot {
                           font-size: 7px;
                       }
                   }
                   
                   @media screen and (max-width: 340px) {
                    .user {
                        font-size: 5px;
                       }
                           
                       .bot {
                           font-size: 5px;
                       }
                   }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        # current_time = datetime.now().strftime("%H:%M:%S")
        
        
        if is_user == False:
            st.markdown(f'''<div class="d-flex flex-row my-0 py-0">
                                <div class="row bot">
                                  <div>{chat}</div>
                                </div>
                            </div>''', unsafe_allow_html=True)
        else:
            st.markdown(f'''<div class="d-flex flex-row-reverse my-0 py-0">
                                <div class="row user">
                                  <div>{chat}</div>
                                </div>
                            </div>''', unsafe_allow_html=True)
        
    except Exception as e:
        logging.error('An Error Occured: ', exc_info=e)
        raise e