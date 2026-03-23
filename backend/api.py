from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

from ml_engine.pose_extractor import PoseExtractor
from ml_engine.feature_extractor import FeatureExtractor

app = FastAPI()

pose_extractor = PoseExtractor()
feature_extractor = FeatureExtractor()


@app.get("/")
def home():
    return {"message": "FitVision AI API is running"}


@app.post("/analyze_frame")
async def analyze_frame(file: UploadFile = File(...)):

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)

    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    landmarks = pose_extractor.extract(frame)

    features = feature_extractor.extract_features(landmarks)

    if features is None:
        return {"status": "no_pose_detected"}

    return {
        "status": "pose_detected",
        "feature_length": len(features)
    }