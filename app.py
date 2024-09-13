from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from TextCraft.pipeline.Prediction import PredictionPipeline
import uvicorn
import os

# Initialize the app and Jinja2 templates
app = FastAPI()
templates = Jinja2Templates(directory=os.path.join("UI" , "template"))

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "output_text": ""})

@app.post("/predict", response_class=HTMLResponse)
async def predict_route(request: Request, user_input: str = Form(...)):
    try:
        # Perform prediction using your PredictionPipeline
        obj = PredictionPipeline()
        generated_text = obj.predict(user_input)
        # Return the template with the generated output
        return templates.TemplateResponse("index.html", {"request": request, "output_text": generated_text})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "output_text": f"Error: {e}"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
