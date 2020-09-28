from backend import get_embedding
from backend import verify_identity

import os

import streamlit as st
from logzero import logger

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
st.title("Speaker Verification")
st.set_option("deprecation.showfileUploaderEncoding", False)


database = {}
THRESHOLD = 0.7

menu_option = st.sidebar.radio("Menu", ["Enroll user", "Test user"])

if menu_option == "Enroll user":
    st.subheader(
        "Enroll a new user by entering their name and upload a short audio file of speech."
    )
    username = st.text_input("User name", "")
    audio_file = st.file_uploader(
        "Upload a short wav or flac file", type=(["wav", "flac"])
    )
    st.audio(audio_file)
    if username != "" and audio_file is not None:
        if st.button("Enroll"):
            with st.spinner("Extracting embedding..."):
                embedding = get_embedding(audio_file)
                database["username"] = embedding
            st.success("Embedding extracted successfully")

else:
    st.subheader(
        "Verify your identity by typing in your name and uploading a short audio file of speech (different from the one used for enrolling."
    )
    username = st.text_input("User name", "")
    audio_file = st.file_uploader(
        "Upload a short wav or flac file", type=(["wav", "flac"])
    )
    st.audio(audio_file)
    if username != "" and audio_file is not None:
        if st.button("Verify"):
            with st.spinner("Verifiying identity"):
                result = verify_identity(database, audio_file, username, THRESHOLD)
            if result:
                st.success("Identity verified successfully")
            else:
                st.error("Identity not verified")
