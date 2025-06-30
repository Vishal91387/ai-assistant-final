from dotenv import load_dotenv
from langchain_community.tools import Tool
from tools.serper_wrapper import SerperWrapper

load_dotenv()
search = SerperWrapper()

serper_tool = Tool.from_function(
    func=search.run,
    name="Web Search",
    description="Useful for searching the web using Serper.dev"
)

