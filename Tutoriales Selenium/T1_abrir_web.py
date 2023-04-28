from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\dchrome\chromedrive.exe")
driver.get("http://sie-prueba.chaco.gob.ar/login")
driver.close()