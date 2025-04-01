import time
import random
import httpx
from markdownify import markdownify
from typing import Optional, Dict

from mistralai import Mistral
from duckduckgo_search import DDGS

# Relative imports
from . import mistral_api_key

def fetch_full_page(url: str) -> Optional[str]:
    """Helper function to fetch full page content from a URL."""
    
    try:
        with httpx.Client() as client:
            response = client.get(url)
            response.raise_for_status()
            return markdownify(response.text)
        
    except Exception as e:
        print(f"Error fetching page content for URL: {e}")
        return None


def duckduckgo_search_tool(query: str, max_results: int = 3, full_page: bool = True) -> Dict[str, list[dict[str, any]]]:
    """
    Helper function to parse search query via _query_ arg, 
    run search using DuckDuckGo and return top 3 results.
    N.B. PLEASE USE SPARINGLY TO AVOID API LIMITS!
    
    Args:
        query: The search query to be processed.
        max_results: The maximum number of search results to return.
        full_page: Whether to return full page content or not. If True, it will use 
        the fetch_full_page() helper function."""

    try:
        ddgs = DDGS(headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        results = []
        search_results = list(ddgs.text(keywords=query,
                        max_results=max_results))
        
        for r in search_results:
            url = r.get("href")
            title = r.get("title")
            search_content = r.get("body")
            
            # If full_page is True, fetch full page content using the fetch_full_page() helper function
            if full_page:
                full_page_content = fetch_full_page(url)

            # Append search results to list
            result = {
                "title": title,
                "url": url,
                "search_content": search_content,
                "full_page_content": full_page_content
            }
            results.append(result)

            return {"results": results}

    except Exception as e:
        print(f"DuckDuckGo API limit reached. Attempting randomized delay: {e}. \nRetrying after a delay...")
        time.sleep(random.uniform(10, 30))  # Randomized backoff to avoid detection
        print(f"Full error stack trace: {type(e).__name__}")

    return results


def mistral_ocr_tool(document_url: str) -> str:
    """ 
    Helper function to parse document URL via _document_url_ arg, 
    and run OCR using Mistral API.
    
    Args:
        document_url: The URL of the document to be processed. 
        Must be a publicly accessible URL pointing to a PDF document."""
    
    if not mistral_api_key:
        raise ValueError("Mistral API key not found. Please provide a valid Mistral API key.")
    
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

    return extracted_text