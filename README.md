# 📝 Optical Character Recognition (OCR) using OpenCV & Tesseract

## 🧠 Overview

This project demonstrates a simple **Optical Character Recognition (OCR)** system that extracts text from images.
It uses **Tesseract OCR** with Python to detect and convert text within an image into machine-readable format.

The application loads an image, processes it, and prints the extracted text.

---

## 🚀 Features

* 🖼️ Read text from images
* 🔍 Accurate text extraction using Tesseract OCR
* ⚡ Simple and lightweight implementation
* 🧾 Supports printed text recognition

---

## 🛠️ Technologies Used

* Python 🐍
* OpenCV (Image Processing)
* Pytesseract (OCR Engine Wrapper)
* Tesseract OCR Engine

---

## 📂 Project Structure

```id="m9x2kp"
├── app.py
├── image.png
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash id="r5n8qd"
pip install opencv-python pytesseract
```

### 2. Install Tesseract OCR

Download and install Tesseract from:
👉 https://github.com/tesseract-ocr/tesseract

### 3. Update Tesseract Path

Make sure to update the path in your code:

```python id="p1k4zw"
pytesseract.pytesseract.tesseract_cmd = "C://Program Files//Tesseract-OCR//tesseract.exe"
```

### 4. Run the Script

```bash id="t6b3vx"
python app.py
```

---

## 🎯 How It Works

* The image is loaded using OpenCV
* Tesseract processes the image
* Extracted text is returned as a string
* The result is printed in the console

---

## 📸 Output

* Displays the input image
* Prints extracted text in the terminal

---

## 💡 Use Cases

* Digitizing documents 📄
* Extracting text from images/screenshots 🖥️
* License plate recognition 🚗
* Automating data entry 🧾

---

## 💡 Future Improvements

* Add image preprocessing (grayscale, thresholding) for better accuracy
* Support handwritten text recognition ✍️
* Build a GUI or web app for user interaction
* Export extracted text to files (TXT, PDF)

---

## 👨‍💻 Author

**Youssef Ayman**
AI Engineer & Data Scientist

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
