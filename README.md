# 🚗 License Plate Detection and OCR with OpenCV & Tesseract

This project performs **license plate detection from an image** using OpenCV and extracts text using Tesseract OCR.

---

## 🧰 Technologies Used

- Python
- OpenCV
- NumPy
- pytesseract (Tesseract OCR)
- imutils

---

## 📷 How It Works

1. Load the input image.
2. Convert the image to grayscale.
3. Apply bilateral filtering to reduce noise while keeping edges sharp.
4. Use Canny edge detection.
5. Find contours and select the one that looks like a license plate (rectangle).
6. Crop the region of interest (ROI).
7. Use Tesseract OCR to extract text from the cropped plate.

---

## 📁 Requirements

- Python 3
- OpenCV (`opencv-python`)
- NumPy
- pytesseract
- Tesseract OCR installed on your system

📌 **Tesseract Installation Path**  
Make sure Tesseract is installed and update this line with the correct path:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
