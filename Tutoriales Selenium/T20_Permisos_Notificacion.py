from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import time

opciones = Options()

#enviar argumentos(1 permite, 2 bloquea (las notificaciones))
opciones.add_experimental_option("prefs",{
    "profile.default_content_setting_values.notificatios" : 2
})

driver = webdriver.Chrome(chrome_options=opciones, executable_path=r"D:\dchrome\chromedriver.exe")
driver.get("https://developer.mozilla.org/es/docs/web/api/notification")
time.sleep(3)