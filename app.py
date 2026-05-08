import streamlit as st
from model.predict import predict_emotion

st.set_page_config(
    page_title="AI Emotion Detection",
    layout="wide"
)

st.title("😊 AI Emotion Detection System")

text = st.text_area("Enter text")

if st.button("Analyze Emotion"):
    emotion, confidence = predict_emotion(text)

    st.subheader("📊 Prediction")

    st.success(f"Emotion: {emotion}")
    st.info(f"Confidence: {confidence:.2f}%")
