from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

search=DuckDuckGoSearchRun()
search_tool=Tool(
    name="search_internet", # note: name must not have spaces
    func=search.run,
    description="look up current information on the internet.") # we need to specify the description for the agent to know when to use this tool

api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=1000)
wiki_tool=WikipediaQueryRun(api_wrapper=api_wrapper)

def save_to_file(data: str, filename: str = 'research_output.txt') :
    """Saves Research content to a file"""
    timeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"=== Research Output ===\nTimestamp: {timeStamp}\n\n{data}\n\n=== End of Research Output ===\n\n"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Data successfully saved to {filename}"

save_tool=Tool(
    name="save_research",
    func=save_to_file,
    description="Saves research content to a file."
)