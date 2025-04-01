import pyttsx3

# Path to the extracted text file
file_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\extracted_text.txt"

# Read the text from the file
try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().strip()

    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Set voice properties (Optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Speak the extracted text
    print("Speaking extracted text...")
    engine.say(text)
    engine.runAndWait()

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"Error: {e}")
