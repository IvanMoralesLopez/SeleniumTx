from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://127.0.0.1:5500/Alerts/T22_Alert_Promp.html")
time.sleep(3)
alert = driver.find_element(By.NAME, "prompt_alert")
alert.click()
time.sleep(3)
alert = driver.switch_to.alert()
alert.dismiss()
time.sleep()
driver.close()