"""USE THE FOLLOWING WITH LLAMA MODELS ONLY TO ALLOW THE LLM TO ACCESS TO THE TOOLKIT IN TOOLS.PY.
ALSO, WHEN NEW TOOLS ARE BUILT IN TOOLS.PY, PLEASE UPDATE THESE TEMPLATES TO REFLECT THE NEW TOOLS.
FOR REFERENCE: https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_2/#-tool-calling
"""

function_definitions = """[
    {
        "name": "duckduckgo_search_tool",
        "description": "Helper function to parse search query via _query_ arg, run search using DuckDuckGo and return top 3 results. N.B. PLEASE USE SPARINGLY TO AVOID API LIMITS!",
        "parameters": {
            "type": "dict",
            "required": [
                "query",
                "max_results",
                "full_page"
            ],
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to be parsed to the DuckDuckGo search engine.",
                "max_results":
                    "type": "integer",
                    "description": "The maximum number of search results to return.",
                "full_page":
                    "type": "boolean",
                    "description": "Whether to return full page content or not. If True, it will use the fetch_full_page() helper function."
                },
            "special": {
                "type": "string",
                "description": "Any special information or parameters that need to be considered while searching the web.",
                "default": "none"
                }
            }
        }
    }
]
"""

system_prompt = """You are an expert in composing functions. You are given a question and a set of possible functions. 
Based on the question, you will need to make one or more function/tool calls to achieve the purpose. The function/tool 
calls can be found in the src.tools module. The required functions have been imported into this module. If none of the 
function can be used, point it out. If the given question lacks the parameters required by the function, also point it 
out. You should only return the function call in tools call sections.

If you decide to invoke any of the function(s), you MUST put it in the format of [func_name1(params_name1=params_value1, params_name2=params_value2...), func_name2(params)]\n
You SHOULD NOT include any other text in the response.

Here is a list of functions in JSON format that you can invoke.\n\n{functions}\n""".format(functions=function_definitions)
