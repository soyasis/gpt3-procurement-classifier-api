import openai
import os
from fastapi import FastAPI
from functions import *

# read API key from system environment
openai.api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

@app.get("/")
def read_root():
    return {"About": "This is a simple API using GPT-3 and FastAPI for text classification.",
            "Docs & Testing": "Check the documentation at /docs",
            "With ♥ by": "@plasticfruits"}


@app.get("/suggestions/", status_code=200)
def get_suggestions(query: str) -> dict:
    """
    Get categories from a free text query
    """  
    response = get_categories(query)

    return {'suggestions': response}