import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
    
    def test_urm(self):
        driver = self.driver
        driver.get("http://sie-prueba.chaco.gob.ar/login")
        time.sleep(1)
        time.sleep(1)
        URM_V1 = driver.find_element(By.XPATH, "//*[@id='username']") 
        time.sleep(2) 
        URM_V1.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        URM_V1.send_keys("Adminecom178k")
        time.sleep(2)
        #buscar_por_xpath.send_keys(Keys.TAB)
        URM_V1 = driver.find_element(By.XPATH, "//*[@id='password']")
        time.sleep(2)
        URM_V1.send_keys("***")
        time.sleep(2)
        #buscar_por_xpath.send_keys(Keys.TAB)
        time.sleep(2) 
        test_urm = driver.find_element(By.XPATH, "//*[@id='_submit']")
        test_urm.send_keys(Keys.ENTER)
        time.sleep(5)

        Modulo_Administr_Usuar = driver.find_element(By.LINK_TEXT, "ADMINISTRAR USUARIOS")
       # Modulo_Administr_Usuar.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        Modulo_Administr_Usuar.click()
        time.sleep(3)
        User_Admin = driver.find_element(By.LINK_TEXT, "Usuarios admin")
        time.sleep(3)
        User_Admin.click()
        time.sleep(2)
        Xpath_Buscar = driver.find_element(By.XPATH, "//*[@id='easyadmin-list-User']/div/div/div[2]/section[1]/div[1]/div[2]/div[1]/form/div/div/input")
        time.sleep(2)
        Xpath_Buscar.send_keys("Coordinador")
        time.sleep(2)
        Xpath_Buscar.send_keys(Keys.ENTER)
        time.sleep(2)
        Xpath_Suplantar = driver.find_element(By.XPATH, "//*[@id='tabla_paginada']/tbody/tr[1]/td[1]/div/a[1]")
        time.sleep(2)
        Xpath_Suplantar.click()
        time.sleep(3)

#para cerrar el proceso
def tearDown(self):
    self.driver.close()

# con esto le decimos que corra el \\    
if __name__ == '__main__':
    unittest.main()