from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import pandas as pd
import sqlite3

# Load environment variables from .env
load_dotenv()

from app.nlptosql import nl_to_sql

app = FastAPI(title="NL to SQL API (OpenRouter GPT-OSS-20B)")

# Load CSV once at startup
CSV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "Salary Data.csv")
df = pd.read_csv(CSV_FILE)

# ✅ Create in-memory SQLite DB with thread-safe option
conn = sqlite3.connect(":memory:", check_same_thread=False)
df.to_sql("salary", conn, index=False, if_exists="replace")

# Request body model
class QueryRequest(BaseModel):
    question: str

# Response model
class QueryResponse(BaseModel):
    sql: str
    answer: list | None = None
    error: str | None = None

@app.get("/")
def root():
    return {"message": "Welcome to NL to SQL API using OpenRouter GPT-OSS-20B!"}

@app.post("/query", response_model=QueryResponse)
def query_database(q: QueryRequest):
    try:
        # Step 1: Generate SQL from question
        sql_query = nl_to_sql(q.question)
        
        # Step 2: Execute SQL
        try:
            result_df = pd.read_sql(sql_query, conn)
            # Convert DataFrame to list of dicts for JSON response
            answer = result_df.to_dict(orient="records")
        except Exception as exec_err:
            return QueryResponse(sql=sql_query, answer=None, error=f"SQL execution error: {str(exec_err)}")
        
        return QueryResponse(sql=sql_query, answer=answer, error=None)
    
    except Exception as e:
        return QueryResponse(sql="", answer=None, error=str(e))
