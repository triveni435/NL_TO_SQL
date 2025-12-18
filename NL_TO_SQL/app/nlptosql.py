import os
import requests

# Load OpenRouter API key from environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OpenRouter API key not found. Set OPENROUTER_API_KEY in your .env file.")

# Model name on OpenRouter
MODEL_NAME = "gpt-oss-20b"

TABLE_SCHEMA = "salary(Age, Gender, Education_Level, Job_Title, Years_of_Experience, Salary)"

def nl_to_sql(question: str, table_schema: str = TABLE_SCHEMA) -> str:
    """
    Convert natural language question to SQL using GPT-OSS-20B via OpenRouter API.
    """
    prompt = f"""
You are an expert SQL generator. Convert the following English question to SQL.
Table schema: {table_schema}
Question: {question}
Only provide the SQL query.
"""
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL_NAME,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0
            }
        )
        response.raise_for_status()
        data = response.json()
        sql_query = data["choices"][0]["message"]["content"].strip()
        return sql_query
    except requests.exceptions.HTTPError as e:
        return f"HTTP error: {str(e)}"
    except Exception as e:
        return f"Error generating SQL: {str(e)}"
