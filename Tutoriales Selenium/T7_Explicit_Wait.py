import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")

    def usando_explicit_wait(self):
        driver = self.driver
        driver.get("http://sie-prueba.chaco.gob.ar/login")
## Espera un máximo de 10 segundos para que el botón sea visible // esto se puede usar para localizar y esperar que cargue lo que sea que se este solicitando. 
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "_username"))  
            ) 
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()