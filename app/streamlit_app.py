import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Mental Health & Social Media Analyzer",
    page_icon=Image.open("../app/mental_health_logo.png"),
    layout="wide"
)

# Background
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4a5568 0%, #2d3748 100%);
    }
    .main-header {
        color: #ffffff;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        font-weight: 300;
    }
    .metric-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .footer {
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        color: #e2e8f0;
        border-top: 1px solid rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Load model and data
@st.cache_data
def load_data():
    model = pickle.load(open("../models/best_model.pkl", "rb"))
    scaler = pickle.load(open("../models/scaler.pkl", "rb"))
    df = pd.read_csv("../data/cleaned/merged_data.csv")
    return model, scaler, df

model, scaler, df = load_data()

TEMPLATE = "plotly_dark"
BG = "rgba(0,0,0,0.1)"
PAPER = "rgba(255,255,255,0.05)"

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select page:", [
    "Home", "Prediction", "Insights", "Chat"
])

# Home Page
if page == "Home":
    st.markdown('<h1 class="main-header">Social Media & Mental Health Analyzer</h1>', unsafe_allow_html=True)

    st.markdown("""
    ### Why does this matter?
    - Teens spend 7+ hours daily on social media
    - 1 in 5 show signs of depression or anxiety
    - Poor sleep and high stress are major triggers

    ### What you'll find here:
    - Analysis of social media's impact on mental health
    - Depression risk prediction from daily habits
    - Data-driven insights for better wellbeing
    """)

    st.success("👈 Use the sidebar to explore different sections.")

    # Footer
    st.markdown("""
    <div class='footer' style='position: fixed; bottom: 0; left: 0; right: 0;
    text-align: center; padding: 15px; font-size: 14px; z-index: 999;'>
        Mental Health Analyzer | Built by @Sujit |
        <a href='https://sujit-port-folio.netlify.app/' target='_blank' style='color:#e2e8f0;'>
        Connect With Me
        </a>
    </div>
    """, unsafe_allow_html=True)

