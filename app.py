from flask import Flask, request, jsonify, session
from flask_cors import CORS
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import requests

app = Flask(__name__)
app.secret_key = "super_secret_key"
CORS(app)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load ChromaDB collection
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("skinalyze_qa")


def ask_mistral_fallback(prompt):
    """
    Sends the user prompt to Mistral via Ollama as fallback.
    """
    system_prompt = (
        "You are a highly knowledgeable skin specialist. "
        "Respond to user concerns with accurate and helpful skincare advice."
    )

    response = requests.post(
        "http://localhost:11434/api/chat",  # Ollama API default
        json={
            "model": "mistral",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        }
    )

    response_json = response.json()
    return response_json.get("message", {}).get("content", "Sorry, I couldn't process your request.")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Embed and query ChromaDB
    query_embedding = model.encode([user_message])[0]
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=1
    )

    answer = None
    if results and results["distances"] and results["distances"][0][0] < 0.3:  # Similar enough
        answer = results["metadatas"][0][0]["answer"]

    # Fallback to Mistral
    if not answer:
        answer = ask_mistral_fallback(user_message)

    # Store history
    if "history" not in session:
        session["history"] = []

    session["history"].append({"user": user_message, "bot": answer})
    session.modified = True

    return jsonify({
        "reply": answer,
        "history": session["history"]
    })


@app.route("/history", methods=["GET"])
def history():
    return jsonify(session.get("history", []))


@app.route("/clear", methods=["POST"])
def clear():
    session["history"] = []
    return jsonify({"message": "History cleared."})


if __name__ == "__main__":
    app.run(debug=True)
