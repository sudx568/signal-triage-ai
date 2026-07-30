#  Signal Triage AI

An AI-powered customer signal classification platform that automatically analyzes incoming issues, predicts categories, calculates confidence, assigns priority, and recommends actions.


##  Features

- AI based customer issue classification
- FastAPI backend API
- React dashboard interface
- Confidence scoring
- Priority detection
- Automatic action recommendation
- Prediction history tracking


## System Architecture


User
  ↓
React Dashboard
 |
 ↓
FastAPI API
 |
 ↓
ML Engine
 |
 ├── Keyword Classifier
 ├── Embedding Classifier
 └── Scoring Engine
 |
 ↓
Decision Engine
 |
 ↓
Dashboard Result

##  Tech Stack

### Frontend

- React
- Vite
- Tailwind CSS
- Lucide Icons

### Backend

- FastAPI
- Python

### Machine Learning

- NLP Classification
- Embedding Based Matching
- Rule Based Scoring


##  Run Locally

### Backend

```bash
uvicorn backend.main:app --reload

## FRONTEND

```bash
cd frontend

npm run dev