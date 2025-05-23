import openai
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
load_dotenv()

import phi
from phi.playground import Playground, serve_playground_app

phi.api= os.getenv("PHI_API_KEY")

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

app= Playground(agents=[websearch_agent,finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True) #inside () are the py file name and the variable name in line 43