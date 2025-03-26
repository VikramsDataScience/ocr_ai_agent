## Optical Character Recognition (OCR) & Research AI Agent (POC Complete)

This project has been a more hastily developed AI Agent (POC developed in about 2 weeks, including the research phase) that has the following approach to development & capabilities:
- The agent has access to two tools from the `tools.py` module. One is a search capability using DuckDuckGo's search (DDGS) library. However, this API is extremely restrictive, and blocks users after running only a few searches. Whilst I've developed the implementation for it in the `search_tool()` function, the limited usage made me think to keep it out of the hands of the AI agent, as an available tool.
- The tool that's currently available to the agent (though I might add more, depending on the direction this project takes, or I'll develop more complexity into the next agent) is the OCR tool offered by Mistral AI. I've managed to get a free tier access to their API that's been pretty generous, so far. For the agent to access this tool only requires the URL of any PDF file. This will need to be provided by the user in the prompt to the agent.
- In terms of the LLM, we're currently using `Qwen2.5-Coder-32B-Instruct` model, due to its ease of use, and performant capability.
- In terms of the agentic implementation, we're using Hugging Face's `smolagents` library, where the aforementioned LLM is hosted by Hugging Face. An HF account and user token is needed to gain access to the LLM, and to also run the agent itself.
- To run the agent in the CLI, please run `python -m src.agent`
- So far, in terms of capability, the agent is able to provide:<br>
&nbsp; &nbsp; &nbsp; --> Insights on any provided PDF link if prompted by the user. The example below provides 3 key insights from the DeepSeek R1 technical paper when provided the link to the arXiv paper:
![image](https://github.com/user-attachments/assets/b5633ce7-2775-4ef0-bae4-0d12522c3b75) <br>
&nbsp; &nbsp; &nbsp; --> Summaries of provided PDF links. Again, using the DeepSeek R1 paper as an example, the agent gives the following:
![image](https://github.com/user-attachments/assets/41330214-a280-443b-a918-449faae013a8) <br>
The above is based on a more basic agent with only 1 tool in its toolkit (Mistral's OCR tool). But, even with just the one tool, it can provide quite reasonable responses with minimal prompting from the user.
- To extend from the above, I've now built a new tool that gives the agent a Research capability that's enabled using DuckDuckGo's search API. With the prompt (i.e. not providing the exact URL like above): "Please list 3 key insights you are able to glean by conducting a search on the Deepseek R1 technical paper. Additionally, see if you can find the technical paper itself on arxiv. If so, please list the URL of the paper.":<br>
![image](https://github.com/user-attachments/assets/b64bcbc3-7811-4df8-a0d2-26a46fa17c8f)
&nbsp; &nbsp; &nbsp; --> We can see that's it only used the search tool (since no PDF URLs were given), and it was able to perform a search and correctly find the DeepSeek R1 URL on arXiv!
