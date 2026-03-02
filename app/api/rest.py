from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
async def status():
    return {"guardian": "running"}

@app.get("/topology")
async def topology():
    return {"file": "topology.png"}
