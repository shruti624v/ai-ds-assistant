import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_model_recommendation(dataset_summary):
    prompt = f"""
You are an expert data scientist. Analyze this dataset summary and recommend the best ML model.

Dataset Summary:
{dataset_summary}

Reply in this exact format:
PROBLEM TYPE: (classification/regression/clustering)
RECOMMENDED MODEL: (model name)
REASON: (one line explanation)
TARGET COLUMN: (most likely target column name)
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content