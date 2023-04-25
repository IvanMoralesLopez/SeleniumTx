from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")

valor = driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[2]/td[2]").text # .text es para q guarde todo el la variable "valor"
                                                            #tr[] td[], adentro poner el n° q se necesita sacar los datos.
print(valor)
rows = len(driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr")) #len(), indica el tamaño de la filas
colum = len(driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th")) #len(), indica el tamaño de la columnas
print(rows)
print(colum)

for n in range(2, rows+1):
    for b in range(1, colum+1):
        dato = driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text #para extraer la informacion.

        print(dato, end='                         ')
    print()