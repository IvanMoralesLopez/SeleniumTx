import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import cv2
import time

# IMPORTANTE: la imagen a comprar siempre tiene que estar en la misma ruta que el screen que saca.

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")

    def test_usando_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com") 
        driver.save_screenshot("img2.png")
        time.sleep(3)
    
    def test_comparando_imagenes(self):
        img1 = cv2.imread('img1.png')
        img1 = cv2.resize(img1, (640, 480))
        img2 = cv2.imread('img2.png')
        img2 = cv2.resize(img2, (640, 480))

        if img1.shape != img2.shape:
            raise Exception("Las Matrices no tienen el mismo tamaño")
        
        if img1.dtype != img2.dtype:
            raise Exception("Las Matricies no tienen el mismo tipo de dato")

#cv2.absdiff = sirve para hacer una comparativa entre imagenes CON OPENCV.

        diferencia = cv2.absdiff(img1, img2)

#cv2.COLOR_BGR2GRAY = Sirve para buscar por gama de colores

        imagen_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
        contours,_ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #declarar una coleccion de datos

        for c in contours:
            if cv2.contourArea(c) >= 20:
                posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c) #con esta linea encontramos la diferencia
                cv2.rectangle(img1,(posicion_x, posicion_y), (posicion_x + ancho, posicion_y + alto),(0,0,255), 2) #con esta linea se dibuja la diferencia.

        while(1):
            cv2.imshow('Imagen1', img1)
            cv2.imshow('Imagen2', img2)
            cv2.imshow('Diferencias detectadas', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        
        cv2.destroyAllWindows()

if __name__ == '__main__':
    unittest.main()