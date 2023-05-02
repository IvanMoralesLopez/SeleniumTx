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
        URM_V1 = driver.find_element(By.XPATH, "//*[@id='username']") 
        time.sleep(2) 
        URM_V1.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        URM_V1.send_keys("Adminecom178k")
        time.sleep(2)
        #buscar_por_xpath.send_keys(Keys.TAB)
        URM_V1 = driver.find_element(By.XPATH, "//*[@id='password']")
        time.sleep(2)
        URM_V1.send_keys("sie2023") #poner pw.
        
        time.sleep(2)
        #buscar_por_xpath.send_keys(Keys.TAB)
        test_urm = driver.find_element(By.XPATH, "//*[@id='_submit']")
        test_urm.send_keys(Keys.ENTER)
        time.sleep(5)
        Modulo_Administr_Usuar = driver.find_element(By.LINK_TEXT, "ADMINISTRAR USUARIOS")
        #Modulo_Administr_Usuar.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        Modulo_Administr_Usuar.click()
        time.sleep(3)
        User_Admin = driver.find_element(By.LINK_TEXT, "Usuarios admin")
        time.sleep(1)
        User_Admin.click()
        time.sleep(1)
        Xpath_Buscar = driver.find_element(By.XPATH, "//*[@id='easyadmin-list-User']/div/div/div[2]/section[1]/div[1]/div[2]/div[1]/form/div/div/input")
        time.sleep(2)
        Xpath_Buscar.send_keys("RM.TEST.DIRECTOR") #Aca va el ROLE
        time.sleep(2)
        Xpath_Buscar.send_keys(Keys.ENTER)
        time.sleep(2)
        Xpath_Suplantar = driver.find_element(By.XPATH, "//*[@id='tabla_paginada']/tbody/tr/td[1]/div/a[1]/i") 
        time.sleep(2)                                       
        Xpath_Suplantar.click()
        time.sleep(2)
        Reconocimiento_Medico = driver.find_element(By.LINK_TEXT, "RECONOCIMIENTO MEDICO")
        time.sleep(1)
        Reconocimiento_Medico.click()
        RM_Crear_Solic = driver.find_element(By.LINK_TEXT, "Solicitud de RM")
        time.sleep(1)
        RM_Crear_Solic.click()
        time.sleep(3)
        Solic_DNI = driver.find_element(By.ID, "crear_solicitud_dni")
        Solic_DNI.click()
        time.sleep(4)
        DNI_ID = driver.find_element(By.NAME, "dni")
        DNI_ID.click()
        DNI_ID.send_keys("28726602")
        DNI_ID.send_keys(Keys.TAB)
        time.sleep(2)
        Establecimiento = driver.find_element(By.ID, "select2-localizacion-container") 
        Establecimiento.click()
        Establecimiento.send_keys(Keys.ARROW_DOWN)
        Establecimiento.send_keys(Keys.ENTER)
        time.sleep(2)
        #Establecimiento.send_keys(Keys.ENTER)
        time.sleep(1)
        #DNI_ID.send_keys(Keys.ENTER)
        #time.sleep(2)
        Calendario = driver.find_element(By.ID, "fechaDesde")
        Calendario.click()
        
#para cerrar el proceso
def tearDown(self):
    self.driver.close()

# con esto le decimos que corra el \\    
if __name__ == '__main__':
    unittest.main()