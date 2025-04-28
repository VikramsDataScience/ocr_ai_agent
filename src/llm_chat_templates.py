"""USE THE FOLLOWING TEMPLATES TO ALLOW THE LLM TO ACCESS TO THE TOOLKIT IN TOOLS.PY.
ALSO, WHEN NEW TOOLS ARE BUILT IN TOOLS.PY, PLEASE UPDATE THESE TEMPLATES TO REFLECT THE NEW TOOLS.
"""

from .tools import duckduckgo_search_tool, google_search_serpapi, mistral_ocr_tool, read_csv_xlsx

function_definitions = """[
        {
        "name": "google_search_serpapi",
        "description": "Helper function to run Google searches via SerpAPI.",
        "parameters": {
            "type": "dict",
            "required": ["query"],
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to be parsed to the Google search engine."
                },
                "max_results": {
                    "type": "integer",
                    "description": "The maximum number of search results to return."
                },
                "full_page": {
                    "type": "boolean",
                    "description": "Whether to return full page content or not."
                }
            }
        }
    },
    {
        "name": "duckduckgo_search_tool",
        "description": "Helper function to parse search query via _query_ arg, run search using DuckDuckGo and return top results.",
        "parameters": {
            "type": "dict",
            "required": ["query"],
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to be parsed to the DuckDuckGo search engine."
                },
                "max_results": {
                    "type": "integer",
                    "description": "The maximum number of search results to return."
                },
                "full_page": {
                    "type": "boolean",
                    "description": "Whether to return full page content or not."
                }
            }
        }
    },
    {
        "name": "mistral_ocr_tool",
        "description": "Helper function to parse document URL and run OCR using Mistral API.",
        "parameters": {
            "type": "dict",
            "required": ["document_url"],
            "properties": {
                "document_url": {
                    "type": "string",
                    "description": "The URL of the document to be processed. Must be a publicly accessible URL pointing to a PDF document."
                }
            }
        }
    },
]"""

llama_system_prompt = """You are an AI research assistant with access to specific tools to help answer questions.

IMPORTANT: You CANNOT import external libraries like 'requests' or anything else. Attempts to do so will fail.

Instead, use ONLY these available tools:
- call_ocr_tool(document_url="The URL of the document to be processed")
- call_google_search_tool(query="The search query to be parsed to the Google search engine")
- call_ddgs_search_tool(query="The search query to be run") 

When you need to use a tool, your response must follow EXACTLY this format:

Thoughts: [brief explanation of your reasoning]
Code:
```py
# Call the appropriate tool
call_ddgs_search_tool(query="specific search terms")
```<end_code>

DO NOT attempt additional imports of any sort that are not listed above.
DO NOT try to define your own functions.
ONLY use the pre-defined tools listed above. Here's the above list of functions in JSON format that you can invoke:
{functions}
""".format(functions=function_definitions)

prompt = "Please list 3 key insights you are able to glean by conducting a search on the Deepseek R1 technical paper. Additionally, see if you can find the technical paper itself on arxiv. If so, please list the URL of the paper."