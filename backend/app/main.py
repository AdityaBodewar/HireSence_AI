from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def home():
    return {"messsage":"server is running "}