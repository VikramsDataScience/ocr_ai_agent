from typing import Dict

from smolagents import CodeAgent, tool
from smolagents.default_tools import FinalAnswerTool

# Relative imports
from .tools import mistral_ocr_tool, duckduckgo_search_tool
from . import llama_1B
from .hf_functions import localTransformersModel


# Call the available tools
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

model = localTransformersModel(llama_1B)

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
agent.run("Please list 3 key insights you are able to glean by conducting a search on the Deepseek R1 technical paper. Additionally, see if you can find the technical paper itself on arxiv. If so, please list the URL of the paper.")
# agent.run("Perform a summary of the document at this URL: https://arxiv.org/pdf/2501.12948")
