import streamlit as st
from PIL import Image
from ai_engine.py import AIEngine

st.set_page_config(layout="wide")

st.title("🏢 Fundbüro AI System")

engine = AIEngine()

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.user = username
            st.rerun()

        else:
            st.error("Login Fehler")

    st.stop()

uploaded = st.file_uploader(
    "Bild hochladen",
    type=["jpg","jpeg","png"]
)

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    result = engine.predict(image)

    st.image(image, width=400)

    st.success(result["label"])

    st.info(
        f"Confidence: {round(result['confidence']*100,2)}%"
    )
