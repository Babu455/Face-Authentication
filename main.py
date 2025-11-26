from fastapi import FastAPI, File, UploadFile
from deepface import DeepFace
from PIL import Image
import numpy as np
import io

app = FastAPI()

def read_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes))
    return np.array(image)

@app.post("/verify")
async def verify(img1: UploadFile = File(...), img2: UploadFile = File(...)):
    img1_bytes = await img1.read()
    img2_bytes = await img2.read()

    image1 = read_image(img1_bytes)
    image2 = read_image(img2_bytes)

    # --- Main verification ---
    result = DeepFace.verify(
        image1, image2,
        enforce_detection=True,
        detector_backend='retinaface'   # ensures bounding boxes
    )

    # DeepFace returns this structure:
    # result["verified"]
    # result["distance"]
    # result["facial_areas"]["img1"]  <-- bounding box
    # result["facial_areas"]["img2"]

    verified = "same person" if result["verified"] else "different person"

    bbox1 = result["facial_areas"]["img1"]
    bbox2 = result["facial_areas"]["img2"]

    return {
        "verification_result": verified,
        "similarity_score": float(result["distance"]),
        "bounding_boxes": {
            "image1": bbox1,
            "image2": bbox2
        }
    }

@app.get("/")
def home():
    return {"status": "face api running"}
