# Flask Financial Analysis API

## 📌 Project Overview

This is a **Flask-based Financial Analysis API** that allows users to:

- Extract stock ticker symbols from natural language queries.
- Fetch financial data for a stock using Yahoo Finance.
- Analyze stock data using AI-driven financial analysis.

## 🏗 Project Structure

```
/flask_financial_api
│── /app
│   │── /api
│   │   │── __init__.py
│   │   │── routes.py
│   │── /models
│   │   │── __init__.py
│   │   │── stock.py
│   │── /services
│   │   │── __init__.py
│   │   │── symbol_extractor.py
│   │   │── data_fetcher.py
│   │   │── stock_analysis.py
│   │── /utils
│   │   │── __init__.py
│   │   │── logger.py
│   │── /config
│   │   │── __init__.py
│   │   │── settings.py
│   │── /middleware
│   │   │── __init__.py
│   │   │── error_handler.py
│   │── __init__.py
│   │── extensions.py
│── /migrations
│── /tests
│   │── __init__.py
│   │── test_routes.py
│── /instance
│── .env
│── requirements.txt
│── gunicorn_config.py
│── wsgi.py
│── README.md
```

## 🚀 Getting Started

### 🔹 Prerequisites

- Python 3.12+
- Anaconda (if using Conda environments)

### 🔹 Setup

#### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/flask_financial_api.git
cd flask_financial_api
```

#### 2. Create a Virtual Environment

```sh
conda create -n financial_api_env python=3.12
conda activate financial_api_env
```

Or using `venv`:

```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

#### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

#### 4. Set Up Database

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

#### 5. Run the Server

```sh
flask run
```

By default, the API runs at: `http://127.0.0.1:5000`

For public access:

```sh
flask run --host=0.0.0.0 --port=5000
```

## 📡 API Endpoints

### 1️⃣ Extract Stock Symbol

**POST** `/api/extract-symbol`

#### Request:

```json
{
    "query": "symbol for microsoft"
}
```

#### Response:

```json
{
  "symbol":"The stock ticker symbol for Microsoft is:\n\nMSFT"
}
```

### 2️⃣ Fetch Financial Data

**POST** `/api/fetch-financials`

#### Request:

```json
{
    "ticker": "AAPL"
}
```

#### Response:

```json
{
 "file":"MSFT.json",
  "message":"Financial data successfully saved at MSFT.json"   
}
```

### 3️⃣ Analyze Stock Data

**POST** `/api/analyze-stock`

#### Request:

```json
{
    "file_path": "AAPL.json",
    "query": "Analyze this stock"
}
```

#### Response:

```json
{
    "analysis": """
  The stock shows strong profitability...
 .... I would recommend that the trader hold the stock.
  """
}
```

## 🧪 Running Tests

```sh
pytest tests/
```

Expected output:

```plaintext
================================================= 3 passed in 13.74s ==================================================
```

## 🚀 Deployment

### 1️⃣ Deploy with Waitress (Windows Production Server)
### ! you can use gunicorn for linux


```sh
pip install waitress
waitress-serve --listen=0.0.0.0:5000 wsgi:app
```
  |

## 📌 License

This project is open-source and available under the **MIT License**.

## ❤️ Contributing

- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Commit your changes (`git commit -m 'Add new feature'`)
- Push to the branch (`git push origin feature-branch`)
- Create a pull request 🚀

