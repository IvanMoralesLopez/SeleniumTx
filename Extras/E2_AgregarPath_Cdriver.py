#Asi hay que colocar una vez que se agrega al PATH el Chrome Driver o lo que se use, SIEMPRE AGREGAR A LA VARIABLE DE ENTRONO ANTES "PATH"
from selenium import webdriver  
driver = webdriver.Chrome("chromedriver.exe")



# <div class = "login-button-container">
#     <div class = "wrapper">
#         <button class = "profile-button" id = "profile-button" id_unico = "profile-button">
#             <img height = "20" src = "/path/to/img.svg" alt = "unboton">
#          <span class = "login"> Entrar</span>
#         </button>
#     </div>
# </div>