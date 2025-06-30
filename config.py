# config.py
from chromadb.config import Settings

CHROMA_PATH = "/Volumes/My_AI/my_ai_suite/chroma_db"

chroma_settings = Settings(
    persist_directory=CHROMA_PATH,
    anonymized_telemetry=False,
    is_persistent=True  # ✅ Ensures not ephemeral
)
