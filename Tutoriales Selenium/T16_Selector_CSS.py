import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(4)
content = driver.find_element(By.CSS_SELECTOR, 'a.w3-blue') #Siempre que se busca por CSS se coloca la letra "a" para aclarar que tiene un conjunto de cosas
content.click()
time.sleep(3)