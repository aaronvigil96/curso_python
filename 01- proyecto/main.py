from user import *
from verificadores import *

logones = (User('B959263','SUPERIOR','CHIPI1971'),User('C569853','ADJUNTO','EURASIA'),User('T698952','TEMPORARIO','JAJAJANT'),User('Z698563','TERCERIZADO','ECHENME'))

contador = 3

while contador > 0:
    codigo = input('Ingresá el código alfanúmerico: ').upper()
    print('Intentos restantes: ' + str(contador))
    if verificarCodigo(codigo, logones):
        logon = buscarLogon(codigo, logones)
        while contador != 0:
            password = input('Ingresá el password del logon')
            if verificarPassword(password, logon):
                print('Bienvenido')
                break
            else:
                print('Password incorrecto')
                contador = contador - 1
    else:
        print("No existe el código " + codigo)
    contador = contador - 1


