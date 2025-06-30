from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.llms import Ollama


wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())