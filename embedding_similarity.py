from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.mnetrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)
documents= [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
    "Islamabad is the capital of Pakistan",
    "Beijing is the capital of China",
]

query = "What is the capital of Pakistan?"

doc_embeddings = embedding.embed_documents(documents) 
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

# print(np.max(scores))
index , scores = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
print(f"Most similar document: {documents[index]} with score: {scores}")
