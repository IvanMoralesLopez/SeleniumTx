from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("http://www.python.org")
time.sleep(3)
driver.close()