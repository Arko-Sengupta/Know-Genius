import re
import nltk
import logging
import pandas as pd
from nltk.corpus import words
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.metrics import edit_distance
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# nltk.download('stopwords')
# nltk.download('punkt')

class Semantic_Analyzer:
    
    def __init__(self) -> None:
        self.ErrorMessage = 'Can you please elaborate your question so that I can understand it properly!'
    
    def Sanitize_String(self, text):
        try:
            return re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
        
    def Preprocess_Stopwords(self, text):
        try:
             filtered_words = [word for word in word_tokenize(text) if word not in set(stopwords.words('english'))]
             return ' '.join(filtered_words)
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
        
    def Synonym_List(self, word):
        try:
            synonyms = []
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name().lower())
            return list(set(synonyms))
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
        
    def Synonym_String(self, text):
        try:
            synonym_lists = [self.Synonym_List(word) for word in word_tokenize(text)]
            return ' '.join([synonym for synonym_list in synonym_lists for synonym in synonym_list])
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
    
    def CosineSimilarity(self, query, question):
        try:
            query = self.Sanitize_String(query)
            query = self.Preprocess_Stopwords(query)
            query = self.Synonym_String(query)
            
            question = self.Sanitize_String(question)
            question = self.Preprocess_Stopwords(question)
            question = self.Synonym_String(question)
            
            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([query, question])
            
            similarity = cosine_similarity(vectors)
            
            return similarity[0][1]
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e
        
    def run(self, df, query):
        try:
            df['Similarity'] = df['Question'].apply(lambda x: self.CosineSimilarity(query, x))
            df['Question'] = df['Question'].drop_duplicates()
            df = df.dropna()
            
            if max(df['Similarity'].tolist()) >= 0.5:
                return df.loc[df['Similarity'] == max(df['Similarity'].tolist()), 'Answer'].iloc[0]
            return self.ErrorMessage
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e