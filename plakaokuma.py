import cv2
import numpy as np
import pytesseract
import imutils

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Yol doğruysa

img = cv2.imread("araba.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filtered = cv2.bilateralFilter(gray, 5, 250, 250)
edged = cv2.Canny(filtered, 70, 300)

contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
screen = None

for c in cnts:
    epsilon = 0.018 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    if len(approx) == 4:
        screen = approx
        break

if screen is None:
    print("Plaka benzeri dörtgen bulunamadı.")
    exit()

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [screen], 0, 255, -1)  # Tek kanal
new_img = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)

(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))

cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
text = pytesseract.image_to_string(cropped, lang="eng")
print("OCR sonucu:", text)

cv2.imshow("Gri", gray)
cv2.imshow("Filtreli", filtered)
cv2.imshow("Kenarlar", edged)
cv2.imshow("Plaka", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
