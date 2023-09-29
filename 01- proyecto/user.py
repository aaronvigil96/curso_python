class User:
    def __init__(self, nombre, rol, password):
        self.nombre = nombre
        self.rol = rol
        self.password = password
    
    def getNombre(self):
        return self.nombre
    def getRol(self):
        return self.rol
    def getPassword(self):
        return self.password
    def setNombre(self, nombre):
        self.nombre = nombre
    def setRol(self, rol):
        self.rol = rol
    def setPassword(self, password):
        self.password = password
    
