import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import gradio as gr

# Load your updated products.csv
df = pd.read_csv("products.csv")

# Generate smart product descriptions
def generate_description(row):
    return f"{row['Product']} for {row['Gender']} | Style: {row['Back_Style']}, Sleeves: {row['Sleeve_Length']}, Color: {row['Color']}, Size: {row['Size']} | Price: ${row['Price']}"

df["description"] = df.apply(generate_description, axis=1)
products = df["description"].tolist()

# Load embedding model
embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Setup ChromaDB
chroma_client = chromadb.Client(Settings(allow_reset=True))
chroma_client.reset()
collection = chroma_client.create_collection(name="clothing", embedding_function=embedding_fn)

# Add product data
collection.add(
    documents=products,
    ids=[str(i) for i in range(len(products))]
)

# Define rude words list
rude_words = ["damn", "shit", "fuck", "idiot", "dumb", "bitch", "hell"]

# Main chatbot logic
def chatbot_response(user_input):
    query = user_input.strip().lower()

    if any(word in query for word in rude_words):
        return "❌ Please keep the conversation respectful."

    if query in ["hi", "hello", "hey"]:
        return "👗 Hi there! Welcome to our clothing store. Ask me anything — dresses, sizes, prices, etc."

    if "order" in query or "buy" in query:
        return "✅ Your order has been placed! We'll get it ready for shipping. Thanks for shopping with us!"

    result = collection.query(query_texts=[user_input], n_results=1)
    if result and result["documents"]:
        return f"🛍️ {result['documents'][0][0]}"

    return "🙁 Sorry, I couldn’t find anything that matches. Could you rephrase your question?"

# Gradio chatbot UI
interface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="🧠 Smart Fashion Chatbot",
    description="Ask me about our products — dresses, t-shirts, jeans, sizes, prices, etc.",
    css="pink_theme.css"
)

# Run the app
if __name__ == "__main__":
    interface.launch()
