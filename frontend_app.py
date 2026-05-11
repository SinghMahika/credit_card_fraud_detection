import streamlit as st
import requests
import pandas as pd

st.title("Fraud Detection System")
st.write(
    "Upload transaction dataset to check "
    "whether transactions are fraudulent."
)
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Transactions")
    st.dataframe(df.head())

    uploaded_file.seek(0)

    files = {
        "file": uploaded_file.getvalue()
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        files=files
    )

    result = response.json()

    predictions = result["predictions"]

    st.subheader("Prediction Results")

    for i, pred in enumerate(predictions):

        if pred == "Fraud":
            st.error(
                f"Transaction {i+1}: FRAUD DETECTED"
            )

        else:
            st.success(
                f"Transaction {i+1}: Not Fraudulent"
            )