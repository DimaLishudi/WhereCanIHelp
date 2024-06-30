from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DBNAME = os.getenv("DBNAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT",5432)

main_engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DBNAME}")
