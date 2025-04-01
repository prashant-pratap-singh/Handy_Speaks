import pytesseract as pyt
import cv2
import os
from gtts import gTTS
import pygame

# Set Tesseract-OCR path
pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image
image_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\he is pps.png"
img = cv2.imread(image_path)

# Check if image is loaded properly
if img is None:
    print("Error: Image not found or unable to load. Check file path.")
    exit()

# Convert image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract text from image
text = pyt.image_to_string(img)

# Print extracted text
print("Extracted Text:\n", text)

# Save extracted text to a .txt file
save_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\extracted_text.txt"
with open(save_path, "w", encoding="utf-8") as file:
    file.write(text)

print(f"Text saved to {save_path}")

# Convert extracted text to speech
if text.strip():  # Check if text is not empty
    tts = gTTS(text, lang="en")
    audio_path = "speech_output.mp3"
    tts.save(audio_path)

    # Initialize pygame mixer and play the audio
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    print("Playing AI-generated speech...")

    # Wait until audio finishes playing
    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()
    pygame.quit()

    # Delete the audio file after playing (optional)
    os.remove(audio_path)
else:
    print("No text found in the image.")
