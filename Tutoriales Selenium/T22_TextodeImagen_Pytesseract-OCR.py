import cv2
import pytesseract

imagen = cv2.imread("pruebacv2.png")
#digi.bib.uni-mannheim.de/tesseract link para descargar.
pytesseract.pytesseract.tesseract_cmd("C:\\Program Files\\Tesseract-OCR\\tesseract.exe")

texto = pytesseract.image_to_string(imagen)
print(texto)