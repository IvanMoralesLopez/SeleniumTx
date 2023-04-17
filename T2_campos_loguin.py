from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("http://sie-prueba.chaco.gob.ar/login")

usuario = driver.find_element("name", '_username')
usuario.send_keys("adminecom178k")
usuario.send_keys(Keys.TAB)

clave = driver.find_element("name", "_password")
clave.send_keys("equiposie2022")
clave.send_keys(Keys.ENTER)
time.sleep(3)

#hay que importar siempre lo siguiente para que se ejecute bien el codigo con las librerias:
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
