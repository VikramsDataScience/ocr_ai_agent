import time
import random

from mistralai import Mistral
from duckduckgo_search import DDGS

# Relative imports
from . import mistral_api_key

# Define the tools
def search_tool(query: str) -> list[dict]:
    """
    Helper function to parse search query via _query_ arg, 
    run search using DuckDuckGo and return top 5 results.
    N.B. PLEASE USE SPARINGLY TO AVOID API LIMITS!
    
    Args:
        query: The search query to be processed."""

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


def mistral_ocr_tool(document_url: str) -> str:
    """ 
    Helper function to parse document URL via _document_url_ arg, 
    and run OCR using Mistral API.
    
    Args:
        document_url: The URL of the document to be processed. 
        Must be a publicly accessible URL pointing to a PDF document."""
    
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
