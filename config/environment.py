import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URL = os.getenv('URLBANCO') or "postgresql://postgres:docker@localhost:5433/postgres"
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or "teste123"



