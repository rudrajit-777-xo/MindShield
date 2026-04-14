import streamlit as st
import datetime
from modules.preprocessing import preprocess
from modules.sentiment import get_sentiment
from modules.distortion import detect_cbt_patterns
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

<h1 class="title">MindShield AI</h1>
""", unsafe_allow_html=True)

text = st.text_area(
    "",
    height=200,
    placeholder="How are you feeling today? What’s on your mind?"
)



# ---------------- BUTTON ----------------
if st.button("Save Entry"):

    if text.strip() == "":
        st.warning("Please write something")
    else:
        clean = preprocess(text)
        sentiment, score = get_sentiment(text)
        cbt_patterns = detect_cbt_patterns(clean)
        cbt_score = len(cbt_patterns)
        #ML (FUTURE)
        # 👉 Replace this later with:
        # from modules.model import predict_risk
        # risk = predict_risk([score, cbt_score])
        risk = "Coming Soon"   # placeholder for now

        st.session_state.history[selected_date] = {
            "text": text,
            "risk": risk
        }

        st.success("✅ Entry saved!")

         # 🔥 SENTIMENT
        st.markdown("### 😊 Sentiment")
        if sentiment == "Positive":
            st.success(f"Positive ({score:.2f})")
        elif sentiment == "Negative":
            st.error(f"Negative ({score:.2f})")
        else:
            st.info(f"Neutral ({score:.2f})")

        # 🔥 CBT PATTERNS
        st.markdown("### 🧠 Thinking Patterns")
        if cbt_patterns:
            for item in cbt_patterns:
                st.warning(f"{item['pattern']}")
                st.caption(item['description'])
        else:
            st.success("Healthy thinking detected")

        # 🔥 RISK (ML PLACEHOLDER)
        st.markdown("### ⚠️ Relapse Risk")
        st.info("ML model will predict: Low / Medium / High")


# ---------------- MAIN DISPLAY ----------------
if selected_date in st.session_state.history:
    entry = st.session_state.history[selected_date]

    st.markdown("### 📖 Entry Confirmed")
    st.write(entry["text"])

    