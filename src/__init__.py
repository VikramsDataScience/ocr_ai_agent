from pathlib import Path
from dotenv import load_dotenv
import os

# Relative imports
from .config import FilePaths

# Model version
__version__ = "0.01"

# Load storage paths from config.py
file_paths = FilePaths()
api_keys_path = Path(file_paths.api_keys)
data_path = Path(file_paths.data_path)

# Load environment file containing API keys, and grab the Mistral API key
load_dotenv(api_keys_path)
mistral_api_key = os.getenv("MISTRAL_API_KEY")
hf_token = os.getenv("HF_TOKEN")