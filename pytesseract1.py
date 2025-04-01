# import pytesseract as pyt
# import cv2

# img =cv2.imread("C:\c c++ files\coding files\.vscode\hadnwriting_reader\Test2handfile.png")

# pyt.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# text = pyt.image_to_string(img)
# print(text)
#     # Save the extracted text to a .txt file
# with open("extracted_text.txt", "w", encoding="utf-8") as file:
#         file.write(text)

import pytesseract as pyt
import cv2

# Load the image
img = cv2.imread(r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\he is pps.png")

# Check if image is loaded properly
if img is None:
    print("Error: Image not found or unable to load. Check file path.")
else:
    pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
    # Convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Extract text from image
    text = pyt.image_to_string(img)
    
    # Print the extracted text
    print(text)
save_path = r"C:\c c++ files\coding files\.vscode\hadnwriting_reader\extracted_text.txt"

with open(save_path, "w", encoding="utf-8") as file:
    file.write(text)


