import os
import time
import random
from dotenv import load_dotenv

from mistralai import Mistral
from duckduckgo_search import DDGS

# Relative imports
from . import api_keys_path, ocr_output_path

# Load environment file containing API keys, and grab the Mistral API key
load_dotenv(api_keys_path)
mistral_api_key = os.getenv("MISTRAL_API_KEY", "")

# Define the tools
def search_tool(query: str) -> list[dict]:
    """
    Parse search query via _query_ arg, run search using 
    DuckDuckGo and return top 5 results.
    N.B. PLEASE USE SPARINGLY TO AVOID API LIMITS!"""

    try:
        ddgs = DDGS(headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        results = ddgs.text(keywords=query,
                        region="wt-wt",
                        safesearch="moderate",
                        timelimit="y",
                        max_results=5)
    except Exception as e:
        print(f"DuckDuckGo API limit reached. Attempting randomized delay: {e}. \nRetrying after a delay...")
        time.sleep(random.uniform(10, 30))  # Randomized backoff to avoid detection
    
    # Only use print() for debugging. REMOVE FOR PRODUCTION
    print(results)

    return results


def ocr_tool(document_url: str) -> str:
    """Parse document URL via _document_url_ arg, and run OCR using Mistral API."""
    
    client = Mistral(api_key=mistral_api_key)
    
    pdf_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": document_url,
    },
    include_image_base64=True
    )
    
    # Perform markdown on the extracted text
    extracted_text = "\n\n".join(page.markdown for page in pdf_response.pages)
    print(extracted_text)

    return extracted_text
