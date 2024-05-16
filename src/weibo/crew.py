from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from weibo.tools.search import SearchTools

@CrewBase
class WeiboCrew():
	"""Weibo crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def market_researcher(self) -> Agent:
		return Agent(
            config=self.agents_config["market_researcher"],
            tools=[
              SearchTools.search_internet,
              SearchTools.search_weibo,
              SearchTools.open_page,
            ],
            verbose=True,
        )

	@agent
	def content_strategist(self) -> Agent:
		return Agent(config=self.agents_config["content_strategist"], verbose=True)

	@agent
	def visual_creator(self) -> Agent:
		return Agent(
			config=self.agents_config["visual_creator"],
			verbose=True,
			allow_delegation=False,
		)

	@agent
	def copywriter(self) -> Agent:
		return Agent(config=self.agents_config["copywriter"], verbose=True)

	@task
	def market_research(self) -> Task:
		return Task(
			config=self.tasks_config["market_research"],
			agent=self.market_researcher(),
			output_file="market_research.md",
		)

	@task
	def content_strategy_task(self) -> Task:
		return Task(
			config=self.tasks_config["content_strategy"],
			agent=self.content_strategist(),
		)

	@task
	def visual_content_creation_task(self) -> Task:
		return Task(
			config=self.tasks_config["visual_content_creation"],
			agent=self.visual_creator(),
			output_file="visual-content.md",
		)

	@task
	def copywriting_task(self) -> Task:
		return Task(
			config=self.tasks_config["copywriting"],
			agent=self.copywriter(),
		)

	@task
	def report_final_content_strategy(self) -> Task:
		return Task(
			config=self.tasks_config["report_final_content_strategy"],
			agent=self.content_strategist(),
			output_file="final-content-strategy.md",
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Weibo crew"""
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=2,
			#language="zh-CN",
			# process=Process.hierarchical,
		)