from flask import Blueprint, request, jsonify
from app.services.symbol_extractor import SymbolExtractor
from app.services.data_fetcher import DataFetcher
from app.services.stock_analysis import StockAnalyst
from langchain_groq import ChatGroq

api_blueprint = Blueprint("api", __name__)
llm = ChatGroq(model="llama3-8b-8192")


@api_blueprint.route("/extract-symbol", methods=["POST"])
def extract_symbol():
    data = request.get_json()
    query = data.get("query")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    extractor = SymbolExtractor(llm)
    result = extractor.extract(query)
    return jsonify({"symbol": result})


@api_blueprint.route("/fetch-financials", methods=["POST"])
def fetch_financials():
    data = request.get_json()
    ticker = data.get("ticker")
    if not ticker:
        return jsonify({"error": "Ticker parameter is required"}), 400

    file_path = f"{ticker}.json"
    fetcher = DataFetcher(ticker)
    message = fetcher.save_data(file_path)
    return jsonify({"message": message, "file": file_path})


@api_blueprint.route("/analyze-stock", methods=["POST"])
def analyze_stock():
    data = request.get_json()
    file_path = data.get("file_path")
    query = data.get("query")
    if not file_path or not query:
        return jsonify({"error": "File path and query parameters are required"}), 400

    analyst = StockAnalyst(llm)
    analysis = analyst.analyze(file_path, query)
    return jsonify({"analysis": analysis})
