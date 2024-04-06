import streamlit as st
from joblib import load

loaded_model = load('regression.pkl')

def pred(features):
    prediction = loaded_model.predict([features])
    return prediction[0]

def main():
    st.title("Profit Predictor")

    rd_spend = st.number_input("R&D Spend: ")
    admin_spend = st.number_input("Admin spend: ")
    market_spend = st.number_input("Marketing spend: ")

    if st.button("Predict"):
        features = [rd_spend, admin_spend, market_spend]
        predicted_profit = pred(features)
        st.success(f"The predicted profit is {predicted_profit}")

if __name__ == '__main__':
    main()
