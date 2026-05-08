# 😊 AI Emotion Detection System (Deep Learning + NLP)

---

# 📌 Overview

The **AI Emotion Detection System** is a Deep Learning and NLP-based application that identifies human emotions from textual input.

The system processes natural language text and predicts emotional categories such as:

* 😊 Happy
* 😢 Sad
* 😡 Angry
* 😨 Fear
* 😍 Love
* 😐 Neutral

This project demonstrates how sequence learning models like **LSTM (Long Short-Term Memory)** networks can understand contextual and emotional patterns in human language.

---

# 🎯 Problem Statement

Understanding emotions from text is an important challenge in Natural Language Processing.

Modern AI systems need emotional intelligence for:

* customer support automation
* mental health applications
* chatbot systems
* social media monitoring
* sentiment-aware AI assistants

This project automates emotion recognition using Deep Learning techniques.

---

# ✨ Features

* 🧠 Emotion prediction from text
* 🔤 NLP text preprocessing
* 📊 Confidence score output
* ⚡ Interactive Streamlit interface
* 🤖 Deep Learning architecture using LSTM

---

# 🧠 Tech Stack

* **Python**
* **TensorFlow / Keras**
* **Streamlit**
* **NumPy**
* **Pandas**
* **Scikit-learn**

---

# 🏗️ System Architecture

```text id="kxl3d0"
Input Text
     ↓
Text Cleaning
     ↓
Tokenization
     ↓
Embedding Layer
     ↓
LSTM Network
     ↓
Emotion Prediction
```

---

# 📂 Project Structure

```text id="ecm0f6"
ai-emotion-detection/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── model.py
│   └── predict.py
│
├── utils/
│   └── preprocess.py
│
├── sample_data/
│   └── emotions.csv
```

---

# 📄 File Explanation

---

## 🔹 `app.py`

Main Streamlit application.

### Responsibilities:

* Takes user text input
* Calls prediction function
* Displays emotion prediction and confidence score

---

## 🔹 `model/model.py`

Defines the Deep Learning model architecture.

### Includes:

* Embedding Layer
* LSTM Layer
* Dense Layers
* Softmax Output

---

## 🔹 `model/predict.py`

Handles:

* Text prediction logic
* Emotion label generation
* Confidence score output

---

## 🔹 `utils/preprocess.py`

Performs NLP preprocessing:

* Lowercasing
* Removing special characters
* Cleaning text

---

## 🔹 `sample_data/emotions.csv`

Sample dataset containing:

* Text samples
* Emotion labels

Used for:

* Testing
* Training demonstrations

---

# 🧠 Deep Learning Concepts Used

---

## ✅ 1. NLP (Natural Language Processing)

Understanding human language using AI.

---

## ✅ 2. LSTM Networks

LSTM is a type of Recurrent Neural Network (RNN) used for sequence learning.

It helps AI remember:

* sentence context
* word relationships
* emotional patterns

---

## ✅ 3. Embedding Layer

Converts words into numerical vectors that preserve semantic meaning.

---

## ✅ 4. Softmax Classification

Used for multi-class emotion prediction.

---

# ▶️ How to Run

---

## 1️⃣ Install dependencies

```bash id="c6g8kt"
pip install -r requirements.txt
```

---

## 2️⃣ Run application

```bash id="j4pb0v"
streamlit run app.py
```

---

# 💡 Example

### Input

```text id="gqfajm"
I feel very stressed and tired today.
```

---

### Output

```text id="5onjlwm"
Emotion: Sad
Confidence: 91%
```

---

# 🎯 Use Cases

* Mental health AI
* Emotion-aware chatbots
* Customer feedback analysis
* Social media sentiment monitoring
* Conversational AI systems

---

# 📬 Author

**Joncy Keda - AI Developer**
