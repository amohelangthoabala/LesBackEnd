from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return "Home URL"