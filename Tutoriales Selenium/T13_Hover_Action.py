#import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver import ActionChains
import time 

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)
elem = driver.find_element(By.LINK_TEXT, ("Condiciones"))

hover = ActionChains(driver).move_to_element(elem) #hace que "figure" en el elemento mencionado arriba.
time.sleep(3)
hover.perform()
time.sleep(10)