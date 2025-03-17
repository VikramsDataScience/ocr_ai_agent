from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool, load_tool, tool
from smolagents.default_tools import FinalAnswerTool

# Relative imports
from .tools import ocr_tool




# Define the agent
# final_answer_tool = FinalAnswerTool()
# model = HfApiModel(
#     model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")



# search_tool("What is the capital of France?")
# ocr_tool("https://arxiv.org/pdf/2501.12948")