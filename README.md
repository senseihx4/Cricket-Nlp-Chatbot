# Cricket NLP Chatbot

A Streamlit-based Q&A search app for IPL 2026 cricket questions. It uses TF-IDF vectorization combined with fuzzy matching to find the best answer from a dataset of cricket Q&A pairs.

## How It Works

1. Your question is preprocessed (lowercased, stopwords removed)
2. TF-IDF cosine similarity finds semantically close questions in the dataset
3. RapidFuzz partial ratio scores exact/fuzzy keyword matches
4. Both scores are combined (40% fuzzy + 60% TF-IDF) to pick the best answer
5. If no confident match is found, it replies: *"Sorry, I don't know about that!"*

## Setup

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run nlpproject.py
```

## Project Structure

```
NLP-project/
├── nlpproject.py        # Main Streamlit app
├── requirements.txt     # Python dependencies
└── data/
    └── ipl2026data.csv  # Cricket Q&A dataset
```

## Dependencies

- `streamlit` — web UI
- `pandas` — data loading
- `scikit-learn` — TF-IDF vectorization & cosine similarity
- `rapidfuzz` — fuzzy string matching
