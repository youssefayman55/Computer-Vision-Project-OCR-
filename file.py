import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C://Program Files//Tesseract-OCR//tesseract.exe"

img = cv2.imread("C:/Users/S_AFRICA/Desktop/Computer Vision Projects/ocr/never.png")

extract_text = pytesseract.image_to_string(img)

print(extract_text)

cv2.imshow("ocr",img)

