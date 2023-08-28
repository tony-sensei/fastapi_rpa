from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from actions import get_elements

app = FastAPI()

@app.post("/process-screenshot/")
async def process_screenshot(file: UploadFile = File(...)):
    # Read the uploaded file
    image_data = await file.read()
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Process the screenshot
    elements = get_elements(img)

    # Return the processed data as JSON
    return JSONResponse(content={"elements": elements})
