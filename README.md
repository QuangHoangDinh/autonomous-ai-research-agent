# 🤖 Autonomous AI Research Agent

An advanced, multi-agent AI system that autonomously performs deep web research on any given topic, synthesizes findings, and generates a structured, high-quality markdown report.

Built with **LangChain**, **OpenAI/Gemini**, and **Tavily Search**, this agent mimics the workflow of a human researcher by iteratively searching, evaluating, and writing.

---

### ✨ Key Features
- **Autonomous Research**: Decides what to search for and how to synthesize the information.
- **Source Citation**: Automatically cites sources for all information gathered.
- **Iterative Refinement**: The agent critiques its own work and improves the final report.
- **Multi-Agent Architecture**: Separate agents for 'Researching' and 'Writing' to ensure quality.

---

### 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/QuangHoangDinh/autonomous-ai-research-agent.git
   cd autonomous-ai-research-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API Keys**
   Create a `.env` file from the template:
   ```bash
   cp .env.example .env
   ```
   Add your `OPENAI_API_KEY` (or `GOOGLE_API_KEY`) and `TAVILY_API_KEY`.

4. **Run the Agent**
   ```bash
   python main.py
   ```

---

### 🛠️ Technology Stack
- **Framework**: LangChain
- **LLM**: GPT-4o / Gemini 1.5 Pro
- **Search Engine**: Tavily AI
- **Environment**: Python 3.9+

---

### 📜 License
MIT
