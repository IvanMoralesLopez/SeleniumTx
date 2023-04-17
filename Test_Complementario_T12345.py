import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        s = Service(r"D:\dchrome\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
    
    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select_element = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/select")
        opcion = select_element.find_elements(By.TAG_NAME, "option")
        time.sleep(3)
        for option in opcion:
            print("Los valores son: %s" % option.get_attribute("value"))
            option.click()
            time.sleep(2)
        seleccionar = driver.find_element(By.XPATH, ("//*[@id='main']/div[3]/div[1]/select"))
        time.sleep(3)
        select_element.find_elements(By.XPATH, (f".//option[value='10']"))

        time.sleep(3)
        option.click()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
