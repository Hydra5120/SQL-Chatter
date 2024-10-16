
import os

os.environ['OPENAI_API_KEY'] = "..."
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI



conn = sqlite3.connect('Chinook.db')
with open('./Chinook_Sqlite.sql', 'r',encoding='cp1252', errors='replace') as f:
    sql_script = f.read()
conn.executescript(sql_script)
conn.close()


db = SQLDatabase.from_uri("sqlite:///./Chinook.db")
llm = ChatOpenAI(temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(
    llm=ChatOpenAI(model='gpt-4o-mini', temperature=0),
    toolkit=toolkit,
    verbose=True, handle_parsing_errors=True
)



root = tk.Tk()
root.title("Chat with your SQL Data")


entry = ttk.Entry(root, font=("Arial", 14))
entry.pack(padx=20, pady=20, fill=tk.X)


def on_click():
    
    query = entry.get()

    
    result = agent_executor.run(query)

    
    text.delete("1.0", tk.END)
    text.insert(tk.END, result)


button = ttk.Button(root, text="Chat", command=on_click)
button.pack(padx=20, pady=20)


text = tk.Text(root, height=10, width=60, font=("Arial", 14))
text.pack(padx=20, pady=20)


root.mainloop()


