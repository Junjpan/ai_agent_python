# file: research_agent.py
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent

load_dotenv()

#https://docs.langchain.com/oss/python/langchain/agents

# Define structured output
class ResearchResponse(BaseModel):
    topic: str=Field(description="The research topic")
    summary: str=Field(description="A concise summary of the research findings")
    sources: list[str]=Field(description="A list of sources referenced in the research")
    tools_used: list[str]=Field(description="A list of tools used during the research process")

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
    {"role": "user", "content": "compared langgraph and n8n, which one is better for building LLM applications? Provide a structured simple research report."}
]}

# # Create agent (no custom prompt templates allowed in v1), to get the structured output you need to pass the resposne_format
agent = create_agent(
    model=llm,
    tools=[],              # no tools for now
    system_prompt=system_text,
    response_format=ResearchResponse
)

# # Invoke agent
rawResult = agent.invoke(messages)
# print("Raw LLM output:")
# print(rawResult)

# # Parse LLM output properly to get structured response
structured = rawResult["structured_response"]
p
print("\nStructured response:")
print(structured)



# todo:
# 1. update the langchain-anthropic to the latest version if you haven't already. and use update to dated syntax
# refer to this doc:https://docs.langchain.com/oss/python/integrations/chat/anthropic#structured-output