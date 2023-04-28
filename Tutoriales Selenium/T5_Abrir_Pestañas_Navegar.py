import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
    
    def test_cambiar_venta(self):
        driver = self.driver
        driver.get("http://sie-prueba.chaco.gob.ar/login")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://stackoverFlow.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(4)

if __name__ == '__main__':
    unittest.main()