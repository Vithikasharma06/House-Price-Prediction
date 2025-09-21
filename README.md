# 🏠 House Price Prediction App

A simple and interactive **Streamlit** app that predicts house prices based on user-provided features like bedrooms, bathrooms, living area, house condition, and nearby schools. Enter your values and get an instant AI-powered estimate.

---

## 💡 Description

This app allows users to input key features of a house:

- Number of bedrooms 🛏  
- Number of bathrooms 🛁  
- Living area in square feet 📏  
- Condition of the house 🏚 (Very Bad → Very Good)  
- Number of schools nearby 🏫  

It then predicts the estimated **house price** using a trained machine learning model (`model.pkl`). The UI is clean and user-friendly, making it easy for anyone to quickly estimate property values.

---

## 🚀 Features

- Interactive web app using **Streamlit**  
- Number input fields for user-provided features  
- Selectbox to choose house condition (mapped to numeric value for the model)  
- Real-time house price prediction  
- Clean layout with columns, dividers, and emojis  
- Expander sections for app info and input details  
- Balloons animation upon prediction 🎉  

---
## 🧰 Technology Stack
- Python 3.13
- Streamlit – Web app framework
- NumPy – Numerical computations
- Joblib – Model serialization
- Scikit-learn – Machine learning library

  
---

## 📄 How to Use
- Enter the number of bedrooms, bathrooms, and living area.
- Select the condition of the house from the dropdown.
- Enter the number of schools nearby.
- Click Predict to see the estimated house price.
- Expand the Input Details section to review your entries.


---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor

2. Install required Python packages
pip install streamlit numpy joblib scikit-learn





