import streamlit as st
import datetime
from modules.preprocessing import preprocess
from modules.sentiment import get_sentiment
st.set_page_config(layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📅 Select Date")

selected_date = st.sidebar.date_input("Choose a date", datetime.date.today())

# Store history
if "history" not in st.session_state:
    st.session_state.history = {}

# Sidebar display
st.sidebar.subheader("📜 Entry Details")

if selected_date in st.session_state.history:
    entry = st.session_state.history[selected_date]

    st.sidebar.write("📝", entry["text"])

    # Risk display with color
    risk = entry["risk"]
    if risk == "High":
        st.sidebar.error("⚠️ High Risk")
    elif risk == "Medium":
        st.sidebar.warning("⚡ Medium Risk")
    else:
        st.sidebar.success("✅ Low Risk")

else:
    st.sidebar.write("No entry for this date")

# ---------------- MAIN UI ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

.title {
    font-family: 'Poppins', sans-serif;
    text-align: center;
    font-size: 48px;
}
</style>

<h1 class="title">🧠 MindShield AI</h1>
""", unsafe_allow_html=True)

text = st.text_area(
    "",
    height=200,
    placeholder="How are you feeling today? What’s on your mind?"
)

# Dummy risk (for now, until ML is added)
def fake_risk(text):
    text = text.lower()
    if "always" in text or "worst" in text:
        return "High"
    elif "stress" in text or "tired" in text:
        return "Medium"
    else:
        return "Low"

# ---------------- BUTTON ----------------
if st.button("Save Entry"):

    if text.strip() == "":
        st.warning("Please write something")
    else:
        clean = preprocess(text)
        sentiment, score = get_sentiment(text)
        risk = fake_risk(clean)

        st.session_state.history[selected_date] = {
            "text": text,
            "risk": risk
        }

        st.success("✅ Entry saved!")

# ---------------- MAIN DISPLAY ----------------
if selected_date in st.session_state.history:
    entry = st.session_state.history[selected_date]

    st.markdown("### 📖 Entry Confirmed")
    st.write(entry["text"])

    st.markdown("### 📊 Risk Level")

    if entry["risk"] == "High":
        st.error("⚠️ High Risk")
    elif entry["risk"] == "Medium":
        st.warning("⚡ Medium Risk")
    else:
        st.success("✅ Low Risk")