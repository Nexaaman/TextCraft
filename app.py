from fastapi import FastAPI 
import uvicorn
import sys
import os

from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from TextCraft.pipeline.Prediction import PredictionPipeline

text:str = "What is a large language model?"
app = FastAPI()

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python3 main.py")
        return Response("Traning Sucessfully!")
    except Exception as e:
        return Response(f"Error Occured! {e}")
    
@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)