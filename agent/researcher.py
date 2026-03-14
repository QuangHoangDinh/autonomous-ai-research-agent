import os
from langchain_community.tools.tavily_search import TavilyAnswer

class ResearchAgent:
    def __init__(self):
        self.tavily = TavilyAnswer()

    def perform_research(self, topic: str):
        # Simulated multi-step research
        queries = [
            f"{topic} overview and core concepts",
            f"latest trends in {topic} 2024-2025",
            f"challenges and future outlook of {topic}"
        ]
        
        results = []
        for q in queries:
            try:
                results.append(self.tavily.run(q))
            except Exception as e:
                print(f"Error during search: {e}")
        
        return "\n\n".join(results)
