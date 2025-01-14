# 🎯 Nike Product Semantic Search Engine

Welcome to the **Nike Product Semantic Search Engine**, an innovative solution designed to revolutionize product recommendations on Nike's e-commerce platform. This repository contains everything you need to run, understand, and extend this semantic search tool.

---

## 🌟 Project Overview

This project aims to create a **domain-specific semantic search tool** tailored for Nike products. By leveraging advanced **natural language processing (NLP)** techniques like Sentence-BERT (SBERT), the search engine provides a smarter, more intuitive way to match queries with relevant products.

### 🔑 Key Features

- **Semantic Search**: Context-aware search using SBERT embeddings.
- **Query Expansion**: Expands search queries with synonyms for better results.
- **Knowledge Graph Simulation**: Visualizes product relationships using NetworkX.
- **User-Friendly Interface**: Built with **Streamlit** for a seamless user experience.
- **Optimized Performance**: Embedding caching for lightning-fast search operations.

---

## 📁 Repository Structure

```plaintext
├── notebooks/
│   ├── data_preprocessing.ipynb    # Data cleaning and preparation
│   ├── EDA.ipynb                   # Exploratory data analysis
│   └── search_engine.ipynb         # Core search engine development
├── scripts/
│   └── app.py                      # Streamlit-based user interface
├── data/
│   ├── semantic_search_ready_data.csv      # Preprocessed product data
│   ├── semantic_search_with_embeddings.csv # Dataset with embeddings
│   └── embeddings_cache.joblib             # Cached embeddings
🚀 Getting Started
🛠️ Prerequisites
Ensure you have the following installed:

Python 3.8 or higher
Libraries: pandas, numpy, scikit-learn, sentence-transformers, nltk, networkx, streamlit, joblib
⚙️ Setting Up Your Environment
Clone the Repository:

bash
Copy code
git clone https://github.com/Birkity/nike-product-semantic-search.git
cd nike-product-semantic-search
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv myenv
source myenv/bin/activate  # Windows: myenv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
🏃‍♀️ Running the Application
1. Data Preprocessing
Open data_preprocessing.ipynb in Jupyter Notebook or Google Colab and run through the cells to:

Clean data
Handle missing values
Prepare data for NLP tasks
2. Exploratory Data Analysis (EDA)
Run EDA.ipynb to gain insights into:

Dataset distribution
Key relationships
Visualized metrics for search relevance
3. Build the Search Engine
Use search_engine.ipynb to:

Compute SBERT embeddings
Implement semantic search with cosine similarity
Expand queries and simulate product relationships with a knowledge graph
4. Launch the User Interface
From the /scripts directory, run:

bash
Copy code
streamlit run app.py
This will start a local web server with a user-friendly interface for searching products.

💡 Usage
Enter a Search Query: Type your query (e.g., "running shoes for men") in the input field.

Filter Results (Optional): Select product colors from the dropdown menu.

View Results: Click Search to see:

Top 5 results ranked by relevance
Knowledge graph insights (if applicable)
🖼️ Example Queries and Outputs
Query: "running shoes for men"
Result: Displays products like Nike Air Pegasus 83 Premium, highlighting features like running and comfort.
Query: "soccer"
Result: Recommends soccer-related gear, e.g., Chelsea FC Strike track jackets, focusing on training needs.

Replace this placeholder with an actual screenshot of your app.

🤝 Contributing
We welcome contributions! 🎉
If you have ideas for enhancements or bug fixes, feel free to:

Fork the repository
Create a new branch
Submit a pull request
```
