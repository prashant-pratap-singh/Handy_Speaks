# import easyocr
# import pyttsx3
# import cv2
# import os

# # Paths
# image_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\he is pps.png"
# text_file_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\extracted_text.txt"

# def extract_text(image_path):
#     """Extracts text from a handwritten image using EasyOCR."""
#     img = cv2.imread(image_path)
#     if img is None:
#         raise ValueError(f"Error: Could not load image {image_path}")

#     reader = easyocr.Reader(['en'], gpu=False)  # Ensure it runs on CPU
#     result = reader.readtext(image_path)
    
#     extracted_text = "\n".join([entry[1] for entry in result])
#     return extracted_text

# def save_text(text, text_file_path):
#     """Saves extracted text to a .txt file."""
#     with open(text_file_path, "w", encoding="utf-8") as f:
#         f.write(text)

# def convert_text_to_speech(text):
#     """Converts text to speech using pyttsx3."""
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 180)  # Adjust speed (default ~200)
#     engine.setProperty('volume', 1.0)
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     # Extract text
#     text = extract_text(image_path)

#     if text.strip():
#         print("Extracted Text:\n", text)
        
#         # Save to file
#         save_text(text, text_file_path)

#         # Convert to speech
#         convert_text_to_speech(text)
#     else:
#         print("No text extracted.")





# import easyocr
# import cv2
# import pyttsx3

# # Define file paths
# image_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\he is pps.png"
# text_file_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\extracted_text.txt"

# def extract_text(image_path):
#     """Extract text from an image using EasyOCR."""
#     img = cv2.imread(image_path)
#     if img is None:
#         raise ValueError(f"Could not read image file: {image_path}")

#     reader = easyocr.Reader(['en'], gpu=False)  # Ensure it runs on CPU
#     result = reader.readtext(image_path)

#     # Join words properly in a single line
#     extracted_text = " ".join([entry[1] for entry in result])
#     return extracted_text

# def save_text_to_file(text, file_path):
#     """Save extracted text to a text file."""
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(text)

# def convert_text_to_speech(text):
#     """Convert text to speech using pyttsx3."""
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Adjust speech speed if needed
#     engine.setProperty('volume', 1.0)  # Set volume level
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     # Extract text from the image
#     extracted_text = extract_text(image_path)

#     if extracted_text.strip():
#         print("Extracted Text:\n", extracted_text)

#         # Save the text to a .txt file
#         save_text_to_file(extracted_text, text_file_path)

#         # Convert the extracted text to speech
#         convert_text_to_speech(extracted_text)
#     else:
#         print("No text extracted from the image.")



import easyocr
import cv2
import pyttsx3
import os
import tempfile

# Define file paths
image_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\he is pps.png"
text_file_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\extracted_text.txt"

def extract_text(image_path):
    """Extract text from an image using EasyOCR."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image file: {image_path}")

    reader = easyocr.Reader(['en'], gpu=False)  # Ensure it runs on CPU
    result = reader.readtext(image_path)

    # Join words properly in a single line
    extracted_text = " ".join([entry[1] for entry in result])
    return extracted_text

def save_text_to_file(text, file_path):
    """Save extracted text to a text file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def convert_text_to_speech(text, output_audio_path):
    """Convert text to speech and save as a file."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speech speed if needed
    engine.setProperty('volume', 1.0)  # Set volume level

    # Save speech to a file instead of playing directly
    engine.save_to_file(text, output_audio_path)
    engine.runAndWait()

if __name__ == "__main__":
    try:
        # Extract text from the image
        extracted_text = extract_text(image_path)

        if extracted_text.strip():
            print("Extracted Text:\n", extracted_text)

            # Save the text to a .txt file
            save_text_to_file(extracted_text, text_file_path)

            # Generate a temporary audio file
            temp_audio_path = os.path.join(tempfile.gettempdir(), "extracted_audio.mp3")
            convert_text_to_speech(extracted_text, temp_audio_path)

            print(f"Audio saved at: {temp_audio_path}")

            # Open the saved audio file (for local playback)
            os.system(f'start {temp_audio_path}')  # Works on Windows

        else:
            print("No text extracted from the image.")

    except Exception as e:
        print(f"Error: {e}")