# Prediction Page
elif page == "Prediction":
    st.markdown('<h1 class="main-header">Depression Risk Predictor</h1>', unsafe_allow_html=True)
    st.markdown("Answer these questions to assess your risk level.")

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 10, 30, 17)
        daily_hours = st.slider("Daily social media hours", 0.0, 12.0, 4.0)
        sleep_hours = st.slider("Sleep hours per night", 3.0, 10.0, 7.0)

    with col2:
        stress_level = st.slider("Stress level (1-10)", 1, 10, 5)
        anxiety_level = st.slider("Anxiety level (1-10)", 1, 10, 5)

    if st.button("Calculate Risk", type="primary"):
        # Calculate derived features
        screen_time = daily_hours * 0.3
        addiction_level = int(daily_hours)
        risk_score = round(stress_level*0.3 + anxiety_level*0.3 +
                    addiction_level*0.2 + daily_hours*0.1 +
                    (10 - sleep_hours)*0.1, 2)
        addiction_index = round(daily_hours*0.5 + screen_time*0.3 + addiction_level*0.2, 2)
        poor_sleep = 1 if sleep_hours < 6 else 0
        high_usage = 1 if daily_hours > 5 else 0

        # Model prediction
        input_data = np.array([[age, 0, daily_hours, sleep_hours, screen_time, 5.0,
        1.0, 1, stress_level, anxiety_level, addiction_level,
        risk_score, addiction_index, poor_sleep, high_usage]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        # Determine risk level
        if prediction == 1 or risk_score > 7:
            risk_level, color = "High Risk", "error"
        elif risk_score > 4:
            risk_level, color = "Medium Risk", "warning"
        else:
            risk_level, color = "Low Risk", "success"

        st.markdown("---")

        # Results
        if color == "error":
            st.error(f"### {risk_level}")
            st.markdown("""
            **Immediate actions needed:**
            - Limit social media to 2 hours maximum per day
            - Aim for 7-8 hours of quality sleep
            - Add 30 minutes of daily physical activity
            - Talk to a trusted friend or professional
            - Practice meditation or deep breathing
            """)
        elif color == "warning":
            st.warning(f"### {risk_level}")
            st.markdown("""
            **Make these improvements:**
            - Set daily screen time limits
            - Establish a better sleep routine
            - Stay physically active regularly
            """)
        else:
            st.success(f"### {risk_level}")
            st.markdown("""
            **Great job! Keep maintaining:**
            - Healthy sleep schedule
            - Regular physical activity
            - Balanced social media use
            """)

        # Metrics
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        col1.metric("Risk Score", f"{risk_score:.1f}", delta=None)
        col2.metric("Addiction Index", f"{addiction_index:.1f}", delta=None)
        col3.metric("Sleep Quality", "Good" if not poor_sleep else "Poor", delta=None)

        # Footer
    st.markdown("""
    <div class='footer' style='position: fixed; bottom: 0; left: 0; right: 0;
    text-align: center; padding: 15px; font-size: 14px; z-index: 999;'>
        Mental Health Analyzer | Built by @Sujit |
        <a href='https://sujit-port-folio.netlify.app/' target='_blank' style='color:#e2e8f0;'>
        Connect With Me
        </a>
    </div>
    """, unsafe_allow_html=True)

# Insights Page
elif page == "Insights":
    st.markdown('<h1 class="main-header">Data Insights</h1>', unsafe_allow_html=True)

    conn = sqlite3.connect("../data/database/mental_health.db")

    # Key metrics
    dep_pct = round(df['depression_label'].mean() * 100, 1)
    avg_sleep = round(df['sleep_hours'].mean(), 2)
    avg_usage = round(df['daily_social_media_hours'].mean(), 2)
    high_risk = pd.read_sql_query("SELECT COUNT(*) as c FROM merged_data WHERE risk_score > 7", conn)['c'][0]
    high_add = pd.read_sql_query("SELECT COUNT(*) as c FROM merged_data WHERE addiction_index > 6", conn)['c'][0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Depression Rate", f"{dep_pct}%")
    col2.metric("Avg Sleep", f"{avg_sleep} hrs")
    col3.metric("High Risk Users", high_risk)
    col4.metric("High Addiction", high_add)

    st.markdown("---")

    # Dataset preview
    st.subheader("Dataset Overview")
    st.dataframe(df.head(10), use_container_width=True, hide_index=True)
    st.write("This table provides a snapshot of the dataset used in the analysis. It includes key features such as age, social media usage, sleep patterns, screen time habits, academic performance, and physical activity levels. These variables help in understanding behavioral patterns and their potential impact on student well-being.")

    st.markdown("---")

    # High risk table
    st.subheader("Top High Risk Users")
    high_risk_df = pd.read_sql_query("""
        SELECT age, daily_social_media_hours as usage_hrs, sleep_hours,
            stress_level, anxiety_level, risk_score
        FROM merged_data WHERE risk_score > 7
        ORDER BY risk_score DESC LIMIT 10
    """, conn)
    st.dataframe(high_risk_df, use_container_width=True, hide_index=True)
    st.write("This table highlights users with the highest risk scores based on factors like social media usage, sleep duration, stress, and anxiety levels. It helps identify individuals who may require attention or intervention.")

    st.markdown("---")

    # Visualization
    st.subheader("Addiction vs Risk Correlation")
    fig = px.scatter(df, x='addiction_index', y='risk_score',
                    color=df['depression_label'].map({0:'No Depression', 1:'Depression'}),
                    color_discrete_map={'No Depression':'#60a5fa', 'Depression':'#ef4444'},
                    labels={'color': 'Mental Health Status'},
                    template=TEMPLATE, height=400)
    fig.update_layout(
        plot_bgcolor=BG, 
        paper_bgcolor=PAPER,
        font_color='#e2e8f0',
        margin=dict(t=30, b=20, l=20, r=20)
    )
    st.plotly_chart(fig, use_container_width=True)
    st.write("This scatter plot shows the relationship between addiction levels and risk scores. Each point represents a user, with colors indicating mental health status. A positive trend suggests that higher addiction is generally associated with increased risk.")

    st.markdown("---")

    st.subheader("Key Findings")
    st.markdown(f"""
    - Depressed users spend ~2 hours more daily on social media
    - Average sleep: 4.76 hrs (depressed) vs 6.49 hrs (healthy)
    - {high_risk} users need immediate attention (risk score > 7)
    - {high_add} users show severe social media addiction
    """)

    conn.close()

    # Footer
    st.markdown("""
    <div class='footer' style='position: fixed; bottom: 0; left: 0; right: 0;
    text-align: center; padding: 15px; font-size: 14px; z-index: 999;'>
        Mental Health Analyzer | Built by @Sujit |
        <a href='https://sujit-port-folio.netlify.app/' target='_blank' style='color:#e2e8f0;'>
        Connect With Me
        </a>
    </div>
    """, unsafe_allow_html=True)

# Chat Page
elif page == "Chat":
    st.sidebar.markdown("Ask about mental health, social media habits, or wellness tips")
    # st.markdown("""
    # <div style='text-align:center; padding: 40px 20px;'>
    #     <h1 class="main-header" style='margin: 10px 0;'>Mental Health Assistant</h1>
    #     <p style='color:#e2e8f0; font-size: 18px; margin: 20px 0;'>
    #     Ask about mental health, social media habits, or wellness tips
    #     </p>
    # </div>
    # """, unsafe_allow_html=True)

    components.iframe(
        "https://scizzor-bot-deploy.hf.space",
        height=600,
        scrolling=False
    )