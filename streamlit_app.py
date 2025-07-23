import streamlit as st
import requests

st.title("🛡️ Real-Time Phishing URL Detector")

url = st.text_input("Enter a URL to check:")
if st.button("Check URL"):
    res = requests.post("http://localhost:5000/predict", json={"url": url})
    st.success(res.json().get("result"))
