import base64
from contextlib import asynccontextmanager
import io
from PIL import Image
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from constants import PORT, RELOAD, SERVER_URL
from schema import CalculateRequest, CalculateResponse
from utils import analyze_image


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def check_health():
    return {"message": "Server is running!"}


@app.post("/calculate")
async def calculate(request: CalculateRequest):
    image_data = base64.b64decode(request.image.split(",")[1])
    image_bytes = io.BytesIO(image_data)
    image = Image.open(image_bytes)

    answers = analyze_image(image, request.dict_of_vars)

    if not answers:
        return CalculateResponse(message="No answers found", success=False)

    return CalculateResponse(message="Answers found", success=True, data=answers)


if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=PORT, reload=RELOAD)
