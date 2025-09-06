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





