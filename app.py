import streamlit as st  # pyright: ignore[reportMissingImports]
import joblib
import numpy as np

model = joblib.load("model.pkl")

# Page Title
st.set_page_config(page_title="🏠 House Price Predictor", layout="wide")
st.title("🏠 House Price Predictor")
st.subheader("Predict your home's price based on its features! 💰")

# Background styling (optional)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }
    </style>
    """, unsafe_allow_html=True
)

st.divider()

# Info section
with st.expander("ℹ️ About this App"):
    st.write("""
        This app uses a machine learning model trained on house data to predict prices. 
        Enter the features of your house below and click Predict! 🏡
    """)
st.divider()

# Input Columns
col1, col2 = st.columns(2)

bedrooms = col1.number_input("🛏 Number of bedrooms",min_value=0, value=0 )
bathrooms = col2.number_input("🛁 Number of bathrooms",min_value=0, value=0 )
livingarea = st.number_input("📏 Living area (sqft)",min_value=0, value=0)

# Condition Dropdown
condition_options = {
    "Very Bad": 1,
    "Bad": 2,
    "Neutral": 3,
    "Good": 4,
    "Very Good": 5
}
condition_text = st.selectbox("🏚 Condition of House", list(condition_options.keys()))
condition = condition_options[condition_text]

numberofschools = st.slider("🏫 Number of schools nearby", 0, 10, 2)

st.divider()

# Prepare input array
X = np.array([[bedrooms, bathrooms, livingarea, condition, numberofschools]], dtype=float)

# Predict button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Predict 🏠"):
        # Optional: Apply scaler if used during training
        # X_scaled = scaler.transform(X)
        prediction = model.predict(X)
        st.success(f"Predicted House Price: 💵 {prediction[0]:,.2f}")
        st.balloons()

# Optional: Display input values for debugging
with st.expander("🔍 Input Details"):
    st.write({
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Living Area": livingarea,
        "Condition": condition_text,
        "Schools Nearby": numberofschools
    })