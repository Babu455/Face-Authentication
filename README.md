# Face Verification API (FastAPI + DeepFace)

This project provides a simple **Face Authentication API** using **FastAPI** and **DeepFace**.
I Can upload two face images, and the API will:

* Detect faces in both images
* Extract facial embeddings
* Compare similarity
* Return:

  * Same Person / Different Person
  * Similarity Score
  * Bounding Boxes for both images

This project is created for learning and assignment use.

---

## Features

* Upload two images via API
* Uses **RetinaFace** detector for accurate bounding boxes
* Returns clean JSON result
* Lightweight FastAPI service

---

## Requirements

Install the dependencies:

```
pip install -r requirements.txt
```

##  How to Run

Run the FastAPI server:

```
uvicorn main:app --reload
```

Open browser and go to:

```
http://127.0.0.1:8000/docs
```

will see Swagger UI to upload two images and test the API.

---

## API Endpoint

### **POST /verify**

Form-data Upload:

* `img1` → first image
* `img2` → second image

### Example Response

```json
{
  "verification_result": "same person",
  "similarity_score": 0.42,
  "bounding_boxes": {
    "image1": { ... },
    "image2": { ... }
  }
}
```

---

## Project Structure

```
face-verification-api/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
│── response(output)
```

