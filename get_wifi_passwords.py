#subprocess permite usar comandos de sistema
import subprocess
#re permite usar expresiones regulares
import re

#Comando que lista perfiles de la interfaz WI-FI
comando = "netsh wlan show profiles"
perfilInterfaz = subprocess.run(comando, capture_output=True).stdout.decode('iso-8859-1')
#Despues de obtener la lista capturamos el nombre de la red
nombreRed = re.findall("Perfil de todos los usuarios     : (.*)\r", perfilInterfaz)

#Lista que almacenará el nombre de la red y la contraseña
listaContraseñeas = list()

# Recorremos el listado de nombres de red para almacenarlos en un diccionario
for nombre in nombreRed:
    datosDeRed = dict()
    datosDeRed['ssid'] = nombre

    #Comando que lista el perfil de la interfaz WI-FI que nos interesa mostrando la contraseña si está disponible
    segundoComando = "netsh wlan show profiles " + nombre + " key=clear"
    introducirComando = subprocess.run(segundoComando, capture_output=True).stdout.decode('iso-8859-1')
    #Captura la contraseña
    contraseñaObtenida = re.findall("Contenido de la clave  : (.*)\r", introducirComando)

    if contraseñaObtenida == []:
        datosDeRed['contraseña']= "Contraseña desconocida"
    else:
        datosDeRed['contraseña']= contraseñaObtenida

    listaContraseñeas.append(datosDeRed)

for lista in listaContraseñeas:
    print(lista)
