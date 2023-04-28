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

    def usando_implicits_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("http://www.google.com") 
        myDynamicElement = driver.find_element(By.NAME, "q")

if __name__ == '__main__':
    unittest.main()