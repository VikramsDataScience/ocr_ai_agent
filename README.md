## Optical Character Recognition (OCR) AI Agent (POC Complete)

This project has been a more hastily developed AI Agent (POC developed in about 2 weeks, including the research phase) that has the following approach to development & capabilities:
- The agent has access to two tools from the `tools.py` module. One is a search capability using DuckDuckGo's search (DDGS) library. However, this API is extremely restrictive. So, whilst I've developed the implementation for it in the `search_tool()` function, I've kept it out of the hands of the AI agent, as an available tool.
- The tool that's currently available to the agent (though I might add more, depending on the direction this project takes) is the OCR tool offered by Mistral AI. I've managed to get a free tier access to their API that's been pretty generous, so far. For the agent to access this tool only requires the URL of any PDF file. This will need to be provided by the user in the prompt to the agent.
- In terms of the LLM, we're currently using `Qwen2.5-Coder-32B-Instruct` model, due to its ease of use, and performant capability.
- In terms of the agentic implementation, we're using Hugging Face's `smolagents` library, where the aorementioned LLM is hosted by Hugging Face. An HF account and user token is needed to gain access to the LLM, and to also run the agent itself.
- To run the agent in the CLI, please run `python -m src.agent`
- So far, in terms of capability, the agent is able to provide:<br>
&nbsp; &nbsp; &nbsp; --> Insights on any provided PDF link if prompted by the user. The example below provides 3 key insights from the DeepSeek R1 technical paper when provided the link to the arXiv paper:
![image](https://github.com/user-attachments/assets/b5633ce7-2775-4ef0-bae4-0d12522c3b75) <br>
&nbsp; &nbsp; &nbsp; --> Summaries of provided PDF links. Again, using the DeepSeek R1 paper as an example, the agent gives the following:
![image](https://github.com/user-attachments/assets/41330214-a280-443b-a918-449faae013a8) <br>
This agent is quite basic. But we can see that even with only 1 tool in its toolkit it can provide quite reasonable responses with minimal prompting from the user. I'll be looking to improve upon this effort with my next project, as I'll attempt to build a more sophisticated agent :).
