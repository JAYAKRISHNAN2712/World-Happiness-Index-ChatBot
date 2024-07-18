# World-Happiness-Index-ChatBot

Welcome to the World Happiness Report Chatbot! This interactive chatbot allows users to query insights from the World Happiness Report 2024. It utilizes advanced natural language processing techniques along with Retrieval Augmented Generation(RAG) to deliver information in a user-friendly manner.

## Table of Contents

- [Prerequisites](#prerequisites)
- [File Descriptions](#file-descriptions)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
  
## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- Required libraries (see Installation)

## File Descriptions

1. **ChatBot.py**:  
   Contains the Streamlit code for the chatbot interface, allowing user interaction and queries about the World Happiness Report.

2. **DataLoader.py**:  
   A custom data loader class that processes the World Happiness Report 2024 PDF, encoding its contents into a `langchain.schema.Document` using the `unstructured.io` library.  

3. **VectorDB.py**:  
   Implements a custom vector database using ChromaDB for efficient storage and retrieval of document embeddings.

4. **RAG_initializers.py**:  
   Initializes the retrieval-augmented generation (RAG) model, setting up the language model (LLM) and custom templates for user query processing.

5. **RetrievalChain.py**:  
   Defines a class for "Question-Answering" with integrated "Memory" using Langchain, enabling context-aware interactions with users.

## Installation

To set up the World Happiness Report Chatbot, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/JAYAKRISHNAN2712/world-happiness-report-chatbot.git
   cd world-happiness-report-chatbot/source

2. Run **requirements.txt**
   ```bash
   pip install -r requirements.txt

## Usage

To run the chatbot, execute the following command:

    ```bash
      streamlit run ChatBot.py

## Project Structure

```plaintext
World-Happiness-Index-ChatBot/source/
│
├── ChatBot.py          
├── DataLoader.py         
├── RAG_initializers.py          
├── RetrievalChain.py         
├── VectorDB.py
├── requirements.txt# List of required dependencies

World-Happiness-Index-ChatBot/input-data
│
├── WHR+24.pdf       # WHR -2024 pdf

World-Happiness-Index-ChatBot/
│
├── README.md      # Project Documentation
