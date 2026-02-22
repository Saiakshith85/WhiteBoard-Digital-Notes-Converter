import cv2
import pytesseract
from docx import Document


pytesseract.pytesseract.tesseract_cmd = r"E:\Python project\tesseract.exe"

input_image = "whiteboard.png"
img = cv2.imread(input_image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
processed = cv2.bitwise_not(thresh)

cv2.imwrite("processed.png", processed)
print("✅ Image processed and saved as processed.png")
text = pytesseract.image_to_string(processed)

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write(text)
doc = Document()
for line in text.split("\n"):
    if line.strip():  # skip empty lines
        doc.add_paragraph(line)
doc.save("notes.docx")

print("✅ OCR complete! Text saved as notes.txt and notes.docx")

