import cv2
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import uvicorn
import os

app = FastAPI()
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload")
async def upload_image(image: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, image.filename)


    # Get the image's bytes
    image_bytes = await image.read()
    # Decode image from bytes
    np_array = np.frombuffer(image_bytes, np.uint8)
    input_image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    # input_image can be used for further processing if needed.
    # For example, Yolov11 can process it directly.

    # Save the image to the specified location
    if input_image is not None:
        cv2.imwrite(file_location, input_image)


    # Return a success message to client
    return JSONResponse(content={"message": f"Image '{image.filename}' uploaded successfully!"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)