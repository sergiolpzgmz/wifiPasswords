import subprocess
#Permite usar comandos de sistema
import re
#Permite usar expresions regulares

comando = "netsh wlan show profiles"
#Lista perfiles de la interfaz WI-FI
perfilInterfaz = subprocess.run(comando, capture_output=True).stdout.decode('iso-8859-1')
#Despues de obtener la lista capturamos el nombre de la red
nombreRed = re.findall("Perfil de todos los usuarios     : (.*)\r", perfilInterfaz)

listaContraseñeas = list()
#Lista que almacenará el nombre de la red y la contraseña

for nombre in nombreRed:
    #Recorremos el listado de nombres de red para almacenarlos en un diccionario
    datosDeRed = dict()
    datosDeRed['ssid'] = nombre

    segundoComando = "netsh wlan show profiles " + nombre + " key=clear"
    #Lista el perfil de la interfaz WI-FI que nos interesa mostrando la contraseña si esta disponible
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