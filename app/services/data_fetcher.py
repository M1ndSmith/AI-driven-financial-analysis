import yfinance as yf
import json


class DataFetcher:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

    def fetch_data(self):
        return {
            "financials": self.ticker.financials.T.to_json(),
            "balance_sheet": self.ticker.balance_sheet.T.to_json(),
            "cashflow": self.ticker.cashflow.T.to_json(),
        }

    def save_data(self, file_path):
        data = self.fetch_data()
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return f"Financial data successfully saved at {file_path}"
