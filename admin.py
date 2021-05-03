class Admin:
    def __init__(self,nombre,apellido,NombreUsuario,Contra):
        self.nombre=nombre
        self.apellido=apellido
        self.NombreUsuario=NombreUsuario
        self.contra=Contra

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    def getNomUsuario(self):
        return self.NombreUsuario
    
    def getContra(self):
        return self.contra

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def setNomUsuario(self,nombreUsuario):
        self.NombreUsuario=nombreUsuario
    
    def setContra(self,contra):
        self.contra=contra