import os
import shutil
import subprocess

# Set paths
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR"
TRAIN_DIR = r"C:\tesseract_training"
FONT_NAME = "Arial"  # Change if needed
LANG_NAME = "custom"  # Custom OCR language name

# Create necessary folders
os.makedirs(TRAIN_DIR, exist_ok=True)

# Step 1: Generate Training Images & Box Files
print("Generating training images and box files...")
text2image_cmd = [
    os.path.join(TESSERACT_PATH, "text2image.exe"),
    f"--text={TRAIN_DIR}\\training_text.txt",
    f"--outputbase={TRAIN_DIR}\\training_image",
    f"--font={FONT_NAME}"
]
subprocess.run(text2image_cmd, shell=True)

# Step 2: Generate Box File from Image
print("Generating box file...")
tesseract_box_cmd = [
    os.path.join(TESSERACT_PATH, "tesseract.exe"),
    f"{TRAIN_DIR}\\training_image.tif",
    f"{TRAIN_DIR}\\training_image_box",
    "nobatch",
    "box.train"
]
subprocess.run(tesseract_box_cmd, shell=True)

# Step 3: Extract Character Set
print("Extracting character set...")
unicharset_cmd = [
    os.path.join(TESSERACT_PATH, "unicharset_extractor.exe"),
    f"{TRAIN_DIR}\\training_image_box.box"
]
subprocess.run(unicharset_cmd, shell=True)

# Step 4: Train the OCR model
print("Training the model...")
mftraining_cmd = [
    os.path.join(TESSERACT_PATH, "mftraining.exe"),
    "-F", f"{TRAIN_DIR}\\font_properties",
    "-U", f"{TRAIN_DIR}\\unicharset",
    "-O", f"{TRAIN_DIR}\\{LANG_NAME}.unicharset",
    f"{TRAIN_DIR}\\training_image_box.tr"
]
subprocess.run(mftraining_cmd, shell=True)

cntraining_cmd = [
    os.path.join(TESSERACT_PATH, "cntraining.exe"),
    f"{TRAIN_DIR}\\training_image_box.tr"
]
subprocess.run(cntraining_cmd, shell=True)

# Step 5: Rename trained files
print("Renaming trained files...")
os.rename(os.path.join(TRAIN_DIR, "normproto"), os.path.join(TRAIN_DIR, f"{LANG_NAME}.normproto"))
os.rename(os.path.join(TRAIN_DIR, "inttemp"), os.path.join(TRAIN_DIR, f"{LANG_NAME}.inttemp"))
os.rename(os.path.join(TRAIN_DIR, "pffmtable"), os.path.join(TRAIN_DIR, f"{LANG_NAME}.pffmtable"))
os.rename(os.path.join(TRAIN_DIR, "shapetable"), os.path.join(TRAIN_DIR, f"{LANG_NAME}.shapetable"))

# Step 6: Combine to Trained Model
print("Creating final traineddata model...")
combine_cmd = [
    os.path.join(TESSERACT_PATH, "combine_tessdata.exe"),
    f"{TRAIN_DIR}\\{LANG_NAME}."
]
subprocess.run(combine_cmd, shell=True)

# Move traineddata file to tessdata folder
shutil.move(f"{TRAIN_DIR}\\{LANG_NAME}.traineddata", os.path.join(TESSERACT_PATH, "tessdata"))

print(f"Training complete! The trained data is saved in {TESSERACT_PATH}\\tessdata\\{LANG_NAME}.traineddata")
