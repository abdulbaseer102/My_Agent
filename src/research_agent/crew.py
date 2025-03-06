import os
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool

# Set API Keys
os.environ["SERPER_API_KEY"] = "765f15d8edae4a379eec3419154c1387cf260d9c"
os.environ["OPENAI_API_KEY"] = "AIzaSyAqUg4mAvMsDFj1-3JABZGvlmgT4pDiPTM"

# Tools
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

@CrewBase
class ResearchAgent:
    """Crew to analyze and report on images"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def image_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['image_researcher'],
            tools=[search_tool, web_rag_tool],
            multimodal=True,
            verbose=True
        )

    @agent
    def expert_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['expert_analyst'],
            multimodal=True,
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            tools=[search_tool, web_rag_tool],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def inspection_task(self) -> Task:
        research = self.research_task()  # Getting previous task output
        return Task(
            config=self.tasks_config['inspection_task'],
            dependencies=[research],
            output_file='inspection_results.txt',
            agent=self.expert_analyst()
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.image_researcher(), self.expert_analyst(), self.reporting_analyst()],
            tasks=[self.research_task(), self.inspection_task(), self.reporting_task()],
            process=Process.sequential,
            verbose=True
        )
