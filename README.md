# Synonym_Engine
This project is a Synonym Retrieval System built in Python that integrates:

Microsoft SQL Server (for persistent synonym data)

Redis (for caching query results)

pyODBC (to connect Python to SQL Server)

dotenv (to manage secure environment configs)

VS Code + Git for development and version control

🚀 What This Project Does
Connects to a Microsoft SQL Server database and retrieves all synonym entries.

Caches the full synonym dataset in Redis with a TTL (time-to-live) of 1 hour.

Returns cached data on subsequent runs, reducing database load.

Uses .env file to securely store connection details for both SQL Server and Redis.

✅ What I Did
✅ Set up Microsoft SQL Server Express and created a database with a synonyms table.

✅ Populated the database with example synonym entries.

✅ Installed and configured Redis using Docker for caching.

✅ Wrote modular Python code:

main.py – Orchestrator script

db_utils.py – Fetches data from SQL Server

cache_utils.py – Manages Redis cache

✅ Integrated .env file support using python-dotenv

✅ Handled edge cases like invalid connections and cached errors

✅ Debugged connection issues including:

SQL Server TCP/IP port settings

SQL Server Browser and instance naming

✅ Used Git and GitHub for version control and project tracking

💻 Tech Stack
Language: Python 3.x

Database: SQL Server 2019 Express

Cache: Redis (via Docker)

Libraries:

pyodbc

redis

python-dotenv

Tools: Docker, VS Code, Git, GitHub
