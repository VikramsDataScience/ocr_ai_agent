from pathlib import Path
from dotenv import load_dotenv
import os

# Allow expandable segments in CUDA memory to prevent OOM errors
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

class FilePaths:
    def __init__(self):
        self.api_keys = "C:/ocr_ai_agent/api_keys.env"
        self.data_path = "C:/ocr_ai_agent/data/"

# Model version
__version__ = "0.01"

# Load storage paths from FilePaths class
file_paths = FilePaths()
api_keys_path = Path(file_paths.api_keys)
data_path = Path(file_paths.data_path)

# Load environment file containing API keys and access tokens
load_dotenv(api_keys_path)
mistral_api_key = os.getenv("MISTRAL_API_KEY")
hf_token = os.getenv("HF_TOKEN")
langfuse_public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
langfuse_secret_key = os.getenv("LANGFUSE_SECRET_KEY")
langfust_host = os.getenv("LANGFUSE_HOST")

# Define LLMs to use
qwen_32B = "Qwen/Qwen2.5-Coder-32B-Instruct"
llama_3B = "meta-llama/Llama-3.2-3B-Instruct"
llama_1B = "meta-llama/Llama-3.2-1B-Instruct"
