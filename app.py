import streamlit as st
import pandas as pd
import pickle

# Load model
with open("model/heart_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Prediksi Penyakit Jantung")

# Input data dari user
def user_input():
    age = st.number_input("Umur", 20, 100)
    sex = st.selectbox("Jenis Kelamin", [0, 1])
    trestbps = st.number_input("Tekanan Darah (istirahat)")
    chol = st.number_input("Kolesterol")
    fbs = st.selectbox("Gula Darah > 120 mg/dl", [0, 1])
    restecg = st.selectbox("EKG istirahat", [0, 1, 2])
    thalach = st.number_input("Detak Jantung Maksimal")
    exang = st.selectbox("Angina akibat olahraga", [0, 1])
    oldpeak = st.number_input("ST depression", format="%.1f")
    slope = st.selectbox("Kemiringan ST", [0, 1, 2])
    ca = st.selectbox("Jumlah pembuluh utama (0–3)", [0, 1, 2, 3])
    
    data = {
        "age": age,
        "sex": sex,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca
    }
    return pd.DataFrame([data])

input_df = user_input()

# Prediksi
if st.button("Prediksi"):
    result = model.predict(input_df)[0]
    if result == 1:
        st.error("Potensi penyakit jantung terdeteksi!")
    else:
        st.success("Tidak terdeteksi penyakit jantung.")
