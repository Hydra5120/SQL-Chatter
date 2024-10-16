# SQL-Chatter

A machine learning application that leverages large language models (LLMs) to enable users to interact with SQL databases using natural language. By translating user inputs into SQL queries, this app provides a seamless, conversational interface for querying and managing database information without requiring SQL expertise. Intended for use with the **Athena ERP system**.

## Features

- **Natural Language to SQL**: Users can query databases using plain English, which is automatically translated into SQL queries.
- **Database Support**: Compatible with popular SQL databases like MySQL, PostgreSQL, and SQLite.
- **Real-Time Query Execution**: Results from database queries are fetched and displayed instantly.
- **User-Friendly Interface**: A conversational, easy-to-use interface powered by LLMs.

## Technologies

- Python
- LangChain
- Athena ERP system integration



## Installation

To begin using LangChain, install it using pip:
``pip install langchain``



LangChain typically requires integration with various model providers, data stores, and APIs. For this example, we'll use OpenAI's APIs.

First, install the OpenAI SDK:
``pip install openai``

Next, set up your OpenAI API key. You can do this in two ways:

1. Set it as an environment variable in your terminal:
``export OPENAI_API_KEY="..."``

2. Or, set it directly in your Python script:

```python
import os
os.environ["OPENAI_API_KEY"] = "..."
```


