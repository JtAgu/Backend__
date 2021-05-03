class Persona:
    def __init__(self,nombre,apellido,edad,sexo,nombreUsuario,contra,tele,tipo):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.sexo=sexo
        self.nombreUsuario=nombreUsuario
        self.contra=contra
        self.tele=tele
        self.tipo=tipo

# METODOS GET
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad
    
    def getSexo(self):
        return self.sexo
    
    def getNomUsuario(self):
        return self.nombreUsuario
    
    def getContra(self):
        return self.contra
    
    def getTele(self):
        return self.tele

    def getTipo(self):
        return self.tipo


    # METODOS SET
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self,sexo):
        self.sexo=sexo
    
    def setNomUsuario(self,nombreUsuario):
        self.nombreUsuario=nombreUsuario
    
    def setContra(self,contra):
        self.contra=contra
    
    def setTele(self,tele):
        self.tele=tele

