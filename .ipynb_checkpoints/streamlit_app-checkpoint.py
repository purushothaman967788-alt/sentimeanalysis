import streamlit as st
import requests

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon=" 🎬",
    layout="centered"
)
st.title("Product Review Sentime Analysis")
st.title("Enter a product review and get instand sentime prediction")

review = st.text_area("Enter your product review here:", height=150)

if st.button("Analyze sentime"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post(
                "http://127.0.0.1:5000.prodict",
                json={"review": review}
            )
            result = response.json()
        sentiment = result['prediction']
        
    if "positive" in sentiment or "negative" in sentiment:
        st.success(f"Sentiment : {sentiment}")
    else:
        st.error(f"Sentiment : {sentiment}")