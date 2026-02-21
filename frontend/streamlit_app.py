import streamlit as st
import requests



st.set_page_config(
    page_title="Clinical Risk Intelligence Platform",
    layout="wide",
    page_icon="🧠"
)



st.markdown("""
<style>
/* Gradient Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #f1f5f9;
}

/* Section Spacing */
.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
}

/* Glass Card */
.glass-card {
    background: rgba(255, 255, 255, 0.06);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    transition: 0.3s;
}

.glass-card:hover {
    transform: translateY(-5px);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #3b82f6);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 17px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #3b82f6, #6366f1);
}

/* Metric Glow */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# HEADER SECTION

st.markdown("""
# 🧠 Clinical Risk Intelligence Platform  
### 🩺 Diabetes Risk Stratification & Predictive Analytics
""")

st.markdown("""
Harnessing ensemble machine learning to deliver early-stage diabetes risk probability 
based on clinical biomarkers and lifestyle indicators.

Built using validated modeling, cross-validation stability testing, 
and calibrated threshold optimization for practical deployment.
""")

st.divider()



col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass-card">
    <h3>🧩 Model Architecture</h3>
    Random Forest (300 Trees)<br>
    Max Depth: 20<br>
    Hyperparameter Optimized
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
    <h3>📊 Validation Strategy</h3>
    5-Fold Cross Validation<br>
    ROC Optimization<br>
    Threshold Calibration (0.25)
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-card">
    <h3>📈 Performance Metrics</h3>
    ROC-AUC: 0.97<br>
    Recall: 76%<br>
    Precision: 79%
    </div>
    """, unsafe_allow_html=True)

st.divider()

# SIDEBAR INPUTS


st.sidebar.header("📝 Patient Clinical Profile")

age = st.sidebar.slider("🎂 Age", 0, 100, 40)
bmi = st.sidebar.slider("⚖ Body Mass Index", 10.0, 60.0, 25.0)
glucose = st.sidebar.slider("🧪 Blood Glucose Level", 70, 300, 120)
hba1c = st.sidebar.slider("🩸 HbA1c Level", 3.0, 10.0, 5.5)

hypertension = st.sidebar.selectbox("💓 Hypertension", ["No", "Yes"])
heart_disease = st.sidebar.selectbox("❤️ Heart Disease", ["No", "Yes"])
gender = st.sidebar.selectbox("👤 Gender", ["Female", "Male"])
smoking = st.sidebar.selectbox(
    "🚬 Smoking History",
    ["never", "former", "current", "not current", "ever"]
)

hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0

st.sidebar.markdown("---")
st.sidebar.markdown("🎯 Decision Threshold: **0.25**")


# PREDICTION BUTTON

if st.button("🚀 Generate Risk Assessment"):

    payload = {
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "bmi": bmi,
        "HbA1c_level": hba1c,
        "blood_glucose_level": glucose,
        "gender_Male": 1 if gender == "Male" else 0,
        "smoking_history_current": 1 if smoking == "current" else 0,
        "smoking_history_ever": 1 if smoking == "ever" else 0,
        "smoking_history_former": 1 if smoking == "former" else 0,
        "smoking_history_never": 1 if smoking == "never" else 0,
        "smoking_history_not_current": 1 if smoking == "not current" else 0,
    }

    response = requests.post(
        "https://diabetes-risk-prediction-shm2.onrender.com/predict",
        json=payload
    )

    if response.status_code == 200:

        result = response.json()
        probability = result["probability"]

        st.divider()
        st.markdown("## 📊 Risk Assessment Dashboard")

        colA, colB = st.columns(2)

        with colA:
            st.metric(
                "📌 Predicted Probability",
                f"{probability*100:.2f}%"
            )
            st.progress(probability)

        with colB:
            if probability >= 0.5:
                st.error("🔴 High Risk Category")
                interpretation = "Immediate clinical consultation recommended."
            elif probability >= 0.25:
                st.warning("🟠 Moderate Risk Category")
                interpretation = "Periodic monitoring and lifestyle adjustment advised."
            else:
                st.success("🟢 Low Risk Category")
                interpretation = "Current risk appears stable."

            st.markdown(f"**🧾 Clinical Interpretation:** {interpretation}")

    else:
        st.error(f"Backend Error: {response.text}")

st.divider()

st.markdown("""
### 🛠 Development Pipeline
EDA → Feature Engineering → Baseline Modeling → Hyperparameter Optimization → Threshold Calibration → API Deployment → UI Integration

---

⚠ This system is for demonstration and research purposes only.
""")