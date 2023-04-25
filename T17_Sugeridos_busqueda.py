from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

palabra_busqueda = "Bokit"
driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(2)

busqueda = driver.find_element(By.NAME, "q")
busqueda.send_keys(palabra_busqueda)
time.sleep(3)

for i in range(1,11):
    elementos = driver.find_element(By.XPATH, "//*[@id='jZ2SBf']/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/ul/li["+str(i)+"]/div[1]/div[2]/div[1]/div[1]/span/b").text
#"+str(i)+" sirve para convertir a cadena para que el 1 sea leido por la automatizacion  y poner .text al final para recuperar el testo que encuentre en esa posicion
    print(palabra_busqueda + elementos) 
driver.close()
    