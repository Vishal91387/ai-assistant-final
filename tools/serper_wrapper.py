import os
import requests
from dotenv import load_dotenv
load_dotenv()

class SerperWrapper:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise ValueError("Missing Serper API Key. Set SERPER_API_KEY in .env or pass it to SerperWrapper().")
        self.base_url = "https://google.serper.dev/search"

    def run(self, query: str) -> str:
        headers = {"X-API-KEY": self.api_key, "Content-Type": "application/json"}
        data = {"q": query}
        response = requests.post(self.base_url, headers=headers, json=data)
        response.raise_for_status()
        results = response.json()
        
        if "answerBox" in results and "answer" in results["answerBox"]:
            return results["answerBox"]["answer"]
        elif "organic" in results and results["organic"]:
            return results["organic"][0].get("snippet", "No snippet available.")
        else:
            return "No results found."
