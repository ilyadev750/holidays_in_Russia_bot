from sqlalchemy import create_engine
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

engine = create_engine(f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('CONTAINER')}/russian_holidays", echo=True)



