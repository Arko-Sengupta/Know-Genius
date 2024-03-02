from sentence_transformers import SentenceTransformer, util

# Load pre-trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example dataset
dataset = [
    "How does photosynthesis work?",
    "Explain the process of photosynthesis.",
    "What is the mechanism behind photosynthesis?",
    "What are the Vowels in English Alphabets?",
    "How many days did we have in a week?",
    "How many weeks are there in a month?"
]

# User's question
user_question = "What is the count of days within a week?"

# Encode all questions in the dataset and the user's question
encoded_dataset = model.encode(dataset, convert_to_tensor=True)
encoded_user_question = model.encode(user_question, convert_to_tensor=True)

# Calculate cosine similarity between user's question and each question in the dataset
cosine_scores = util.pytorch_cos_sim(encoded_user_question, encoded_dataset)[0]

# Find the index of the most similar question
most_similar_index = cosine_scores.argmax().item()

# Print the most similar question
print("User's Question:", user_question)
print("Most Similar Question:", dataset[most_similar_index])
print("Cosine Similarity Score:", cosine_scores[most_similar_index].item())
