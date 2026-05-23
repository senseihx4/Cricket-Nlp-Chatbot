# 🏏 Cricket NLP Chatbot
 
A smart cricket Q&A chatbot built with NLP techniques — no NLTK, no spaCy. Uses fuzzy matching and TF-IDF cosine similarity to understand user questions even with typos and mistakes.
 
![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-UI-red) ![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)
 
---
 
## 🚀 What It Does
 
- Answers cricket questions from a pre-built IPL 2025 dataset
- Understands questions even with **spelling mistakes**
- Uses **Fuzzy Matching** to handle typos
- Uses **TF-IDF + Cosine Similarity** to understand meaning
- Combines both scores for the **best possible answer**
- Says *"Sorry, I don't know"* when the question is off-topic
- Clean **Streamlit web UI**
---
 
## 🧠 How It Works
 
```
User Question
      ↓
Preprocess (lowercase, remove stop words)
      ↓
Layer 1 — Fuzzy Matching (handles typos)
Layer 2 — TF-IDF + Cosine Similarity (handles meaning)
      ↓
Combined Score
      ↓
Best Answer or "Sorry, I don't know"
```
 
---
 
## 📁 Project Structure
 
```
cricket-nlp-chatbot/
│
├── data/
│   └── qa_data.csv          # IPL 2025 Q&A dataset
│
├── nlpproject.py            # Main Streamlit app
├── requirements.txt         # All dependencies
└── README.md
```
 
---
 
## ⚙️ Installation
 
### 1. Clone the repository
 
```bash
git clone https://github.com/yourusername/cricket-nlp-chatbot.git
cd cricket-nlp-chatbot
```
 
### 2. Create a virtual environment
 
```bash
python -m venv venv
```
 
Activate it:
 
- **Mac/Linux:**
```bash
source venv/bin/activate
```
 
- **Windows:**
```bash
venv\Scripts\activate
```
 
### 3. Install requirements
 
```bash
pip install -r requirements.txt
```
 
---
 
## ▶️ Run the App
 
```bash
streamlit run nlpproject.py
```
 
Then open your browser at `http://localhost:8501`
 
---
 
## 📦 requirements.txt
 
```
streamlit
pandas
scikit-learn
rapidfuzz
python-dotenv
```
 
---
 
## 💬 Example Questions You Can Ask
 
| Question | Answer |
|---|---|
| Who won IPL 2025? | RCB won IPL 2025 |
| Best bowler in IPL? | Josh Hazlewood - Purple Cap |
| Who has orange cap? | B Sai Sudharsan - 679 runs |
| Did Kohli win IPL? | Yes, first title in 2025 |
| Woh won ipl 2025? | RCB (handles typos!) |
 
---
 
## 🔧 Tech Stack
 
| Tool | Purpose |
|---|---|
| `pandas` | Load and manage Q&A data |
| `rapidfuzz` | Fuzzy string matching for typos |
| `scikit-learn` | TF-IDF vectorizer + cosine similarity |
| `streamlit` | Web UI |
 
---
 
## 🚫 Constraints
 
This project was built **without**:
- ❌ NLTK
- ❌ spaCy
All text processing is done manually using pure Python and allowed libraries only.
