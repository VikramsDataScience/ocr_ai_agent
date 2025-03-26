from typing import Dict

from smolagents import CodeAgent, HfApiModel, tool
from smolagents.default_tools import FinalAnswerTool

# Relative imports
from .tools import mistral_ocr_tool, duckduckgo_search_tool
from . import hf_token


# Call the necessary tools
@tool
def call_ocr_tool(document_url: str) -> str:
    """A tool that performs OCR on a document using Mistral's API.

    Args:
        document_url: The URL of the document to be processed. 
        Must be a publicly accessible URL pointing to a PDF document,
        and the user must provide this URL to the agent."""

    return mistral_ocr_tool(document_url)

@tool
def call_ddgs_search_tool(query: str) -> Dict[str, list[dict[str, any]]]:
    """A tool that performs a DuckDuckGo search. Use this tool if you require
    additional information from the web that is not provided by the user. Please
    use this tool sparingly to avoid API limits.
    
    Args:
        query: The search query to be run."""

    return duckduckgo_search_tool(query)


# Define and run the agent
final_answer_tool = FinalAnswerTool()

model = HfApiModel(max_tokens=2096,
                   token=hf_token,
                   temperature=0.5,
                   model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
                   custom_role_conversions=None,
)

agent = CodeAgent(
    model=model,
    tools=[final_answer_tool,
           call_ocr_tool,
           call_ddgs_search_tool],
        max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
)
# agent.run("Please list 3 key insights you are able to glean from the text in the document at this URL: https://arxiv.org/pdf/2501.12948")
agent.run("Perform a summary of the document at this URL: https://arxiv.org/pdf/2501.12948")
