import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import cv2
import pandas as pd

from ml_engine.pose_extractor import PoseExtractor
from ml_engine.feature_extractor import FeatureExtractor
import cv2
import pandas as pd
import os

from ml_engine.pose_extractor import PoseExtractor
from ml_engine.feature_extractor import FeatureExtractor

pose_extractor = PoseExtractor()
feature_extractor = FeatureExtractor()

dataset = []


def process_video(video_path, label):

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        landmarks = pose_extractor.extract(frame)

        features = feature_extractor.extract_features(landmarks)

        if features is not None:

            row = list(features) + [label]

            dataset.append(row)

    cap.release()


def build_dataset():

    video_folder = "dataset/raw_videos"

    if not os.path.exists(video_folder):
        print("raw_videos folder not found")
        return

    for file in os.listdir(video_folder):

        if file.endswith(".mp4"):

            label = file.split("_")[0]

            video_path = os.path.join(video_folder, file)

            print("Processing:", file)

            process_video(video_path, label)

    if len(dataset) == 0:
        print("No data collected")
        return

    df = pd.DataFrame(dataset)

    os.makedirs("dataset", exist_ok=True)

    df.to_csv("dataset/dataset.csv", index=False)

    print("Dataset saved to dataset/dataset.csv")


if __name__ == "__main__":

    build_dataset()