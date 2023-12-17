import tensorflow as tf
import streamlit as st


# Translator = tf.saved_model.load('./translator/content/translator')
# # Translator('Eu amo programar em Python.').numpy()



# def translate_text(text, Translator):
#     translated_text = Translator(text).numpy()
#     return translated_text

def translate_text(text):
    return "This is translated english sentence"

# Streamlit app
st.title("Text Translator - Portuguese to English")

# Text input for user input
user_input = st.text_area("Enter text in Portuguese:", "")

if st.button("Translate"):
    if user_input:
        translated_text = translate_text(user_input)
        st.write("<p style='font-size: 18px;'><strong>Translated text (English):</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 16px;'>{translated_text}</p>", unsafe_allow_html=True)
    else:
        st.warning("Please enter some text in Portuguese to translate.")
