from langchain_community.tools import WikipediaQueryRun
from ddgs import DDGS
from langchain_community.utilities import WikipediaAPIWrapper, DuckDuckGoSearchAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Save structured research data to a text file."
)

# ✅ Use DuckDuckGoSearchAPIWrapper (compatible with most versions)
search_api = DuckDuckGoSearchAPIWrapper()
search_tool = Tool(
    name="search",
    func=search_api.run,
    description="Search the web for information. Useful for finding recent or specific data."
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

