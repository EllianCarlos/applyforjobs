from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Applyforjobs:
    """Applyforjobs crew"""
    agents_config = 'config/agents.yaml'
    llm = LLM(model="ollama/deepseek-14b-custom",base_url="http://localhost:11434")
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        print(self.llm)

    @before_kickoff
    def create_llm(self,inputs) -> None:
        return inputs

    @after_kickoff
    def after_kickoff_function(self, result):
        print("=============================================")
        print("=============================================")
        print("=============================================")
        print("=============================================")
        print(f"After kickoff function with result: {result}")
        return result # You can return the result or modify it as needed


    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            llm=self.llm,
            verbose=True,
        )

    @task
    def create_resume(self) -> Task:
        return Task(
            config=self.tasks_config['write_resume'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Applyforjobs crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
