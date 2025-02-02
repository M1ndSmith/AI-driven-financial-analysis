import json


class StockAnalyst:
    def __init__(self, llm):
        self.llm = llm

    def analyze(self, file_path, query):
        with open(file_path, "r") as file:
            financial_data = json.load(file)

        # Convert JSON to string in parts (avoid exceeding token limits)
        sections = ["financials", "balance_sheet", "cashflow"]
        analysis_results = {}

        for section in sections:
            if section in financial_data:
                data_part = json.dumps(financial_data[section])[
                    :5000
                ]  # Limit data size per request
                prompt = f"""
                You are a financial stock analyst. Analyze the following financial section:
                {data_part}
                Based on this, provide insights on {section}.
                By the end provide a justified recommendation for trading based on your                   analysis, should the trader hold, buy or sell the stock
                """
                output = self.llm.invoke(prompt)
                analysis_results[section] = output.content

        # Combine all results into a final report
        return json.dumps(analysis_results, indent=4)
