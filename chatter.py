import os


os.environ['OPENAI_API_KEY'] = "..."


from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor

db = SQLDatabase.from_uri("sqlite:///./Chinook.db")
toolkit = SQLDatabaseToolkit(db=db)

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0.9),
    toolkit=toolkit,
    verbose=True
)

agent_executor.run("Describe the playlisttrack table")