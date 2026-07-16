# ResearchMind 🔬 - Multi-Agent AI Research Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![LangChain](https://img.shields.io/badge/LangChain-Integration-32a852.svg)

**ResearchMind** is an advanced, autonomous Multi-Agent Artificial Intelligence system designed to streamline and automate the research process. Built with LangChain and Streamlit, it orchestrates a collaborative pipeline of specialized AI agents that search the web, scrape deep content, synthesize information, and critique findings to deliver a comprehensive, polished research report on any given topic.

## 🌟 Key Features

*   **Multi-Agent Orchestration**: Utilizes a sophisticated 4-step pipeline of AI agents with distinct roles (Search, Reader, Writer, Critic).
*   **Intelligent Web Searching**: Leverages the Tavily Search API to gather the most recent and reliable information, titles, URLs, and snippets.
*   **Deep Content Scraping**: Automatically selects the most relevant URLs and scrapes clean, readable text using BeautifulSoup for deep context extraction.
*   **Automated Report Generation**: Synthesizes gathered data into a structured, well-formatted markdown report.
*   **Self-Critique & Review**: Includes a critic agent that reviews and scores the drafted report to ensure high quality and accuracy.
*   **Stunning UI**: Features a custom, highly responsive, and interactive Streamlit UI with real-time pipeline status tracking, dynamic CSS styling, and downloadable reports.

## 🏗️ Architecture & Pipeline

The system operates through a sequential, LangChain-powered multi-agent pipeline:

1.  **Search Agent (🔍)**: Takes the user's research topic and queries the web to find the most relevant, up-to-date sources.
2.  **Reader Agent (📄)**: Evaluates search results, selects the top resource, and performs deep web scraping to extract comprehensive text.
3.  **Writer Chain (✍️)**: Processes the combined search snippets and scraped content to draft a detailed, structured research report.
4.  **Critic Chain (🧐)**: Analyzes the writer's draft, providing feedback, scoring, and refinement suggestions for the final output.

## 🛠️ Technology Stack

*   **Core Logic**: Python, LangChain, Google Gemini (via `langchain-google-genai`)
*   **Frontend UI**: Streamlit with custom CSS (Glassmorphism, dynamic gradients)
*   **Web Search**: Tavily API (`tavily-python`)
*   **Web Scraping**: BeautifulSoup4, Requests, HTML5lib
*   **Environment Management**: `python-dotenv`

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Gen_Ai_Project
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 💡 Usage

1. Open the application in your browser (usually `http://localhost:8501`).
2. Enter a research topic in the input field (e.g., "Quantum computing breakthroughs in 2025").
3. Click on **⚡ Run Research Pipeline**.
4. Watch the agents work in real-time on the right-hand panel.
5. Review the final generated report and the critic's feedback.
6. Download the comprehensive `.md` report for your records.

## 📝 Future Enhancements

*   Integration with vector databases (e.g., ChromaDB, Pinecone) for persistent knowledge retrieval.
*   Support for multiple concurrent search paths and comparative analysis.
*   Export options for PDF and DOCX formats.

---
*This project highlights expertise in Generative AI, prompt engineering, agentic workflows, and full-stack Python development.*
