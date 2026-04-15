# 🧠 MindShield AI

### AI-Powered Mental Health Monitoring & Early Risk Detection System

---

## 📌 Overview

**MindShield AI** is an intelligent mental health analysis system that helps users track their thoughts, identify negative thinking patterns, and predict the risk of mental health relapse.

The system combines **Natural Language Processing (NLP)** and **Machine Learning (ML)** to analyze user input and provide meaningful insights such as emotional state, cognitive patterns, and relapse risk levels.

---

## 🚀 Key Features

### ✍️ Thought Journal

* Users can write their daily thoughts
* Entries are stored date-wise
* Calendar-based tracking system

### 📊 Sentiment Analysis

* Uses VADER (NLTK)
* Detects emotional tone:

  * Positive
  * Negative
  * Neutral

### 🧠 Cognitive Pattern Detection

* Identifies negative thinking patterns such as:

  * Always thinking negative
  * Expecting the worst
  * Blaming yourself
  * Assuming others think badly
  * All or nothing thinking(Seeing things in extremes only — either 100% good or 100% bad)

### ⚠️ Relapse Risk Prediction

* Uses Machine Learning (Random Forest)
* Predicts risk level:

  * 🟢 Low
  * 🟡 Medium
  * 🔴 High

## 🖥️ Interactive UI
Built with Streamlit
Sidebar date selection
Displays:
Past entries
Sentiment
CBT patterns
Risk level

---

## 🏗️ Project Architecture

```
User Input (Streamlit UI)
        ↓
Preprocessing (Text Cleaning)
        ↓
Sentiment Analysis (VADER)
        ↓
Cognitive Pattern Detection
        ↓
Machine Learning Model (Random Forest)
        ↓
Risk Prediction (Low / Medium / High)
        ↓
UI Display + History Storage
```

---

## 🛠️ Tech Stack

* **Frontend + Backend:** Streamlit
* **NLP:** NLTK (VADER, Tokenization, Stopwords)
* **Machine Learning:** Scikit-learn (Random Forest)
* **Language:** Python
* **Data Handling:** Pandas, NumPy

---

## 📂 Project Structure

```
MindShield/
│
├── app.py
├── train_model.ipynb
│
├── modules/
│   ├── preprocessing.py
│   ├── sentiment.py
│   ├── distortion.py
│   └── model.py
│
├── data/
│ └── dataset.csv
│
├── models/
│ └── model.pkl
│
├── README.md
├── LICENSE
```

---

## ⚙️ How to Run

### 1. Clone Repository

```
git clone <your-repo-link>
cd MindShield
```

### 2. Create Virtual Environment

```
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run App

```
streamlit run app.py
```

---

---

## ⚠️ Disclaimer

This project is for **educational and experimental purposes only**.
It is **not a substitute for professional medical advice or mental health treatment**.

---

## 👨‍💻 Author

Rudrajit Dey

---
