from typing import Dict, Optional
from pathlib import Path

from smolagents import CodeAgent, tool, PromptTemplates
from smolagents.default_tools import FinalAnswerTool
import pandas as pd

# Relative imports
from .tools import mistral_ocr_tool, duckduckgo_search_tool, read_csv_xlsx
from . import qwen_7BQuant
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

@tool
def call_read_csv_xlsx_tool(file_path: Path, sheet_name: Optional[str] = None) -> pd.DataFrame:
    """A tool that reads a CSV or XLSX file from a user provided file path 
    and returns a Pandas DataFrame for analysis, or any task that the user 
    asks the agent to perform on the returned DataFrame.
    
    Args:
        file_path: The path to the CSV or XLSX file to be read.
        sheet_name: If the _file_path_ suffix is an XLSX, the user needs to provide
        name of the sheet to read from the XLSX file."""

    return read_csv_xlsx(file_path, sheet_name)


# Define and run the agent
final_answer_tool = FinalAnswerTool()
model = localTransformersModel(qwen_7BQuant)

prompt = "Please list 3 key insights you are able to glean by conducting a search on the Deepseek R1 technical paper. Additionally, see if you can find the technical paper itself on arxiv. If so, please list the URL of the paper."

agent = CodeAgent(
    model=model,
    # prompt_templates=messages,
    tools=[final_answer_tool,
           call_ocr_tool,
           call_ddgs_search_tool],
        max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name="Research Assistant",
    description="An AI Agent that can search the web, perform OCR on documents, read CSV/XLSX files, and answer questions based on the information it finds.",
)
agent.run(prompt)
# agent.run("Perform a summary of the document at this URL: https://arxiv.org/pdf/2501.12948")
