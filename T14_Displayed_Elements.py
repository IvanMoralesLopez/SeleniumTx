from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(5)
displayelement = driver.find_element(By.NAME, "btnI")
print(displayelement.is_displayed()) #regresa true o false si ya cargo el elemento.
print(displayelement.is_enabled()) #regresa true o false si el elemento esta disponible.