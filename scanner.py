import cv2
from ml_engine.pose_extractor import PoseExtractor
from ml_engine.feature_extractor import FeatureExtractor

video_path = "dataset/raw_videos/test_video.mp4"

cap = cv2.VideoCapture(video_path)

pose_extractor = PoseExtractor()
feature_extractor = FeatureExtractor()

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    landmarks = pose_extractor.extract(frame)

    features = feature_extractor.extract_features(landmarks)

    if features is not None:
        print("Feature vector size:", len(features))

    cv2.imshow("FitVision Scanner", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()