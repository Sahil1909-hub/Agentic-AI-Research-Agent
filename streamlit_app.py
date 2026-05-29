import requests
import streamlit as st

st.set_page_config(
    page_title="AI Research Agent",
    layout="wide"
)

st.title("Agentic AI Research Agent")

uploaded_file = st.file_uploader(label="Upload your PDF", type=["pdf"])

if uploaded_file:
    
    files = {
        "file": uploaded_file
    }

    upload_response = requests.post(
        "http://localhost:8000/upload-pdf",
        files=files
    )

    st.success("PDF Uploaded Succesfully")

query = st.text_input("Enter Research Query")

if st.button("Research"):

    response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"question": query}
)


    print(response.status_code)
    print(response.text)

    if response.status_code == 200:

        result = response.json()

        st.write(result)

    else:
        st.error(f"Error: {response.text}")