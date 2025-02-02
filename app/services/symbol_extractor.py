from langchain_groq import ChatGroq


class SymbolExtractor:
    def __init__(self, llm):
        self.llm = llm

    def extract(self, query):
        role = "act as a stock ticker symbol extractor"
        output = self.llm.invoke(f"{role}: {query}")
        return output.content
