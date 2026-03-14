import os
from dotenv import load_dotenv
from agent.researcher import ResearchAgent
from agent.writer import WritingAgent

load_dotenv()

def run_research_pipeline(topic: str):
    print(f"🚀 Starting research on: {topic}")
    
    # Step 1: Research Agent
    researcher = ResearchAgent()
    print("🔍 Gathering data from multiple sources...")
    data = researcher.perform_research(topic)
    
    # Step 2: Writing Agent
    writer = WritingAgent()
    print("✍️ Synthesizing findings and writing report...")
    report = writer.generate_report(topic, data)
    
    # Step 3: Save Report
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    filename = f"reports/{topic.replace(' ', '_').lower()}_report.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Research completed! Report saved to {filename}")

if __name__ == "__main__":
    user_topic = input("Enter a research topic: ")
    if user_topic:
        run_research_pipeline(user_topic)
