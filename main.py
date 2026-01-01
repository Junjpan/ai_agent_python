# file: research_agent.py
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import search_tool,wiki_tool,save_tool

load_dotenv()

#https://docs.langchain.com/oss/python/langchain/agents

# Define structured output
class ResearchResponse(BaseModel):
    topic: str=Field(description="The research topic")
    summary: str=Field(description="A concise summary of the research findings")
    sources: list[str]=Field(description="A list of sources referenced in the research")
    tools_used: list[str]=Field(description="A list of tools used during the research process")

query=input(" What topic would you like to research? ")

# LLM Model, it automatically picks up the ANTHROPIC_API_KEY from environment variables
llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    temperature=0,
    max_tokens=1024
)


parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_text = f"""
You are a research assistant that generates structured research reports.
"""

messages={"messages":[
    {"role": "user", "content": query}
]}

tools = [search_tool,wiki_tool,save_tool]

# # Create agent (no custom prompt templates allowed in v1), to get the structured output you need to pass the resposne_format
agent = create_agent(
    model=llm,
    tools=tools,              # no tools for now
    system_prompt=system_text,
    response_format=ResearchResponse
)

# # Invoke agent
rawResult = agent.invoke(messages)
# print("Raw LLM output:")
# print(rawResult)

# # Parse LLM output properly to get structured response // when no tool is used

# try:
#     structured = parser.parse(rawResult["output"])
#     print("\nStructured response:")
#     print(structured)
# except Exception as e:
#     print("Error parsing output:", e, "\nRaw output was:", rawResult)

# Directly access structured response when tools are used

structured_response = rawResult.get('structured_response')

if structured_response:
    print("\n=== Research Summary ===")
    print(f"Topic: {structured_response.topic}")
    print(f"\nSummary:\n{structured_response.summary}")
    print(f"\nSources: {', '.join(structured_response.sources)}")
    print(f"Tools Used: {', '.join(structured_response.tools_used)}")
else:
    print("No structured response found")



# todo:
# 1. update the langchain-anthropic to the latest version if you haven't already. and use update to dated syntax
# refer to this doc:https://docs.langchain.com/oss/python/integrations/chat/anthropic#structured-output