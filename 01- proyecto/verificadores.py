def verificarCodigo(nombre, logones):
    for logon in logones:
        if nombre == logon.getNombre():
            return True
    return False

def buscarLogon(nombre, logones):
    for logon in logones:
        if nombre == logon.getNombre():
            return logon
    return None

def verificarPassword(nombre, logon):
    if nombre == logon.getPassword():
        return True
    else:
        return False