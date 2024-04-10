import os
import sys
import logging
from flask import Blueprint, Flask, jsonify, request

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.src.PrepareDataset import PrepareDataset
from backend.src.SemanticAnalyzer import Semantic_Analyzer

class Chatbot:
    
    def __init__(self):
        self.dataPrep = PrepareDataset()
        self.analyzer = Semantic_Analyzer()
        
    def PrepareData(self):
        try:
            return self.dataPrep.run()
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
        
    def run(self, query):
        try:
            self.df = self.PrepareData()
            response = self.analyzer.run(self.df, query)
            return response
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e

class BACKEND_SERVER:

    def __init__(self):
        self.app = Flask(__name__)
        self.chatbot_blueprint = Blueprint('chatbot', __name__)
        self.chatbot_blueprint.add_url_rule('/', 'SERVER_STARTED', self.SERVER_STARTED, methods=['GET'])
        self.chatbot_blueprint.add_url_rule('/query', 'query', self.query, methods=['POST'])
        self.chatbot = Chatbot()
        
    def SERVER_STARTED(self):
        try:
            return jsonify({'response': 200, 'SERVER STARTED': True}), 200
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e

    def query(self):
        try:
            query = request.get_json()['query']
            response = self.chatbot.run(query)
            return jsonify({'response': response}), 200
        except Exception as e:
            logging.error('An Error Occurred: ', exc_info=e)
            return jsonify({'Error': str(e)}), 400
        
    def run(self):
        try:
            self.app.register_blueprint(self.chatbot_blueprint)
            self.app.run(debug=True)
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
        
if __name__=='__main__':
      
    server = BACKEND_SERVER()
    server.run()