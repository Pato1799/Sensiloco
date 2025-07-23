import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title("SensiLoco")

texto = st.text_area("Introducir texto:")

if st.button("Reproducir"):
    if texto.strip() == "":
        st.warning("Debes escribir algo para escucharlo")
    else:
        tts = gTTS(text=texto, lang='es')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        st.audio(audio_bytes.getvalue(), format='audio/mp3')
        st.success("¡Listo!")
