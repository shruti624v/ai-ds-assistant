# AI Data Science Assistant 🤖

An AI-powered full-stack web application that automatically analyzes uploaded datasets, recommends the most suitable ML model, executes it, and explains the results in plain English.

## 🚀 Features
- Upload any CSV dataset
- AI automatically detects problem type (classification, regression, clustering)
- Recommends and runs the best ML model using scikit-learn
- Explains results in plain English using LLM API
- Interactive charts and visualizations
- Adjusts explanations based on user expertise level

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Frontend | React + Tailwind CSS |
| Backend | Django + Django REST Framework |
| AI/LLM | Claude API (Anthropic) |
| ML | scikit-learn, pandas, numpy |
| Visualization | matplotlib, seaborn |
| Database | SQLite |

## ⚙️ Setup Instructions

### Backend
```bash
conda create -n ai-ds-assistant python=3.11
conda activate ai-ds-assistant
pip install -r requirements.txt
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 📊 How It Works
1. User uploads a CSV file
2. Django parses it using pandas
3. Dataset summary sent to Claude LLM API
4. LLM recommends the best ML model
5. scikit-learn runs the model
6. Results and charts displayed on React frontend
7. LLM explains output in plain English

## 📌 Status
🔨 Currently under active development
