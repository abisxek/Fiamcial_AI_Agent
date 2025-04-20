# 🧠 Phi Multi-Agent Finance & Web Intelligence System

A multi-agent framework built using the [Phi](https://github.com/phi-tools/phi) ecosystem, designed to perform real-time financial analysis and web searches. The system uses [Groq](https://groq.com/) models, and integrates tools such as YFinance and DuckDuckGo for intelligent querying and data retrieval.

## 🚀 Features

- 🤖 **Multi-Agent Architecture**: Specialized agents for web search and finance insights.
- 📈 **Finance Agent**: Fetches stock prices, analyst recommendations, news, and fundamentals using YFinance.
- 🌐 **Web Search Agent**: Queries the web with DuckDuckGo, always including sources.
- 📊 **Structured Output**: Tables and markdown formatting for clean, user-friendly responses.
- 💬 **Interactive Playground**: Launch and interact with agents via a customizable UI.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/abisxek/Financial_AI_Agent.git
cd Financial_AI_Agent
```

### 2. Create a Conda Virtual Environment (Python 3.12)

Make sure you have Conda installed.

```bash
conda create -n phi-multiagent python=3.12
conda activate phi-multiagent
```

### 3. Install Project Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not provided yet, manually install the following packages:

```bash
pip install phi groq openai yfinance duckduckgo-search python-dotenv
```

### 4. Add a .env File

Create a .env file in the root directory of the project and include your API keys:

```env
PHI_API_KEY=your_phi_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholders with your actual API keys. You can get them from:
- [Phi API Key](https://github.com/phi-tools/phi)
- [Groq API Key](https://groq.com/)

## ▶️ Running the Application

After activating your environment and setting up everything, run the script to launch the playground:

```bash
python playground.py  or   python financial_agent.py
```

This command will launch the Phi Playground with the configured Web and Finance agents, allowing you to interact with them directly through the UI.

## 🧠 Example Query

In the playground, try asking:

```
Summarize analyst recommendations and share the latest news for NVDA
```

The multi-agent system will route the request to the appropriate agent(s) and return structured and sourced results.

## 📁 Project Structure

```
phi-multiagent-framework/
├── .env                   # API keys for PHI and GROQ
├── financial_agent.py    
├── playground.py          # Main Python file to run the playground
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 📌 Requirements Recap

- Python 3.12
- Conda (or virtualenv)
- Phi Framework
- Groq LLM Access
- DuckDuckGo and YFinance tools (via Phi)
- .env file with API keys

## 📬 License

MIT License. Free to use, modify, and distribute.
