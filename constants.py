from dotenv import load_dotenv
import os

load_dotenv()

SERVER_URL = os.getenv("SERVER_URL", "localhost")
PORT = int(os.getenv("PORT", 8000))
ENV = os.getenv("ENV", "dev")

RELOAD = bool(ENV == "dev")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.0-flash"
