import os
from dotenv import load_dotenv

load_dotenv()
DBNAME = os.getenv("DBNAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT",5432)

settings = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DBNAME}"