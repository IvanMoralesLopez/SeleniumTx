from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com")
time.sleep(3)

encontrar_link = driver.find_element(By.LINK_TEXT, "Learn HTML") #El nombre tiene que ser EXACTO para que lo encuentre.
encontrar_link.click()
time.sleep(3)

