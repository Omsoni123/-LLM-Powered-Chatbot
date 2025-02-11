# AI-Powered Chatbot using Pinecone & Sentence Transformers

## 🚀 Project Overview
This project is a **smart chatbot** that retrieves answers from stored documents using **vector search**. It leverages **Pinecone for vector storage**, **Sentence Transformers for embeddings**, and **Streamlit for an interactive UI**. The chatbot can efficiently fetch relevant information based on user queries.

## 🛠 Tech Stack Used
- **Python** (Core language for development)
- **Pinecone** (Vector database for storing embeddings)
- **Sentence Transformers** (Embedding model for vector representation)
- **Streamlit** (For a simple and interactive web UI)
- **LangChain** (For seamless query processing)


## 🔧 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Omsoni123/-LLM-Powered-Chatbot.git
cd -LLM-Powered-Chatbot
```

### 2️⃣ Install Required Packages
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Pinecone
- Sign up on **[Pinecone](https://www.pinecone.io/)** and get your **API key**.
- Initialize Pinecone inside `vector_storage.py`.
- Ensure your index name is correctly mentioned.

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 🛠 How It Works
1️⃣ **Data Processing**: Loads documents, converts them into vector embeddings using **Sentence Transformers**, and stores them in **Pinecone**.  
2️⃣ **Query Handling**: Takes user input, converts it into a vector, and retrieves the most relevant information from **Pinecone**.  
3️⃣ **Response Generation**: Displays the best-matching response on **Streamlit UI**.  

## 🔍 Example Queries
Try asking questions like:
- *"What is the budget allocation for this project?"*
- *"Tell me about financial planning."*
- *"Summarize the key aspects of the report."*

## 📸 Demo Screenshot
![image](https://github.com/user-attachments/assets/45b9795a-3dba-4c01-96ee-179a867d8647)
![image](https://github.com/user-attachments/assets/278b8c24-0255-478d-9542-2e0a2a7aded5)


## 🎯 Future Improvements
- Integrate OpenAI or LLaMA for **response generation**.
- Add support for **multiple languages**.
- Improve **retrieval accuracy** using **better embeddings**.

## 🤝 Contribution
Feel free to **fork** this repo and submit pull requests for improvements!

## 🏆 Acknowledgments
- **Pinecone** for vector search
- **Hugging Face** for Sentence Transformers
- **LangChain** for simplifying retrieval workflows

---
🌟 **Like this project? Give it a star ⭐ and connect with me on [LinkedIn](https://www.linkedin.com/in/om-soni-8b0643231/)!**

