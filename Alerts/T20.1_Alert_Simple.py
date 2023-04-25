from selenium import webdriver    
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("http://127.0.0.1:5500/Alerts/T20_Alert_Simple.html")
time.sleep(5)
alerta_simple = driver.find_element(By.NAME, "Alert")
alerta_simple.click()
time.sleep(3)
alerta_simple=driver.switch_to_Alert()
alerta_simple.dismiss()
time.sleep(3)
driver.close()