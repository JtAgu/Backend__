from Medicina import Medicina
class Pedido:
    def __init__(self,correlativo,IdPac,NomPaciente,Medicinas,total):
        self.correlativo=correlativo
        self.IdPaciente=IdPac
        self.Paciente=NomPaciente
        self.Medicina=Medicinas
        self.Total=total

# METODOS GET

    def getId(self):
        return self.correlativo

    def getIdPaciente(self):
        return self.IdPaciente
    
    def getNomPaciente(self):
        return self.NomPaciente
        

    # METODOS SET
    
    
    

