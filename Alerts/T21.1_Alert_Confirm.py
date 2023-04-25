from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://127.0.0.1:5500/Alerts/T21_Alert_Confirm.html")
time.sleep(2)
confirm_alert = driver.find_element(By.NAME, "confirmar_alert")
confirm_alert.click()
time.sleep(2)
confirm_alert = driver.switch_to.alert
confirm_alert.dismiss() #dismiss = cancelar #accept = acepta.
time.sleep(2)
driver.close()
