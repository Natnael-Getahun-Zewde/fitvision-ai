import numpy as np

class FeatureExtractor:

    def extract_features(self, landmarks):

        if landmarks is None or len(landmarks) == 0:
            return None

        landmarks = np.array(landmarks)

        # flatten (33 landmarks × 3 values)
        features = landmarks.flatten()

        return features