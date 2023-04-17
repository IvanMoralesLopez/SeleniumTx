import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedirver.exe")

#SIEMPRE poner "test" antes del name para la funcion, primero inicia con "setUp"

    def test_buscar(self):
        driver = self.driver
        driver.get("http://sie-prueba.chaco.gob.ar/login")
#self.assertIn: confirmar que esta entrando a la pagina que se solicita.
        self.assertIn("chrome", driver.name)
        
        time.sleep(2)

        elemento = driver.find_element("name", "_username")
        elemento.send_keys(Keys.PAGE_DOWN)
        elemento.send_keys("adminecom178k")
        time.sleep(2)
        elemento.send_keys(Keys.TAB)
        elemento = driver.find_element("name", "_password")
        time.sleep(3)
        elemento.send_keys("equiposie2022")
        time.sleep(3)
        elemento.send_keys(Keys.TAB)
        time.sleep(1)
        elemento.send_keys(Keys.ENTER)

        time.sleep(10)

#assert: verificar que... "" no esta en el codigo de la pagina:
        assert "No se encontro el elemento:" not in driver.page_source

#cuando se usan los T.C. (se usan funciones (def)) 
#tearDown: apagar el proceso ()
    def tearDown(self):
        self.driver.close()

#para cerrar la CLASE:

if __name__ == '__main__':
    unittest.main()