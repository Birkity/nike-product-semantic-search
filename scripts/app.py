import streamlit as st
import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet', quiet=True)

# Load preprocessed data with embeddings
@st.cache
def load_data():
    data = pd.read_csv('../data/semantic_search_with_embeddings.csv')
    cached_embeddings = joblib.load('../data/embeddings_cache.joblib')
    return data, cached_embeddings

data, cached_embeddings = load_data()

# Initialize SBERT model
@st.cache
def load_model():
    return SentenceTransformer('paraphrase-MiniLM-L6-v2')

model = load_model()

# Knowledge Graph Simulation
G = nx.DiGraph()
for _, row in data.iterrows():
    G.add_node(row['name'], type='Product', description=row['description'], color=row['dominant_color'])
    G.add_edge(row['name'], row['dominant_color'], type='has_color')

# Query Expansion Function
def expand_query(query):
    terms = query.split()
    expanded_terms = []
    for term in terms:
        synsets = wordnet.synsets(term)
        if synsets:
            for lemma in synsets[0].lemmas():
                expanded_terms.append(lemma.name())
    return list(set(expanded_terms + terms))

# Search Function with Query Expansion
def search_with_expansion(query, data):
    expanded_query = expand_query(query)
    query_embedding = model.encode(' '.join(expanded_query))
    similarities = cosine_similarity([query_embedding], cached_embeddings)
    top_indices = similarities[0].argsort()[-5:][::-1]
    return top_indices, similarities[0][top_indices]

# Knowledge Graph Query Function
def query_knowledge_graph(query, G):
    results = []
    query_lower = query.lower()
    for node, attributes in G.nodes(data=True):
        if attributes.get('type') == 'Product':
            if query_lower in attributes['description'].lower() or query_lower in attributes['color'].lower():
                results.append((node, attributes['description'], attributes['color']))
    return results[:5] if results else []

# Streamlit App UI
st.title('Nike Product Semantic Search Engine')

# User Input
query = st.text_input("Enter your search query:")

# Filter Options
filter_options = st.multiselect(
    "Filter by Color",
    options=data['dominant_color'].unique()
)

# Search Button
if st.button('Search'):
    if query:
        # Perform Search
        indices, scores = search_with_expansion(query, data)
        
        # Filter by selected colors
        if filter_options:
            filtered_data = data[data['dominant_color'].isin(filter_options)]
            filtered_indices = [idx for idx in indices if data.iloc[idx]['name'] in filtered_data['name'].values]
            indices = filtered_indices[:5]  # Limit to top 5 after filtering
        
        st.subheader(f"Top 5 results for query '{query}':")
        for idx, score in zip(indices, scores):
            product = data.iloc[idx]
            st.write(f"- **{product['name']}** - {product['sub_title']} (Score: {score:.4f})")
            st.write(f"  **Description:** {product['description'][:100]}...")
            st.write("---")
        
        # Knowledge Graph Results
        kg_results = query_knowledge_graph(query, G)
        if kg_results:
            st.subheader("Knowledge Graph Results:")
            for name, desc, color in kg_results:
                st.write(f"- **Name:** {name}, **Color:** {color}")
                st.write(f"  **Description:** {desc[:100]}...")
                st.write("---")
        else:
            st.write("No knowledge graph results found for the query.")
    else:
        st.warning("Please enter a search query.")

# Running the app
if __name__ == '__main__':
    st.write("Welcome to the Nike Product Search Engine!")