from smolagents import CodeAgent, HfApiModel, tool
from smolagents.default_tools import FinalAnswerTool

import gradio as gr

# Relative imports
from .tools import mistral_ocr_tool

@tool
def call_ocr_tool(document_url: str) -> str:
    """A tool that performs OCR on a document using Mistral's API.

    Args:
        document_url: The URL of the document to be processed. 
        Must be a publicly accessible URL pointing to a PDF document,
        and the user must provide this URL to the agent."""

    return mistral_ocr_tool(document_url)


# Define the agent
final_answer_tool = FinalAnswerTool()
# model = HfApiModel(
#     model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
model = HfApiModel(max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
    custom_role_conversions=None,
)

agent = CodeAgent(
    model=model,
    tools=[final_answer_tool,
           call_ocr_tool],
        max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
)
agent.run("Perform a summary of the document at this URL: https://arxiv.org/pdf/2501.12948")
