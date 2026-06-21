import os
from crewai import Agent, LLM
from crewai_tools import FileReadTool


# LLM configurations - Agent specific config
# Using os.environ ensures Pylance recognizes these as strings, clearing the errors
model = os.environ["ANALYST_AGENT_LLM"]
temperature = float(os.environ["ANALYST_AGENT_TEMPERATURE"])

llm = LLM(
    model=model,
    temperature=temperature
)

data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Analyze gathered information to extract key insights, patterns, and conclusions",
    backstory = (
                "You are a skilled data analyst with expertise in synthesizing complex "
                "information into actionable insights. You excel at identifying patterns, trends, "
                "and key findings from research data."
            ),
    llm=llm,
    tools=[FileReadTool()],
    verbose=True,
)