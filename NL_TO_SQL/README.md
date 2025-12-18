NL_TO_SQL

# 📝 NL to SQL Project

This project converts **natural language questions (English)** into **SQL queries** and fetches results from a **customer dataset** using **FastAPI** + **OpenRouter API (OpenAI gpt-oss-20b model)**.

---

## 📌 Features

* ✅ Ask questions in plain English
* ✅ Automatically generate SQL queries using **OpenRouter’s OpenAI gpt-oss-20b** model
* ✅ Execute queries on a **SQLite database**
* ✅ View results in **Swagger UI** (`/docs`)
* ✅ Free to use (through OpenRouter’s free tier)

---

## 📂 Project Structure

```
nl_to_sql_app/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── db.py            # Database setup & CSV loader
│   ├── nlp_to_sql.py    # NL → SQL conversion via OpenRouter API
│   └── models.py        # Pydantic request models
│
├── data/
│   └── customer_data.csv # Sample dataset
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/nl_to_sql_app.git
cd nl_to_sql_app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```
OPENROUTER_API_KEY=your_api_key_here
```

Get your free API key from 👉 [https://openrouter.ai](https://openrouter.ai)

### 4. Load dataset into SQLite

Open a Python shell and run:

```python
from app.db import load_data
load_data('data/customer_data.csv')
```

This will create a **customer.db** SQLite database with a `customers` table.

---

## 🚀 Run the FastAPI App

```bash
uvicorn app.main:app --reload --port 8084
```


Open your browser: 👉 [http://127.0.0.1:8084/docs](http://127.0.0.1:8084/docs)

You’ll see an interactive Swagger UI to test queries.

---

## 🧪 Example Queries

**Input (English question):**

```
Show all customers from India with purchase_amount greater than 500
```

**Generated SQL (via gpt-oss-20b):**

```sql
SELECT * FROM customers WHERE country = 'India' AND purchase_amount > 500;
```

**Output (JSON):**

```json
[
  {
    "customer_id": 1,
    "name": "John",
    "email": "john@example.com",
    "city": "Delhi",
    "country": "India",
    "purchase_amount": 600
  }
]
```

---

## 📊 Dataset Schema

**Table: `customers`**

| Column           | Type  | Description                |
| ---------------- | ----- | -------------------------- |
| customer\_id     | INT   | Unique customer ID         |
| name             | TEXT  | Customer name              |
| email            | TEXT  | Customer email             |
| city             | TEXT  | Customer’s city            |
| country          | TEXT  | Customer’s country         |
| purchase\_amount | FLOAT | Purchase amount in dollars |

---

## 🔧 Tech Stack

* **[FastAPI](https://fastapi.tiangolo.com/)** – Web framework
* **[SQLite](https://www.sqlite.org/)** – Lightweight database
* **[OpenRouter API](https://openrouter.ai/)** – Unified API to access models
* **OpenAI gpt-oss-20b** – Text-to-SQL model (free)
* **Pandas + SQLAlchemy** – Data handling

---

## ⚠️ Notes

* You must set your `OPENROUTER_API_KEY` in `.env`.
* The **gpt-oss-20b** model may sometimes generate invalid SQL → you should validate queries before execution.
* For large datasets, consider upgrading from **SQLite → PostgreSQL/MySQL**.

---

## 📌 Future Improvements

* Add **SQL validation & sanitization** before execution
* Support for **joins, group by, and aggregations**
* Add a **frontend UI (Streamlit/React)**
* Option to switch between **OpenRouter** and **Hugging Face/OpenAI GPT models**


