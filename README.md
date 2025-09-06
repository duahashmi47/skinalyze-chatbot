# 🧴 Skinalyze Chatbot

Skinalyze is an intelligent skincare Q&A chatbot built with **Flask**, **ChromaDB**, and **SentenceTransformers**. It provides accurate, context-aware responses to user queries using a hybrid approach: semantic search over a curated dermatology dataset, with fallback to a local **Mistral** model via **Ollama**.

---

## 🚀 Features

- 🔍 **Semantic Search**: Uses sentence embeddings to retrieve relevant answers from a dermatology-focused ChromaDB collection.
- 🧠 **LLM Fallback**: If no close match is found, queries are routed to a local Mistral model for generative responses.
- 📚 **Multi-source QA Loader**: Combines public datasets and custom JSON files to build a rich knowledge base.
- 🧵 **Session History**: Tracks user-bot interactions across sessions.
- 🧼 **Clear History Endpoint**: Allows users to reset their conversation.

---

## 🛠️ Tech Stack

| Component            | Description                                      |
|---------------------|--------------------------------------------------|
| Flask               | Web framework for API endpoints                  |
| SentenceTransformers | Embedding model (`all-MiniLM-L6-v2`)             |
| ChromaDB            | Vector database for semantic search              |
| HuggingFace Datasets| Loads dermatology and skincare QA datasets       |
| Ollama + Mistral    | Local LLM fallback for unmatched queries         |
| Flask-CORS          | Enables cross-origin requests                    |

---

## 📂 Project Structure
skinalyze-chatbot/ ├── app.py             # Flask app with chat, history, and clear endpoints 
                   ├── qa_loader.py       # Loads and embeds QA data into ChromaDB 
                   ├── skincare_qa.json   # (Optional) Custom QA pairs 
                   ├── chroma_db/         # Persistent ChromaDB storage

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/duahashmi47/skinalyze-chatbot.git
cd skinalyze-chatbot
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Rub the QA Loader
This script embeds questions and stores them in ChromaDB:
```bash
python qa_loader.py
```

### 4. Start Ollama (Mistral)
Ensure Ollama is running locally with the Mistral model:
```bash
ollama pull mistral
ollama run mistral
```
### 5. Launch the Flask App
```bash
python app.py
```

## 📡 API Endpoints

| Endpoint | Method | Description                         |
|----------|--------|-------------------------------------|
| /chat    | POST   | Accepts user message, returns reply | 
| /history | GET    | Returns session chat history        | 
| /clear   | POST   | Clears session history              | 


## 🧪 Example Request
```bash
POST /chat
Content-Type: application/json

{
  "message": "What’s the best routine for oily skin?"
}
```


## 📌 Notes
- The chatbot first attempts to find a relevant answer via ChromaDB. If no match is found (distance > 0.3), it falls back to Mistral.
- You can customize the QA dataset by editing skincare_qa.json.

## 🙌 Acknowledgements
- Mreeb/Dermatology-Question-Answer-Dataset-For-Fine-Tuning
- UrFavB0i/skincare-ecommerce-FAQ
- Ollama for local LLM integration

## 📬 Contact
Built with 💡 by Dua Hashmi
Feel free to reach out or contribute!

---








