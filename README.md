# Telegram Chatbot with Retrieval-Augmented Generation (RAG)

This project demonstrates a Telegram chatbot powered by Retrieval-Augmented Generation (RAG) using the LLaMA 3 model from Hugging Face. The bot is designed to provide intelligent responses based solely on the information retrieved from relevant documents. It integrates various technologies like LLaMA 3 for NLP tasks Word embedding  and ChromaDB for document storage.

## Features
- Intelligent responses based on retrieved documents
- Built using Telegram Bot API with the bot name `info_ai`
- Uses the LLaMA 3 model for response generation
- Retrieves information from a custom knowledge base
- Uses ChromaDB for storing documents

## Requirements
- Python 3.8+
- `python-telegram-bot` library
- `langchain.llms` library (for LLaMA 3)
- `huggingface_hub` library
- `langchain` library
- `chromadb` library
  

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hirenkhokhar/telegram_chatbot_using_rag.git
   cd telegram-chatbot-rag
