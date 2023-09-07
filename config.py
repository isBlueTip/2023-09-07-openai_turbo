import os
from dotenv import load_dotenv

load_dotenv()

GPT_35_TURBO_API_KEY = os.getenv("GPT_3.5_TURBO_API_KEY", "default key")
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "default key")
