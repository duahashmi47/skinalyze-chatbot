import os
import json
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import chromadb

client = chromadb.PersistentClient(path="chroma_db")
collection_name = "skinalyze_qa"

# Recreate collection (delete if exists)
if collection_name in [c.name for c in client.list_collections()]:
    client.delete_collection(name=collection_name)

collection = client.create_collection(name=collection_name)

def load_questions():
    # Load datasets
    ds1 = load_dataset("Mreeb/Dermatology-Question-Answer-Dataset-For-Fine-Tuning", split="train")
    
    ds2 = load_dataset("UrFavB0i/skincare-ecommerce-FAQ", split="train")

    questions = []
    answers = []

    for row in ds1:
        questions.append(row["prompt"])
        answers.append(row["response"])

    for row in ds2:
        questions.append(row["Buyer"])
        answers.append(row["AI Assistant"])

    # Load your own dataset
    if os.path.exists("skincare_qa.json"):
        with open("skincare_qa.json", "r", encoding="utf-8") as f:
            custom_data = json.load(f)
        for pair in custom_data:
            questions.append(pair["prompt"])
            answers.append(pair["response"])

    return questions, answers

def embed_all_questions():
    questions, answers = load_questions()

    print(f"Embedding {len(questions)} questions...")

    # Load local embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(questions, convert_to_numpy=True)

    # Setup Chroma
    client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="chroma_db"))
    if "skinalyze" in client.list_collections():
        client.delete_collection("skinalyze")
    collection = client.create_collection("skinalyze")

    for i, (q, a, emb) in enumerate(zip(questions, answers, embeddings)):
        collection.add(
            ids=[str(i)],
            documents=[q],
            embeddings=[emb.tolist()],
            metadatas=[{"answer": a}]
        )

    print("Done! All questions embedded and stored.")

if __name__ == "__main__":
    embed_all_questions()
