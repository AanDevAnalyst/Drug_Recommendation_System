import streamlit as st

def show_info_page():
    st.title("📘 Info & Help")
    st.markdown("""
    👉 **How to Use the App:**
    1. Go to **Prediction Page**
    2. Enter your symptoms (comma separated)
    3. Click **Predict Disease**
    4. View results (Precautions, Medications, Diets, Workouts)

    ⚠️ **Disclaimer:** This tool is for educational purposes only and does not replace professional medical advice.
    """)
