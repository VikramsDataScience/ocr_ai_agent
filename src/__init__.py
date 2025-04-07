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
qwen_1halfB = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
qwen_7BQuant = "Qwen/Qwen2.5-Coder-7B-Instruct-GPTQ-Int4"
qwen_1half5BQuant = "Qwen/Qwen2.5-Coder-1.5B-Instruct-AWQ"

######### PROMPT TEMPLATES #########
# If required, call the following prompt templates ('system_prompt' arg) using the PromptTemplates() class from smolagents
phi_4_3point8B = "microsoft/Phi-4-mini-instruct"
phi_4_3point8B_prompt_template = """
<|system|>You are a helpful assistant with some tools.
<|tool|>[{"name": "call_ocr_tool", 
"description": "A tool that performs OCR on a document using Mistral's API.", 
"parameters": {"document_url": 
{"description": "The URL of the document to be processed. 
        Must be a publicly accessible URL pointing to a PDF document,
        and the user must provide this URL to the agent.", 
"type": "str"}}},
{"name": "call_ddgs_search_tool",
"description": "A tool that performs a DuckDuckGo search. Use this tool if you require
    additional information from the web that is not provided by the user. Please
    use this tool sparingly to avoid API limits.",
"parameters": {"query":
{"description": "The search query to be run.",
"type": "str"}}}
]
<|/tool|><|end|>
<|user|>{prompt}<|end|><|assistant|>"""