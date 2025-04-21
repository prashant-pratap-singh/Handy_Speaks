# Handy_Speaks

Handy_Speaks is an application designed to convert handwritten text from images into speech. It allows users to upload images containing handwritten notes, extract the text using OCR (Optical Character Recognition), listen to the spoken version of the text, and download the extracted text for later use.

---

## Features

- Upload handwritten images in PNG, JPG, or JPEG formats.
- Extract text from handwritten images using EasyOCR and Microsoft TrOCR models.
- Convert extracted text to speech using `pyttsx3` or Google Text-to-Speech (gTTS).
- Download extracted text as a `.txt` file.
- Play audio of the extracted text directly within the app.
- Batch process handwritten notes from a folder and save converted text files.
- Cross-platform support (Windows tested).

---

## Installation

1. Clone the repository:

   ```bash
   git clone 
   cd Handy_Speaks
   ```

2. Create and activate a Python virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Required libraries include:

   - `streamlit`
   - `easyocr`
   - `pyttsx3`
   - `opencv-python`
   - `Pillow`
   - `transformers`
   - `torch`
   - `gTTS`
   - `pygame`

4. For Tesseract OCR (used in some scripts), install Tesseract-OCR engine:

   - Windows: Download and install from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
   - Set the path in your scripts if needed (e.g., `pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`).

---

## Usage

### Streamlit Web App (`app.py`)

Run the Streamlit app to interactively upload handwritten images, extract text, and listen to speech:

```bash
streamlit run app.py
```

- Upload an image file.
- Click **Extract Text** to perform OCR.
- View extracted text in the text area.
- Click **Play Audio** to listen to the text-to-speech conversion.
- The extracted text is saved to `extracted_text.txt`.

### Batch Processing with TrOCR and EasyOCR (`easyocr_trocr.py`)

Process all handwritten images in a folder and save extracted text files:

- Set your input folder path (containing images) and output folder path in the script.
- Run the script:

```bash
python easyocr_trocr.py
```

The script uses Microsoft’s TrOCR model first and falls back to EasyOCR if needed. It also converts the text to speech.

### Command Line OCR and TTS (`easyyy.py`)

Extract text from a single image and save both text and audio files:

```bash
python easyyy.py
```

Modify the image and text file paths inside the script as needed.

### Integrated OCR and TTS with Tesseract and gTTS (`integrated_code.py`)

Extract text using Tesseract OCR and convert it to speech using Google Text-to-Speech:

```bash
python integrated_code.py
```

Make sure Tesseract is installed and the path is set correctly.

---

## Project Structure

| File                | Description                                                  |
|---------------------|--------------------------------------------------------------|
| `app.py`            | Streamlit web app for interactive handwriting to speech.    |
| `easyocr_trocr.py`  | Batch processing using TrOCR and EasyOCR with TTS.           |
| `easyyy.py`         | Command line script for OCR and TTS using EasyOCR and pyttsx3.|
| `integrated_code.py` | OCR with Tesseract and TTS using gTTS and pygame.            |
| `texttospeech.py`   | Simple script to read text from file and convert to speech.  |
| `README.md`         | This documentation file.                                      |
| `extracted_text.txt`| Sample output text file.                                      |

---

## Dependencies and Requirements

- Python 3.7 or higher
- Streamlit
- EasyOCR
- PyTTSx3
- OpenCV
- Pillow
- Transformers (for TrOCR)
- Torch
- gTTS and pygame (for integrated_code.py)
- Tesseract OCR engine (for pytesseract scripts)

---

## Notes

- The app currently supports English language handwriting.
- For best OCR results, use clear and well-lit images of handwriting.
- The text-to-speech engine speed and volume can be adjusted in the scripts.
- Temporary files like images and audio are cleaned up after processing.
- Windows users may need to adjust file paths and commands accordingly.

---

## License

Specify your license here (e.g., MIT License).

---

## Contact

For issues or feature requests, please open an issue on the GitHub repository.

---

This README provides a comprehensive overview and instructions to use the Handy_Speaks repository for converting handwritten text to speech and saving extracted text.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/65269353/dfbd036b-2319-4e96-96e9-f9a3619cfb59/paste.txt

---
Answer from Perplexity: pplx.ai/share
