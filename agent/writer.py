from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class WritingAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7)

    def generate_report(self, topic: str, context: str):
        prompt = ChatPromptTemplate.from_template("""
        You are a Senior AI Research Scientist. Your goal is to write a comprehensive, professional, 
        and high-quality research report based on the provided context.
        
        Topic: {topic}
        Context: {context}
        
        Instructions:
        1. Create a structured report in Markdown format.
        2. Include an Abstract, Introduction, Key Findings, Current Trends, Challenges, and Future Outlook.
        3. Ensure professional and technical tone.
        4. Cite the data provided appropriately.
        """)
        
        chain = prompt | self.llm
        response = chain.invoke({"topic": topic, "context": context})
        
        return response.content
