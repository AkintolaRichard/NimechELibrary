from dotenv import load_dotenv
import os
load_dotenv
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITH = os.environ.get("ALGORITH")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
DB_URL = os.environ.get("DB_URL")
