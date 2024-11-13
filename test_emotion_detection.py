import unittest
from EmotionDetection.emotion_detection import emotion_detector

test_data = {
    "I am glad this happened": "joy",
    "I am really mad about this": "anger",
    "I feel disgusted just hearing about this": "disgust",
    "I am so sad about this": "sadness",
    "I am really afraid that this will happen": "fear"
}

def fetch_emotion(text: str) -> str:
    emotions = emotion_detector(text)
    return emotions["dominant_emotion"]

class EmotionDetectionTest(unittest.TestCase):
    def test_emotion_detector(self):
        for (text, expected_motion) in test_data.items():
            self.assertEqual(fetch_emotion(text), expected_motion)

if __name__ == "__main__":
    unittest.main()