import streamlit as st
import datetime
from modules.preprocessing import preprocess
from modules.sentiment import get_sentiment
from modules.distortion import detect_cbt_patterns
from modules.model import predict_risk

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
        cbt_score = sum(item.get("matches",0) for item in cbt_patterns)
        features = [score, cbt_score]
        risk_num = predict_risk(features)
        mapping = {0: "Low", 1: "Medium", 2: "High"}
        risk = mapping[risk_num]
        #ML (FUTURE)
        # 👉 Replace this later with:
        # from modules.model import predict_risk
        # risk = predict_risk([score, cbt_score])
       

        st.session_state.history[selected_date] = {
            "text": text,
            "risk": risk
        }
        # 🔥 CHECK LAST 2 DAYS HIGH RISK
        dates = sorted(st.session_state.history.keys())

        if len(dates) >= 2:
            last_date = dates[-1]
            prev_date = dates[-2]

            last_risk = st.session_state.history[last_date]["risk"]
            prev_risk = st.session_state.history[prev_date]["risk"]

            if last_risk == "High" and prev_risk == "High":
                st.markdown("""
                    <style>
                    @keyframes slideDownFade {
                        from { top: -50px; opacity: 0; }
                        to { top: 30px; opacity: 1; }
                    }
                    .custom-risk-alert {
                        position: fixed;
                        top: 30px;
                        left: 50%;
                        transform: translateX(-50%);
                        background: rgba(255, 75, 75, 0.95);
                        backdrop-filter: blur(10px);
                        -webkit-backdrop-filter: blur(10px);
                        color: white !important;
                        padding: 18px 30px;
                        border-radius: 16px;
                        font-weight: 600;
                        font-family: 'Poppins', sans-serif;
                        font-size: 16px;
                        z-index: 999999;
                        box-shadow: 0 8px 32px rgba(255, 75, 75, 0.4);
                        border: 1px solid rgba(255, 255, 255, 0.2);
                        display: flex;
                        align-items: center;
                        gap: 14px;
                        animation: slideDownFade 0.6s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
                    }
                    .custom-risk-alert span:nth-child(1) {
                        font-size: 24px;
                    }
                    </style>
                    <div class="custom-risk-alert">
                        <span>⚠️</span>
                        <span>High risk detected for consecutive days. Please consider contacting a doctor.</span>
                    </div>
                """, unsafe_allow_html=True)

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
        if cbt_patterns[0]["pattern"] != "Healthy thinking":
            for item in cbt_patterns:
                st.warning(f"{item['pattern']}")
                st.caption(item['description'])
        else:
            st.success("Healthy thinking detected")

        st.markdown("### ⚠️ Risk Level")
        if risk == "High":
            st.error("🔴 High Risk")
        elif risk == "Medium":
            st.warning("🟡 Medium Risk")
        else:
            st.success("🟢 Low Risk")


# ---------------- MAIN DISPLAY ----------------
if selected_date in st.session_state.history:
    entry = st.session_state.history[selected_date]

    st.markdown("### 📖 Entry Confirmed")
    st.write(entry["text"])

    