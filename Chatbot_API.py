import os
import sys
import logging
from flask import Blueprint, Flask, jsonify, request
from backend.src.SemanticAnalyzer import SemanticAnalyzer

# Configure Logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)

# Append Parent Directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class Chatbot:
    """
    Chatbot Class responsible for processing queries using Semantic Analyzer.
    """
    
    def __init__(self):
        """
        Initializes the Chatbot with a Semantic_Analyzer Instance.
        """
        self.analyzer = SemanticAnalyzer()

    def run(self, query: str) -> str:
        """
        Processes the Input query using the Semantic_Analyzer and returns the result.
        
        :param query: The query to be analyzed.
        :return: The result of the analysis.
        :raises Exception: If an error occurs during processing.
        """
        try:
            return self.analyzer.run(query)
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            raise e

class Chatbot_API:
    """
    Chatbot_API Class that sets up Flask Application with routes for Chatbot Interaction.
    """
    
    def __init__(self):
        """
        Initializes the Flask app and Chatbot blueprint, and sets up routes.
        """
        self.app = Flask(__name__)
        self.chatbot_blueprint = Blueprint('chatbot', __name__)
        self.chatbot_blueprint.add_url_rule('/', 'SERVER_STARTED', self.SERVER_STARTED, methods=['GET'])
        self.chatbot_blueprint.add_url_rule('/query', 'query', self.query, methods=['POST'])
        self.chatbot = Chatbot()

    def SERVER_STARTED(self) -> tuple:
        """
        Handles the root URL and returns a response indicating the server has started.
        
        :return: A tuple containing the JSON response and HTTP status code.
        :raises Exception: If an error occurs while handling the request.
        """
        try:
            return jsonify({'response': 200, 'SERVER STARTED': True}), 200
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            raise e

    def query(self) -> tuple:
        """
        Handles the /query URL, processes the input query, and returns the response.
        
        :return: A tuple containing the JSON response and HTTP status code.
        :raises Exception: If an error occurs while handling the request.
        """
        try:
            query = request.get_json().get("query", "")
            response = self.chatbot.run(query)
            return jsonify({'response': response}), 200
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            return jsonify({'Error': str(e)}), 400

    def run(self) -> None:
        """
        Starts the Flask Application with the registered blueprint.
        
        :raises Exception: If an error occurs while starting the server.
        """
        try:
            self.app.register_blueprint(self.chatbot_blueprint)
            self.app.run(debug=True)
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            raise e
        
if __name__ == '__main__':
    
    server = Chatbot_API()
    server.run()