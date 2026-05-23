import os
import streamlit as st
from rapidfuzz import fuzz
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocess(text):
    text = text.lower()
    tokens = text.split()
    stop_words = set([
        "the", "is", "in", "and", "to", "of", "a", "that", "it", "with",
        "as", "for", "was", "on", "are", "by", "this", "be", "from",
        "or", "which", "at", "an"
    ])
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return " ".join(filtered_tokens)


@st.cache_resource
def load_data():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'ipl2026data.csv')
    data = pd.read_csv(data_path)
    data['processed_question'] = data['question'].apply(preprocess)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(data['processed_question'])
    return data, vectorizer, tfidf_matrix


st.title("Cricket Q&A Search")

data, vectorizer, tfidf_matrix = load_data()

query = st.text_input("Enter your question:")

if query:
    input_tfidf = vectorizer.transform([preprocess(query)])
    similarity_scores = cosine_similarity(input_tfidf, tfidf_matrix)

    df = data.copy()
    df['fuzzy_score'] = df['question'].apply(lambda x: fuzz.partial_ratio(x, query))
    df['tfidf_score'] = similarity_scores.flatten()
    df['final_score'] = (df['fuzzy_score'] * 0.4) + (df['tfidf_score'] * 100 * 0.6)

    best_match = df.loc[df['final_score'].idxmax()]

    if best_match['tfidf_score'] > 0.3 or best_match['fuzzy_score'] > 80:
        answer_text = best_match['answer']
    else:
        answer_text = "Sorry, I don't know about that!"

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #1e1e2f, #2a2a4a);
            border-left: 4px solid #7c6af7;
            border-radius: 12px;
            padding: 24px 28px;
            margin-top: 20px;
            box-shadow: 0 4px 20px rgba(124, 106, 247, 0.2);
        ">
            <p style="
                color: #a89cf7;
                font-size: 12px;
                font-weight: 600;
                letter-spacing: 1.5px;
                text-transform: uppercase;
                margin: 0 0 10px 0;
            ">Answer</p>
            <p style="
                color: #f0eeff;
                font-size: 17px;
                line-height: 1.7;
                margin: 0;
            ">{answer_text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
