import os
import sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.processed_data.Dataset import PrepareDataset
from src.models.SemanticAnalyze import Semantic_Analyzer

class Chatbot:
    
    def __init__(self):
        self.df = PrepareDataset().run()
        
    def run(self, query):
        try:
            analyzer = Semantic_Analyzer()
            
            response = analyzer.run(self.df, query)
            return response
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e