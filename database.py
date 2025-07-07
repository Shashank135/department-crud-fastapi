from pymongo import MongoClient # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["agamin"]
department_collection = db["departments"]
