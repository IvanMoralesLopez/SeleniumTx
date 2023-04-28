import unittest
import configparser
import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Aca defimos lo que se quiere hacer con el script y "set.py" se selecciona las configuraciones
#, luego con "configuraciones.ini" se editan las url de las paginas 
class usando_unittest(unittest.TestCase):
    def setUp(self):
        configuracion = configparser.ConfigParser()
        configuracion.read('configuracion.ini')
        configuracion.sections()
        obtenerexplorer = configuracion['General']['chrome']
        self.page = configuracion['Paginas']['page']
        self.driver = webdriver.Chrome(executable_path=obtenerexplorer)

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) 
        driver.get(self.page)
        navegador = driver.find_element(By.NAME, "search_query") #dynamic element = cual nombre puede ser puesto
        time.sleep(3)
        navegador.send_keys("eminem")
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()