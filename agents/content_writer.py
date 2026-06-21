import os
from crewai import Agent, LLM
from crewai_tools import FileWriterTool


# LLM configurations - Agent specific config
# Using os.environ clears the type-checking errors by ensuring these values aren't None
model = os.environ["WRITER_AGENT_LLM"]
temperature = float(os.environ["WRITER_AGENT_TEMPERATURE"])

llm = LLM(
    model=model,
    temperature=temperature
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create comprehensive, well-structured reports and summaries",
    backstory = (
                "You are a professional content writer with expertise in creating "
                "clear, engaging, and well-structured documents. You can transform complex "
                "information into accessible and compelling content."
            ),
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
)