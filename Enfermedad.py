class Enfermedad:
    def __init__(self,nombre,Padecimientos):
        self.nombre=nombre
        self.Numero=Padecimientos

# METODOS GET

    def getNombre(self):
        return self.nombre
    
    def getNum(self):
        return self.Numero

    
    # METODOS SET
    
    def setNum(self, Num):
        self.Numero = Num
    
   

    
