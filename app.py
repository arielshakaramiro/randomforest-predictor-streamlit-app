import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Custom CSS HUD Futuristic
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron&display=swap');

        html, body, [class*="css"] {
            background-color: #0C3B5D;
            color: #00FFFF;
            font-family: 'Orbitron', sans-serif;
        }

        .stButton>button {
            background-color: #00FFFF;
            color: #0C3B5D;
            border: none;
            padding: 0.6em 1.2em;
            border-radius: 10px;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background-color: #008B8B;
            color: white;
        }

        .block-container {
            padding-top: 2rem;
        }

        .stSlider > div {
            color: #00FFFF;
        }

        .stTitle {
            color: #00FFFF;
        }

        .stMarkdown h1, .stMarkdown h2 {
            color: #00FFFF;
        }

    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
with open("models/random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Layout & UI
st.title("🔮 AI Customer Predictor")
st.subheader("Futuristic HUD Dashboard")

col1, col2 = st.columns(2)

with col1:
    usia = st.slider("🧑 Usia", 18, 65, 30)

with col2:
    pendapatan = st.slider("💰 Pendapatan (USD)", 1000, 15000, 5000)

# Predict
if st.button("🔍 Prediksi Pembelian"):
    x_input = np.array([[usia, pendapatan]])
    prediction = model.predict(x_input)[0]

    st.markdown("---")
    if prediction == 1:
        st.success("✅ **Prediksi: Pelanggan kemungkinan akan membeli.**")
    else:
        st.warning("❌ **Prediksi: Pelanggan kemungkinan tidak membeli.**")

# Footer
st.markdown("""
    <hr style="border: 1px solid #00FFFF;">
    <center>
        <small>🚀 Developed with ❤️ using Streamlit | Theme: HUD Futuristic</small>
    </center>
""", unsafe_allow_html=True)
