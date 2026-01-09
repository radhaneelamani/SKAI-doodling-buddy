import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Skai", layout="centered")

st.title("Skai")
st.caption("Your sketching AI companion for sketching")

uploaded_file = st.file_uploader(
    "Upload an image of your sketch", 
    type=["png", "jpg", "jpeg"]
    )

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption= "Your Sketch", use_column_width=True)

    if st.button("Ask Skai"):
        with st.spinner("Skai is thinking..."):
            response = requests.post(
                "http://localhost:8000/analyze",
                files={"file": uploaded_file.getvalue()
                       })
            if response.status_code == 200:
                data = response.json()
                st.success(f"Skai says: {data['comment']}")
            else:
                st.error("Skai could not process your sketch. Please try again.")
