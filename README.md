# AI Research Agent

A production-grade Multi-Agentic AI Research Assistant built using LangGraph, LangChain, Groq LLMs, and Streamlit.

This project demonstrates how modern Agentic AI systems can perform intelligent web-based research, analyze information, orchestrate workflows, and generate detailed research-oriented responses using modular AI architecture.

---

# Features

* AI-powered Research Assistant
* Multi-Agentic AI Architecture
* Intelligent Web Search Integration
* LangGraph Workflow Orchestration
* Modular Project Structure
* Streamlit Interactive UI
* Production-Style Codebase
* Docker Support
* Groq LLM Integration
* Real-Time Research Responses
* Professional AI Engineering Practices

---

# Tech Stack

| Technology    | Usage                     |
| ------------- | ------------------------- |
| Python        | Core Programming Language |
| LangChain     | LLM Framework             |
| LangGraph     | Workflow Orchestration    |
| Groq LLM      | Fast AI Inference         |
| Streamlit     | Frontend UI               |
| Tavily Search | Web Search Tool           |
| Docker        | Containerization          |

---

# Project Architecture

```bash
User Query
    ↓
Research Agent
    ↓
Web Search Tool
    ↓
LangGraph Workflow
    ↓
Groq LLM Processing
    ↓
Final Research Response
```

---

# Project Structure

```bash
ai-research-agent/
│
├── app/
│   │
│   ├── agent/
│   │   └── research_agent.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── core/
│   │   └── llm.py
│   │
│   ├── prompts/
│   │   └── research_prompt.py
│   │
│   ├── tools/
│   │   └── web_search.py
│   │
│   ├── workflow/
│   │   └── graph.py
│   │
│   └── utils/
│       └── logger.py
│
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── .env
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd ai-research-agent
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# Running The Application

```bash
streamlit run streamlit_app.py
```

The application will start on:

```bash
http://localhost:8501
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t ai-research-agent .
```

---

## Run Docker Container

```bash
docker run -p 8501:8501 ai-research-agent
```

---

# Example Queries

```text
Future of Agentic AI
```

```text
Latest trends in AI Engineering
```

```text
Compare LangChain vs LangGraph
```

```text
What is Multi-Agentic AI?
```

---

# Key Concepts Demonstrated

* Agentic AI Systems
* Multi-Agent AI Architecture
* Tool Calling
* Workflow Orchestration
* AI Research Automation
* LLM Integration
* Modular Software Engineering
* Production-Level Project Structuring

---

# Why This Project Matters

This project demonstrates real-world AI Engineering concepts used in modern AI applications.

It showcases:

* AI workflow orchestration
* Agentic reasoning
* scalable project architecture
* intelligent tool usage
* production-ready coding practices

This project is highly suitable for:

* AI Engineer Roles
* GenAI Engineer Roles
* LLM Application Developer Roles
* AI Research Engineering Roles
---

---

# Resume Description

Built a production-grade Multi-Agentic AI Research Assistant using LangGraph, LangChain, Groq LLMs, and Streamlit. Implemented intelligent web search integration, workflow orchestration, modular architecture, and AI-powered research automation using modern Agentic AI engineering practices.

---

# Skills Demonstrated

* Python
* LangChain
* LangGraph
* Agentic AI
* LLM Engineering
* Prompt Engineering
* Streamlit
* Docker
* AI Workflow Design
* Software Architecture

---

# License

This project is licensed under the MIT License.

---

# Author

Sahil Soni

