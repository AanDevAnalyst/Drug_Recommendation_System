import streamlit as st
from pages.prediction import show_prediction_page
from pages.Developer import show_developer_page
from pages.info import show_info_page  

# --- App Config ---
st.set_page_config(page_title="AI Disease Prediction App", page_icon="🧬", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🧬 Disease Prediction App")
page = st.sidebar.radio(
    "📌 Navigate",
    ["🏠 Home", "🔍 Prediction", "👨‍💻 Developer", "ℹ️ Info"]
)

# --- Page Routing ---
if page == "🏠 Home":
    st.title("🏥 Welcome To AI Disease Prediction App")
    st.markdown("""
    This **AI-powered system** predicts possible **diseases** based on symptoms  
    and provides recommendations such as **precautions, medications, diets, and workouts**.  
    
    🔍 Go to **Prediction Page** to try it out.  
    👨‍💻 Learn more about the creator in the **Developer Page**.  
    📘 Visit the **Info Page** for extra guidance.
    """)
    st.image("https://img.icons8.com/color/452/hospital-room.png", width=280)

elif page == "🔍 Prediction":
    show_prediction_page()

elif page == "👨‍💻 Developer":
    show_developer_page()

elif page == "ℹ️ Info":
    show_info_page()

# --- Footer ---
st.markdown(
    "<div style='text-align: center; margin-top: 40px; font-size: 14px;'>"
    "🚀 Built with ❤️ using <b>Streamlit</b> | © 2025 <b>Medical AI Project</b>"
    "</div>",
    unsafe_allow_html=True
)
