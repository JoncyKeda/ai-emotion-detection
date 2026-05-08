import random
import numpy as np
from utils.preprocess import clean_text

emotions = [
    "Happy",
    "Sad",
    "Angry",
    "Fear",
    "Love",
    "Neutral"
]

# Demo prediction logic
# Replace with trained model later

def predict_emotion(text):

    cleaned = clean_text(text)

    emotion = random.choice(emotions)

    confidence = np.random.uniform(80, 99)

    return emotion, confidence
