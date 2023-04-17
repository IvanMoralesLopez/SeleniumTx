import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
#driver.back = volver a la pestaña anterior.
#driver.forward = ir a la siguiente pestaña.
class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
    
    def test_pagin_siguient_o_anterior(self):
        driver = self.driver
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("http://www.youtube.com")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
