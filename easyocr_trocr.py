import os
import cv2
import easyocr
import pyttsx3
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

# Set paths
input_folder = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\handwritten_notes"
output_folder = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\converted_text"

# Load TrOCR model
trocr_processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
trocr_model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Initialize EasyOCR
easyocr_reader = easyocr.Reader(['en'])

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # Set speech speed
tts_engine.setProperty('volume', 1.0)  # Set volume

def extract_text_trocr(image_path):
    """Extract text using TrOCR."""
    image = Image.open(image_path).convert("RGB")
    pixel_values = trocr_processor(images=image, return_tensors="pt").pixel_values
    generated_ids = trocr_model.generate(pixel_values)
    return trocr_processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

def extract_text_easyocr(image_path):
    """Extract text using EasyOCR."""
    result = easyocr_reader.readtext(image_path)
    return "\n".join([entry[1] for entry in result])

def process_images():
    """Process all images in the input folder and save extracted text."""
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.lower().endswith(('.jpg', '.png')):
            image_path = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".txt")

            if os.path.exists(output_file):
                print(f"Skipping '{file}' (already processed).")
                continue

            try:
                text_trocr = extract_text_trocr(image_path)
                text_easyocr = extract_text_easyocr(image_path)

                final_text = text_trocr if text_trocr.strip() else text_easyocr

                if final_text.strip():
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(final_text)

                    print(f"Converted '{file}' to '{output_file}'")
                    convert_text_to_speech(final_text)
                else:
                    print(f"No text extracted from '{file}'")

            except Exception as e:
                print(f"Failed to process '{file}': {e}")

def convert_text_to_speech(text):
    """Convert extracted text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

if __name__ == "__main__":
    process_images()
    print("Processing complete.")
