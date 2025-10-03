import streamlit as st
import pickle

def show_prediction_page():
    st.title("🩺 Disease Prediction")

    st.write("Enter your symptoms below (comma separated):")
    symptoms = st.text_input("Symptoms:")

    if st.button("Predict Disease"):
        if symptoms.strip():
            # Load model
            with open("SVC.pickle", "rb") as file:
                model = pickle.load(file)

            # For now just a placeholder
            st.success("✅ Prediction completed (replace with actual model logic)")
        else:
            st.warning("⚠️ Please enter symptoms before predicting.")
