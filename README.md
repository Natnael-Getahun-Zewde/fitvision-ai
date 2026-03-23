# FitVision AI

FitVision AI is an AI-powered fitness analysis system that uses **computer vision and machine learning** to detect human pose, analyze exercises, and build training datasets from workout videos.

The project demonstrates a **full machine learning pipeline**, from dataset generation and feature extraction to model training, backend deployment, and mobile app integration.

---

## Features

* Pose detection using MediaPipe
* Feature extraction from body landmarks
* Exercise classification (squat, push-up, plank, jumping jack)
* AI dataset generator from workout videos
* Machine learning training pipeline with PyTorch
* FastAPI backend for real-time AI analysis
* Mobile integration with Flutter
* Workout analytics and progress tracking

---

## Tech Stack

**Machine Learning**

* PyTorch
* Scikit-learn
* NumPy
* Pandas

**Computer Vision**

* OpenCV
* MediaPipe Pose

**Backend**

* FastAPI
* Uvicorn

**Mobile**

* Flutter

---

## Project Architecture

```
FITVISION_AI
│
├ analytics
│   └ progress_analysis.py
│
├ backend
│   ├ api.py
│   ├ database.py
│   └ scoring.py
│
├ dataset
│   ├ raw_videos
│   ├ processed
│   ├ dataset.csv
│   └ progress.json
│
├ ml_engine
│   ├ pose_extractor.py
│   ├ feature_extractor.py
│   ├ rep_counter.py
│   ├ posture_analyzer.py
│   └ exercise_classifier.py
│
├ training_pipeline
│   ├ dataset_builder.py
│   └ train_model.py
│
├ mobile_app
│   └ fitvision_app
│
├ models
│   └ exercise_model.pth
│
├ utils
│   └ pose_utils.py
│
├ scanner.py
├ requirements.txt
└ README.md
```

---

## Machine Learning Pipeline

```
Workout Videos
      ↓
Pose Detection (MediaPipe)
      ↓
Landmark Feature Extraction
      ↓
Dataset CSV
      ↓
Model Training (PyTorch)
      ↓
Exercise Classification
      ↓
Real-Time Workout Analysis
```

---

## Installation

Clone the repository:

```
git clone https://github.com/Natnael-Getahun-Zewde/fitvision-ai.git
cd fitvision-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Generate Training Dataset

Place workout videos in:

```
dataset/raw_videos/
```

Example:

```
squat_1.mp4
pushup_1.mp4
plank_1.mp4
jumpingjack_1.mp4
```

Run the dataset generator:

```
python training_pipeline/dataset_builder.py
```

This will generate:

```
dataset/dataset.csv
```

---

## Train the Machine Learning Model

```
python training_pipeline/train_model.py
```

The trained model will be saved to:

```
models/exercise_model.pth
```

---

## Run the Backend API

Start the FastAPI server:

```
uvicorn backend.api:app --reload
```

API documentation will be available at:

```
http://127.0.0.1:8000/docs
```

---

## Mobile Application

The Flutter mobile app communicates with the FastAPI backend to:

* capture camera frames
* send images to the AI engine
* receive exercise analysis results
* track workout progress

---

## Example Use Cases

* AI-powered fitness trainer
* Exercise form analysis
* Workout tracking
* Pose-based exercise recognition
* Fitness analytics

---

## Skills Demonstrated

This project demonstrates experience with:

* Computer Vision
* Machine Learning Engineering
* Dataset Generation
* Feature Engineering
* Backend API Development
* Mobile App Integration
* AI System Architecture

---

## Future Improvements

* Real-time exercise classification
* Posture correction system
* AI rep counting
* Workout recommendation system
* Cloud deployment
* User authentication

---

## License

This project is open-source and available under the MIT License.
