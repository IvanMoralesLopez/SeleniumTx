from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
#esto sirve para hacer scroll down hasta el final de la pagina
#para cargar todos los elementos q no se cargan si no se baja.

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")  
driver.get("https://www.mercadolibre.com.ar")
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")# buscar info sobre esto.
time.sleep(2)
driver.close()