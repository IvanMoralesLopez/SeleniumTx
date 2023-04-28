#"D:\dchrome\chromedriver.exe"
#Como encontrar un elemento si no se encuentra por "id" "name" etc. // cuando el codigo cambia mucho.
#importate: xpath: estructura de objetos (xml)
#xpath relativo:busca por toda la ruta lo solicitado: //*[@id="username"]
#xpath absoluto:busca en la ruta DIRECTA que se escribe.
#doble comillas no permitidas.

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("http://sie-prueba.chaco.gob.ar/login")
#time.sleep(): da tiempo de carga
        time.sleep(3)
        buscar_por_xpath = driver.find_element(By.XPATH, "//*[@id='username']") 
        time.sleep(3) 
        buscar_por_xpath.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        buscar_por_xpath.send_keys("Adminecom178k")
        time.sleep(2)
        #buscar_por_xpath.send_keys(Keys.TAB)
        buscar_por_xpath = driver.find_element(By.XPATH, "//*[@id='password']")
        time.sleep(2)
        buscar_por_xpath.send_keys("equiposie2022")
        time.sleep(2)
        #buscar_por_xpath.send_keys(Keys.TAB)
        time.sleep(2) 
        buscar_por_xpath = driver.find_element(By.XPATH, "//*[@id='_submit']")
        buscar_por_xpath.send_keys(Keys.ENTER)
        time.sleep(10)
#para cerrar el proceso
def tearDown(self):
    self.driver.close()

# con esto le decimos que corra el \\    
if __name__ == '__main__':
    unittest.main()
    