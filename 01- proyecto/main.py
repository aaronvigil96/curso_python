from user import *
from verificadores import *

logones = (User('B959263','SUPERIOR','CHIPI1971'),User('C569853','ADJUNTO','EURASIA'),User('T698952','TEMPORARIO','JAJAJANT'),User('Z698563','TERCERIZADO','ECHENME'))

contador = 3
estado = None

while contador > 0:
    codigo = input('Ingresá el código alfanúmerico: ').upper()
    if verificarCodigo(codigo, logones):
        logon = buscarLogon(codigo, logones)
        while contador != 0:
            password = input('Ingresá el password del logon: ').upper()
            if verificarPassword(password, logon):
                print('Bienvenido')
                estado = logon
                break
            else:
                print('Password incorrecto')
                contador = contador - 1
    else:
        print("No existe el código " + codigo)
        contador = contador - 1
    if estado:
        break
    print('Intentos restantes: ' + str(contador))

if estado:
    print("Mostrando abajo")
    print(estado)
else:
    print("Gracias por utilizar la APP de logones")
