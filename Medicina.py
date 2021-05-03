class Medicina:
    def __init__(self,correlativo,nombre,precio,descripcion,cantidad,Vendido):
        self.correlativo=correlativo
        self.nombre=nombre
        self.precio=precio
        self.descripcion=descripcion
        self.cantidad=cantidad
        self.Vendido=Vendido

# METODOS GET

    def getId(self):
        return self.correlativo

    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio

    def getDescrp(self):
        return self.descripcion
    
    def getCantidad(self):
        return self.cantidad
    
    def getVende(self):
        return self.Vendido

    # METODOS SET
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def setDes(self, descripcion):
        self.descripcion =descripcion

    def setCan(self,cantidad):
        self.cantidad=cantidad
    
    def setVen(self,Ven):
        self.Vendido=Ven

    
