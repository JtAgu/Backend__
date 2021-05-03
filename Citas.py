class Citas:
    def __init__(self,correlativo,IdPaci,NomPaciente,IdDoc,NomDoc,descripcion,Fecha,Hora,estado,Acept):
        self.correlativo=correlativo
        self.IdPaciente=IdPaci
        self.NomPaciente=NomPaciente
        self.IdDoctor=IdDoc
        self.NomDoc=NomDoc
        self.descripcion=descripcion
        self.Fecha=Fecha
        self.Estado=estado
        self.Hora=Hora
        self.Acept=Acept

# METODOS GET

    def getId(self):
        return self.correlativo

    def getIdPaciente(self):
        return self.IdPaciente
    
    def getNomPaciente(self):
        return self.NomPaciente
    
    def getIdDoc(self):
        return self.IdDoctor

    def getNomDoc(self):
        return self.NomDoc
    
    def getHora(self):
        return self.Hora

    def getDescrp(self):
        return self.descripcion
    
    def getFecha(self):
        return self.Fecha
    
    def getEstado(self):
        return self.Estado
    
    def getAcept(self):
        return self.Acept
    

    # METODOS SET
    def setIdDoc(self, IdDoc):
        self.IdDoctor = IdDoc

    def setNomDoc(self, Doc):
        self.NomDoc = Doc

    def setEstado(self, Estado):
        self.Estado = Estado

    def setAceptada(self, Acepta):
        self.Acept = Acepta
    
    

