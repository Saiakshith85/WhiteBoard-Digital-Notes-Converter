import cv2
import pytesseract
from docx import Document

# Tell pytesseract where Tesseract OCR is installed
pytesseract.pytesseract.tesseract_cmd = r"E:\Python project\tesseract.exe"

# -------------------------------
# STEP 1: Load and process image
# -------------------------------
# Change this to your input image (whiteboard photo)
input_image = "whiteboard.png"

# Read the image
img = cv2.imread(input_image)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding (makes text stand out)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Invert back to normal (black text on white)
processed = cv2.bitwise_not(thresh)

# Save processed image
cv2.imwrite("processed.png", processed)
print("✅ Image processed and saved as processed.png")

# -------------------------------
# STEP 2: OCR (extract text)
# -------------------------------
# Use Tesseract OCR
text = pytesseract.image_to_string(processed)

# -------------------------------
# STEP 3: Save output
# -------------------------------

# Save as .txt
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Save as .docx
doc = Document()
for line in text.split("\n"):
    if line.strip():  # skip empty lines
        doc.add_paragraph(line)
doc.save("notes.docx")

print("✅ OCR complete! Text saved as notes.txt and notes.docx")
