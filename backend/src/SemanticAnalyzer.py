import re
import json
import logging
import pandas as pd
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set Up Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SemanticAnalyzer:
    
    def __init__(self, dataset_path='backend/data/General_Knowledge_Data.json') -> None:
        """
        Initialize the Semantic Analyzer with the path to the dataset.
        """
        self.dataset_path = dataset_path
        
    def ConvertToDataframe(self) -> pd.DataFrame:
        """
        Load the dataset from JSON and convert it to a Pandas DataFrame.
        """
        try:
            with open(self.dataset_path, 'r') as file:
                data = json.load(file)
            return pd.DataFrame(data)
        except Exception as e:
            logging.error("Error loading dataset: ", exc_info=True)
            raise e
    
    def Sanitize_String(self, text: str) -> str:
        """
        Sanitize the Input Text by removing non-alphanumeric characters and converting to lowercase.
        """
        try:
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
            return ' '.join(text.split())
        except Exception as e:
            logging.error('Error sanitizing string: ', exc_info=True)
            raise e
        
    def Preprocess_Stopwords(self, text: str) -> str:
        """
        Remove stopwords from the Input Text.
        """
        try:
            filtered_words = [word for word in word_tokenize(text) if word not in set(stopwords.words('english'))]
            return ' '.join(filtered_words)
        except Exception as e:
            logging.error('Error preprocessing stopwords: ', exc_info=True)
            raise e
        
    def Synonyms_List(self, word: str) -> list:
        """
        Retrieve a list of synonyms for a given word.
        """
        try:
            synonyms = set()
            for syn in wordnet.synsets(word):
                synonyms.update(lemma.name().lower() for lemma in syn.lemmas())
            return list(synonyms)
        except Exception as e:
            logging.error('Error getting synonyms: ', exc_info=True)
            raise e
        
    def Synonyms_String(self, text: str) -> str:
        """
        Replace words in the text with their synonyms.
        """
        try:
            words = word_tokenize(text)
            expanded_words = [synonym for word in words for synonym in self.Synonyms_List(word)]
            return ' '.join(expanded_words)
        except Exception as e:
            logging.error('Error expanding with synonyms: ', exc_info=True)
            raise e
        
    def Preprocess_Text(self, text: str) -> str:
        """
        Sanitize, remove stopwords, and expand the text with synonyms.
        """
        try:
            text = self.Sanitize_String(text)
            text = self.Preprocess_Stopwords(text)
            text = self.Synonyms_String(text)
            return text
        except Exception as e:
            logging.error("Error preprocessing text: ", exc_info=True)
            raise e
    
    def Cosine_Similarity(self, query: str, question: str) -> float:
        """
        Compute the Cosine Similarity between the query and the question.
        """
        try:
            query = self.Preprocess_Text(query)
            question = self.Preprocess_Text(question)
            
            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([query, question])
            
            similarity = cosine_similarity(vectors)
            return similarity[0][1]
        except Exception as e:
            logging.error('Error computing cosine similarity: ', exc_info=True)
            raise e
        
    def run(self, query: str) -> str:
        """
        Run the Semantic Analysis on the query and return the most similar answer from the dataset.
        """
        try:
            df = self.ConvertToDataframe()
            
            df['similarity'] = df['question'].apply(lambda x: self.Cosine_Similarity(query, x))
            df = df.drop_duplicates(subset=['question']).dropna(subset=['similarity'])
            
            max_similarity = df['similarity'].max()
            if max_similarity >= 0.85:
                return df.loc[df['similarity'] == max_similarity, 'answer'].iloc[0]
            return "Unable to Analyze"
        except Exception as e:
            logging.error('Error in run method: ', exc_info=True)
            raise e