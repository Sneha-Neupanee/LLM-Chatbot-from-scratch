# LLM Chatbot for Fashion Store 👗✨

Welcome to **Smart Fashion Chatbot**, a locally running, AI-powered chatbot built from scratch using Python, Gradio, ChromaDB, and Sentence Transformers. This chatbot helps users find fashion items (like dresses, t-shirts, shoes, undergarments, etc.) from a CSV product catalog — using intelligent semantic search.


## Features

-  Ask questions like "Do you have pink crop tops?" or "Show me blue XL hoodies"
-  Uses LLM-style embedding search via **Sentence Transformers**
-  Product catalog sourced from `products.csv`
-  Fully themed UI with **sparkles, pink colors, animations, custom cursor**
-  Responds politely even to rude users
-  Simulated ordering feature — just say “order this!”

---

## Technologies Used

| Tech         | Purpose                                 |
|--------------|-----------------------------------------|
| Python       | Core programming language               |
| Gradio       | Frontend UI for chatbot interaction     |
| ChromaDB     | Local vector store (no OpenAI needed)   |
| SentenceTransformers | Generates embeddings for product descriptions |
| Pandas       | Reads and formats product CSV           |

---

##  Installation Guide

###  Clone the Repo

```bash
git clone https://github.com/Sneha-Neupanee/LLM-Chatbot-from-scratch.git
cd LLM-Chatbot-from-scratch
