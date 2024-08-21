from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import streamlit as st

st.sidebar.title("Links")
apikey = st.sidebar.text_input("api-key")
url = st.sidebar.text_input("url")

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

st.title("Language Translator")

text_to_translate = st.text_area("Enter the word to translate")
source_language = st.selectbox('Language', ["en", "ar", "zh", "fr", "de", "it", "ja", "ko", "pt", "ru", "es", "hi"])
target_language = st.selectbox('Language to translate into', ["en", "ar", "zh", "fr", "de", "it", "ja", "ko", "pt", "ru", "es", "hi"])

if st.button("Translate"):
    translation = language_translator.translate(
        text=text_to_translate,
        model_id=f'{source_language}-{target_language}'
    ).get_result()
    
    translated_text_content = translation['translations'][0]['translation']

    st.write(f"Translated text: {translated_text_content}")
