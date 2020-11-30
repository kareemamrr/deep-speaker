from st_backend import Model
import os
import io
import soundfile as sf
import streamlit as st


def decode_bytes(audio_bytes):
    signal, sr = sf.read(io.BytesIO(audio_bytes))


def store_bytes_as_wav(audio_bytes, name):
    with open(f'uploads/{name}.wav', mode='bx') as f:
        f.write(audio_bytes)
    return f'uploads/{name}.wav'


def remove_file(path):
    os.remove(path)


def audio_widget(key):
    username = st.text_input('Username', value="", key=key)
    uploaded_file = st.file_uploader("Choose an audio file", key=key)

    if uploaded_file is not None and len(username) > 0:
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format='audio/wav')

        if st.button(key):
            audio_path = store_bytes_as_wav(audio_bytes, username)
            if key == "Enroll":
                Model.enroll(audio_path, username)
            elif key == "Verify":
                st.write(Model.verify(audio_path, username))

            remove_file(audio_path)


def main():
    st.title('Speaker Verification')
    enroll_menu = st.beta_expander("Enroll user", expanded=True)
    verify_menu = st.beta_expander("Verify user", expanded=False)

    with enroll_menu:
        audio_widget("Enroll")
    with verify_menu:
        audio_widget("Verify")


if __name__ == '__main__':
    model = Model()
    main()
