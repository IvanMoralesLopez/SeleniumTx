#Una vez creado el "Set.py", al correr el codigo crea un archivo con el nombre de la variable
#en este caso "configuracion.ini", esto se crea en la carpeta general del proyecto OJO.
import configparser

configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome' : 'D:\dchrome\chromedriver.exe'}
configuracion['Paginas'] = {'page' : 'https://www.youtube.com'} 

with open('configuracion.ini', 'w') as archivoconfig:
    configuracion.write(archivoconfig):