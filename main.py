from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool
from ddgs import DDGS
import os


load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    detailed_summary: str
    sources: list[str]
    tools_used: list[str]




#llm = ChatOpenAI(model="gpt-4o")
llm = ChatOpenAI(model="llama3-70b-8192",openai_api_base="https://api.groq.com/openai/v1",api_key=os.getenv("GROQ_API_KEY"))
parser= PydanticOutputParser(pydantic_object=ResearchResponse)



# Escape curly braces inside the JSON schema
escaped_format = parser.get_format_instructions().replace("{", "{{").replace("}", "}}")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            Provide a **detailed and informative explanation**, not just one line.
            Wrap the output in this format and provide no other text:\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())




tools= [wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm= llm,
    prompt=prompt,
    tools=tools

)


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("What can i help you research?: ")
raw_response = agent_executor.invoke({"query": query})

try:
    structed_response = parser.parse(raw_response.get("output"))
    print("Structured Response:", structed_response)
except Exception as e:
    print("Error parsing response:", e, "Raw Response - ", raw_response)

