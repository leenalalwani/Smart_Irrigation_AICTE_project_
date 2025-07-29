import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("Farm_Irrigation_System.pkl")

# Custom CSS styling
st.markdown("""
    <style>
    * {
        font-family: 'Times New Roman', Times, serif !important;
    }
    body {
        background-color: #d4edda;
    }
    .block-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
        color: black;
    }
    h1, h2, h3 {
        color: black !important;
        text-align: center;
    }
    label, .stSlider label, .stMarkdown p {
        color: black !important;
    }
    .stSlider > div[data-baseweb="slider"] > div {
        background: #90ee90;
        height: 10px;
        border-radius: 5px;
    }
    .stSlider > div[data-baseweb="slider"] > div > div {
        background: #008000;
    }
    .center-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .center-output {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .custom-box {
        border: 2px solid #28a745;
        padding: 10px 20px;
        margin: 5px 0;
        border-radius: 8px;
        background-color: #eafaf1;
        color: black;
        width: fit-content;
        text-align: center;
    }
    .stButton>button {
        background-color: #28a745;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 0.5em 1em;
        font-family: 'Times New Roman', Times, serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle (centered)
st.markdown("<h1> Smart Sprinkler System </h1>", unsafe_allow_html=True)
st.markdown("<h3>🌱 Scaled Sensor Inputs (0 to 1)</h3>", unsafe_allow_html=True)

# Layout for sliders
sensor_values = []
cols = st.columns(2)
for i in range(20):
    with cols[i % 2]:
        val = st.slider(
            f"Sensor {i}",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.01,
            key=f"sensor_{i}"
        )
        sensor_values.append(val)

# Predict Button centered
st.markdown('<div class="center-button">', unsafe_allow_html=True)
predict_clicked = st.button("💧 Predict Sprinklers")
st.markdown('</div>', unsafe_allow_html=True)

# Prediction Output (centered with black text)
if predict_clicked:
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown('<div class="center-output">', unsafe_allow_html=True)
    st.markdown("<h2>🌿 Sprinkler Status</h2>", unsafe_allow_html=True)
    for i, status in enumerate(prediction):
        st.markdown(
            f"<div class='custom-box'>Sprinkler {i} (parcel_{i}): {'💡 ON' if status == 1 else '❌ OFF'}</div>",
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)
