from fastapi import FastAPI
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Navitrac AI")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.get("/")
def home():
    return {"message": "Navitrac AI Server Running"}
