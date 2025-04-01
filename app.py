# import streamlit as st
# import easyocr
# import pyttsx3
# import cv2
# import os
# from PIL import Image
# import numpy as np

# def extract_text(image_path):
#     reader = easyocr.Reader(['en'], gpu=False)
#     result = reader.readtext(image_path)
#     extracted_text = " ".join([entry[1] for entry in result])
#     return extracted_text

# def save_text(text, output_file):
#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write(text)

# def convert_text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     engine.setProperty('volume', 1.0)
#     engine.say(text)
#     engine.runAndWait()

# st.title("Handwriting Recognition and Text-to-Speech")
# st.write("Upload a handwritten image, extract text, and listen to it!")

# uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)
    
#     image_path = "temp_image.png"
#     image.save(image_path)
    
#     if st.button("Extract Text"):
#         with st.spinner("Extracting text..."):
#             extracted_text = extract_text(image_path)
#             save_text(extracted_text, "extracted_text.txt")
#             st.text_area("Extracted Text", extracted_text, height=150)
            
#             if st.button("Play Audio"):
#                 convert_text_to_speech(extracted_text)
    
#     os.remove(image_path)





import streamlit as st
import easyocr
import pyttsx3
import cv2
import os
from PIL import Image
import numpy as np

def extract_text(image_path):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image_path)
    extracted_text = " ".join([entry[1] for entry in result])
    return extracted_text

def save_text(text, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

def convert_text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

st.title("Handwriting Recognition and Text-to-Speech")
st.write("Upload a handwritten image, extract text, and listen to it!")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    image_path = "temp_image.png"
    image.save(image_path)
    
    if st.button("Extract Text"):
        with st.spinner("Extracting text..."):
            extracted_text = extract_text(image_path)
            save_text(extracted_text, "extracted_text.txt")
            st.text_area("Extracted Text", extracted_text, height=150)
            
            if st.button("Play Audio"):
                convert_text_to_speech(extracted_text)
    
    os.remove(image_path)  

