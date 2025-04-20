from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import openai
from dotenv import load_dotenv
load_dotenv()
#openai.api_key= os.getenv("OPENAI_API_KEY")

websearch_agent= Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model= Groq(
        id="llama-3.1-8b-instant"
    ),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown= True,

)

finance_agent= Agent(
    name="Finance AI Agent",
    model= Groq(
        id="llama-3.1-8b-instant"
    ),
    tools=[YFinanceTools(stock_price= True, analyst_recommendations= True, stock_fundamentals=True, company_news=True)],
    instructions=["Use table to display data"],
    show_tool_calls=True,
    markdown= True
)

multi_ai_agent=Agent(
    team=[websearch_agent,finance_agent],
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)