from flask import Flask, jsonify,request
from flask_cors import CORS
import json

from Persona import Persona
from Doctor import Doctor
from Medicina import Medicina
from admin import Admin
from Citas import Citas
from Pedido import Pedido
from Enfermedad import Enfermedad


Personas=[]
Doctores=[]
Medicinas=[]
Citase=[]
Pedidos=[]
Enfermedades=[]

MedicinaPedido=[]


NCitas=1
NPedido=1

app= Flask(__name__)
CORS(app)

Administrador=Admin("Abner","Cardona","admin",1234)

@app.route('/',methods=['GET'])
def Ayuda():
    objeto ={
        "Nombre":"Hola"
    }
    Datos.append(objeto)
    return(jsonify(Datos))


@app.route('/Pacientes',methods=['GET'])
def ObtenPersona():
    global Persona
    Datos=[]
    for persona in Personas:
       if persona.getTipo()=="Paciente":
            objeto ={
                "Nombre":persona.getNombre(),
                "Apellido":persona.getApellido(),
                "Edad":persona.getEdad(),
                'Sexo':persona.getSexo(),
                'nombreUsuario': persona.getNomUsuario(),
                'Contra': persona.getContra(),
                'Tele': persona.getTele()
            }
            Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Enfermeras',methods=['GET'])
def Obten():
    global Persona
    Datos=[]
    for persona in Personas:
        if persona.getTipo()=="Enfermera":
            objeto ={
                "Nombre":persona.getNombre(),
                "Apellido":persona.getApellido(),
                "Edad":persona.getEdad(),
                'Sexo':persona.getSexo(),
                'nombreUsuario': persona.getNomUsuario(),
                'Contra': persona.getContra(),
                'Tele': persona.getTele()
            }
            Datos.append(objeto)
    return(jsonify(Datos))


@app.route('/Doctor',methods=['GET'])
def ObtenDoc():
    global Doctores
    DatosD=[]
    for D in Doctores:
        objetoD ={
            'NombreD':D.getNombre(),
            'ApellidoD':D.getApellido(),
            'EdadD':D.getEdad(),
            'SexoD':D.getSexo(),
            'nombreUsuarioD': D.getNomUsuario(),
            'ContraD': D.getContra(),
            'TeleD': D.getTele(),
            'Especial':D.getEspecial(),
            'Atendido':D.getCitas()
        }
        DatosD.append(objetoD)
    return(jsonify(DatosD))

@app.route('/Medicina',methods=['GET'])
def ObtenMedicinas():
    global Medicinas
    Datos=[]
    for M in Medicinas:
        objeto ={
            'Id':M.getId(),
            'Nombre':M.getNombre(),
            'Precio':M.getPrecio(),
            'Descripcion':M.getDescrp(),
            'Cantidad': M.getCantidad(),
            'Vendido': M.getVende()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/MedicinaFac',methods=['GET'])
def ObtenPedido():
    global MedicinaPedido
    Datos=[]
    for M in MedicinaPedido:
        objeto ={
            'Id':M.getId(),
            'Nombre':M.getNombre(),
            'Precio':M.getPrecio(),
            'Descripcion':M.getDescrp(),
            'Cantidad': M.getCantidad()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Enfermedad',methods=['GET'])
def ObtenEnfermedad():
    global Enfermedades
    Datos=[]
    for M in Enfermedades:
        objeto ={
            'Nombre':M.getNombre(),
            'Numero':M.getNum()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Cita',methods=['GET'])
def ObtenCitas():
    global Citase
    Datos=[]
    
    for M in Citase:
        objeto ={
            'Id':M.getId(),
            'IdP':M.getIdPaciente(),
            'Paciente':M.getNomPaciente(),
            'Descripcion':M.getDescrp(),
            'Fecha': M.getFecha(),
            'Hora':M.getHora(),
            'IdDoc':M.getIdDoc(),
            'Estado':M.getEstado(),
            'Ace':M.getAcept(),
            "Mensaje": "Si"
        }
        Datos.append(objeto)
    return(jsonify(Datos))


@app.route('/Paciente/<string:nombre>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerPaciente(nombre): 
    # Referencia al arreglo global
    global Personas
    # Recorrido del arreglo
    for persona in Personas:
        if persona.getNomUsuario() == nombre:
            if persona.getTipo()=="Paciente":
                # Crear el objeto
                objeto = {
                'Nombre': persona.getNombre(),
                'Apellido': persona.getApellido(),
                'Edad': persona.getEdad(),
                'Sexo':persona.getSexo(),
                'nombreUsuario': persona.getNomUsuario(),
                'Contra': persona.getContra(),
                'Tele': persona.getTele(),
                'Mensaje':"Si"
                }
                return(jsonify(objeto))
    
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    # Retornamos el objeto creado
    return(jsonify(salida))

@app.route('/Enfermera/<string:nombre>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerEnfermera(nombre): 
    # Referencia al arreglo global
    global Personas
    # Recorrido del arreglo
    for persona in Personas:
    
        if persona.getNomUsuario() == nombre:
            if persona.getTipo()=="Enfermera":
                # Crear el objeto
                objeto = {
                'Nombre': persona.getNombre(),
                'Apellido': persona.getApellido(),
                'Edad': persona.getEdad(),
                'Sexo':persona.getSexo(),
                'nombreUsuario': persona.getNomUsuario(),
                'Contra': persona.getContra(),
                'Tele': persona.getTele(),
                'Mensaje':"Si"
                }
                return(jsonify(objeto))
    
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    # Retornamos el objeto creado
    return(jsonify(salida))



@app.route('/Doctor/<string:nombre>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerDoctor(nombre): 
    # Referencia al arreglo global
    global Doctores
    # Recorrido del arreglo
    for D in Doctores:
    
        if D.getNomUsuario() == nombre:
            # Crear el objeto
            objeto = {
            'Nombre': D.getNombre(),
            'Apellido': D.getApellido(),
            'Edad': D.getEdad(),
            'Sexo':D.getSexo(),
            'nombreUsuario': D.getNomUsuario(),
            'Contra': D.getContra(),
            'Tele': D.getTele(),
            'Especial': D.getEspecial(),
            'Mensaje':"Si"
            }
    
            return(jsonify(objeto))
    
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    # Retornamos el objeto creado
    return(jsonify(salida))

@app.route('/Medicina/<int:nombre>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerMedi(nombre): 
    # Referencia al arreglo global
    global Medicinas
    # Recorrido del arreglo
    for D in Medicinas:
    
        if D.getId() == nombre:
            # Crear el objeto
            objeto = {
            'Id':D.getId(),
            'Nombre': D.getNombre(),
            'Descripcion': D.getDescrp(),
            'Precio':D.getPrecio(),
            'Cantidad': D.getCantidad()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    # Retornamos el objeto creado
    return(jsonify(salida))

@app.route('/CitaIn/<int:nombre>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerCitaIn(nombre): 
    # Referencia al arreglo global
    global Citase
    # Recorrido del arreglo
    for F in Citase:
        if F.getId()==nombre:
            # Crear el objeto
            objeto = {
            'Id':F.getId(),
            'Nombre': F.getNomPaciente(),
            'Descripcion': F.getDescrp(),
            'NombreDoc':F.getNomDoc(),
            'Fecha': F.getFecha()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Enfermedad/<string:nombre>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerEnfermedad(nombre): 
    # Referencia al arreglo global
    global Enfermedades
    # Recorrido del arreglo
    for F in Enfermedades:
        if F.getNombre()==nombre:
            # Crear el objeto
            objeto = {
            'Nombre': F.getNombre(),
            'Num': F.getNum(),
            'Mensaje':"si"
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    # Referencia a la lista global
    global Personas
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    sexo=request.json['sexo']
    nUsuario=request.json['nombreUsuario']
    contra=request.json['contra']
    tele=request.json['tele']
    tipo="Paciente"
    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Persona(nombre,apellido,edad,sexo,nUsuario,contra,tele,tipo)
    # Agregamos la persona
    Personas.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})



@app.route('/Pacientes', methods=['POST'])
def AgregarPaciente():
    # Referencia a la lista global
    global Personas
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    sexo=request.json['sexo']
    nUsuario=request.json['nombreUsuario']
    contra=request.json['contra']
    tele=request.json['tele']
    tipo="Paciente"

    # nuevo objeto con la informacion recolectada del request
    nuevo = Persona(nombre,apellido,edad,sexo,nUsuario,contra,tele,tipo)
    Personas.append(nuevo)
    #objeto JSON con la salida
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})

@app.route('/Enfermeras', methods=['POST'])
def AgregarEnfermera():
    # Referencia a la lista global
    global Personas
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    sexo=request.json['sexo']
    nUsuario=request.json['nombreUsuario']
    contra=request.json['contra']
    tele=request.json['tele']
    tipo="Enfermera"

    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Persona(nombre,apellido,edad,sexo,nUsuario,contra,tele,tipo)
    # Agregamos la persona
    Personas.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})

@app.route('/Doctor', methods=['POST'])
def AgregarDoc():
    # Referencia a la lista global
    global Doctores
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    sexo=request.json['sexo']
    nUsuario=request.json['nombreUsuario']
    contra=request.json['contra']
    tele=request.json['tele']
    especialidad=request.json['especialidad']

    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Doctor(nombre,apellido,edad,sexo,nUsuario,contra,tele,especialidad,0)
    # Agregamos la persona
    Doctores.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})


@app.route('/Medicina', methods=['POST'])
def AgregarMedicina():
    # Referencia a la lista global
    global Medicinas
    global NMedicina
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['des']
    cantidad=request.json['cantidad']
    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Medicina(NMedicina,nombre,precio,descripcion,cantidad)
    # Agregamos la persona
    Medicinas.append(nuevo)
    NMedicina=1+NMedicina
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})


@app.route('/MedicinaFac', methods=['POST'])
def AgregarPedidoMedi():
    # Referencia a la lista global
    global MedicinaPedido
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    Id = request.json['Id']
    Nombre = request.json['Nombre']
    Des = request.json['Descripcion']
    Precio=request.json['Precio']
    Can=request.json['Cantidad']

    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Medicina(Id,Nombre,Precio,Des,Can,0)
    # Agregamos la persona
    MedicinaPedido.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})

@app.route('/Enfermedad', methods=['POST'])
def AgregarEnfermedad():
    # Referencia a la lista global
    global Enfermedades
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    Nombre = request.json['Nombre']
    Padecimiento=1
    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Enfermedad(Nombre,Padecimiento)
    # Agregamos la persona
    Enfermedades.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})

@app.route('/Pedido', methods=['POST'])
def AgregarPedido():
    # Referencia a la lista global
    global Pedidos
    global MedicinaPedido
    global NPedido
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    Id = NPedido
    IdPaciente = request.json['idPaciente']
    Paciente = request.json['Paciente']
    Medicina=MedicinaPedido
    Total=request.json['Total']
    nuevo =Pedido(Id,IdPaciente,Paciente,Medicina,Total)
    # Agregamos la persona
    Pedidos.append(nuevo)
    NPedido=1+NPedido
    return jsonify({'Mensaje':'Se agrego la cita exitosamente',})


@app.route('/Cita', methods=['POST'])
def AgregarCita():
    # Referencia a la lista global
    global Citase
    global NCitas
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    Id = NCitas
    IdPaciente = request.json['idPaciente']
    Paciente = request.json['Paciente']
    descripcion=request.json['Descripcion']
    Fecha=request.json['Fecha']
    Hora=request.json['Hora']
    IdDoc="Sin asignar"
    Doc="Sin Asignar"
    Estado="Pendiente"
    Acept="Sin Asignar"

    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo=Citas(Id, IdPaciente, Paciente, IdDoc, Doc, descripcion, Fecha,  Hora ,Estado,Acept)
    NCitas=NCitas+1
    # Agregamos la persona
    Citase.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego la cita exitosamente',})


# METODO - ACTUALIZAR UN DATO
# actualizaremos el dato que le mandaremos por el parametro y la nueva informacion se mandara en el body
@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    # Hacemos referencia a nuestro usuario global
    global Personas
    
    for i in range(len(Personas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == Personas[i].getNomUsuario():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Personas[i].setNombre(request.json['nombre'])
            Personas[i].setApellido(request.json['apellido'])
            Personas[i].setEdad(request.json['edad'])
            Personas[i].setSexo(request.json['sexo'])
            Personas[i].setNomUsuario(request.json['nombreUsuario'])
            Personas[i].setContra(request.json['contra'])
            Personas[i].setTele(request.json['tele'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/Doctor/<string:nombre>', methods=['PUT'])
def ActualizaDoctor(nombre):
    # Hacemos referencia a nuestro usuario global
    global Doctores
    
    for i in range(len(Doctores)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == Doctores[i].getNomUsuario():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Doctores[i].setNombre(request.json['nombre'])
            Doctores[i].setApellido(request.json['apellido'])
            Doctores[i].setEdad(request.json['edad'])
            Doctores[i].setSexo(request.json['sexo'])
            Doctores[i].setNomUsuario(request.json['nombreUsuario'])
            Doctores[i].setContra(request.json['contra'])
            Doctores[i].setTele(request.json['tele'])
            Doctores[i].setEspecial(request.json['especialidad'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/DoctorCita/<string:nombre>', methods=['PUT'])
def ActualizaDoctorCita(nombre):
    # Hacemos referencia a nuestro usuario global
    global Doctores
    for i in range(len(Doctores)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == Doctores[i].getNomUsuario():
            Doctores[i].setCita(Doctores[i].getCita()+1)
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})



@app.route('/Medicina/<int:ids>', methods=['PUT'])
def ActualizaMedicina(ids):
    # Hacemos referencia a nuestro usuario global
    global Medicinas
    for i in range(len(Medicinas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Medicinas[i].getId():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Medicinas[i].setNombre(request.json['nombre'])
            Medicinas[i].setDes(request.json['des'])
            Medicinas[i].setCan(request.json['cantidad'])
            Medicinas[i].setPrecio(request.json['precio'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})    

@app.route('/MedicinaVender/<int:ids>', methods=['PUT'])
def ActualizaMedicinaVender(ids):
    # Hacemos referencia a nuestro usuario global
    global Medicinas
    for i in range(len(Medicinas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Medicinas[i].getId():
            Medicinas[i].setVen(request.json['Cantidad'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})    

@app.route('/CitaConfirmada/<int:ids>', methods=['PUT'])
def CitaConfirmada(ids):
    # Hacemos referencia a nuestro usuario global
    global Citase
    for i in range(len(Citase)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Citase[i].getId():
            Citase[i].setIdDoc(request.json['IdDoc'])
            Citase[i].setAceptada(request.json['IdEnf'])
            Citase[i].setEstado("Aceptada")
            Citase[i].setNomDoc(request.json['Doc'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})    

@app.route('/CitaRechazada/<int:ids>', methods=['PUT'])
def CitaRechazada(ids):
    # Hacemos referencia a nuestro usuario global
    global Citase
    for i in range(len(Citase)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Citase[i].getId():            
            Citase[i].setEstado("Rechazada")
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})    

@app.route('/CitaCompletada/<int:ids>', methods=['PUT'])
def CitaCom(ids):
    # Hacemos referencia a nuestro usuario global
    global Citase
    for i in range(len(Citase)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Citase[i].getId():            
            Citase[i].setEstado("Completada")
            return jsonify({'Mensaje':'Cita Completada'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})    

@app.route('/CitaFacturada/<int:ids>', methods=['PUT'])
def CitaFac(ids):
    # Hacemos referencia a nuestro usuario global
    global Citase
    for i in range(len(Citase)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Citase[i].getId():            
            Citase[i].setEstado("Facturada")
            return jsonify({'Mensaje':'Cita Facturada'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})    


@app.route('/MedicinaFac/<int:ids>', methods=['PUT'])
def ActualizaMedicinaFac(ids):
    # Hacemos referencia a nuestro usuario global
    global MedicinaPedido
    for i in range(len(MedicinaPedido)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == MedicinaPedido[i].getId():
            MedicinaPedido[i].setCan(MedicinaPedido[i].getCantidad()+1)
            return jsonify({'Mensaje':'Articulo añadido'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'}) 

@app.route('/MedicinaFacMenos/<int:ids>', methods=['PUT'])
def ActualizaMedicinaFacMenos(ids):
    # Hacemos referencia a nuestro usuario global
    global MedicinaPedido
    for i in range(len(MedicinaPedido)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == MedicinaPedido[i].getId():
            MedicinaPedido[i].setCan(MedicinaPedido[i].getCantidad()-1)
            return jsonify({'Mensaje':'Articulo añadido'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'}) 

@app.route('/MedicinaMas/<int:ids>', methods=['PUT'])
def ActualizaMedicinaMas(ids):
    # Hacemos referencia a nuestro usuario global
    global Medicinas
    for i in range(len(Medicinas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Medicinas[i].getId():
            Medicinas[i].setCan(Medicinas[i].getCantidad()+1)
            Medicinas[i].setVen(Medicinas[i].getVende()-1)
            return jsonify({'Mensaje':'Articulo añadido'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'}) 

@app.route('/MedicinaMasMas/<int:ids>', methods=['PUT'])
def ActualizaMedicinaMasMas(ids):
    # Hacemos referencia a nuestro usuario global
    global Medicinas
    for i in range(len(Medicinas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Medicinas[i].getId():
            Medicinas[i].setCan(Medicinas[i].getCantidad()+int(request.json['Cantidad']))
            Medicinas[i].setCan(Medicinas[i].getVende()-int(request.json['Cantidad']))
            return jsonify({'Mensaje':'Articulo añadido'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'}) 


@app.route('/MedicinaMenos/<int:ids>', methods=['PUT'])
def ActualizaMedicinaMenos(ids):
    # Hacemos referencia a nuestro usuario global
    global Medicinas
    for i in range(len(Medicinas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if ids == Medicinas[i].getId():
            Medicinas[i].setCan(Medicinas[i].getCantidad()-1)
            Medicinas[i].setVen(Medicinas[i].getVende()+1)
            return jsonify({'Mensaje':'Articulo añadido'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'}) 

@app.route('/Enfermedad/<string:nombre>', methods=['PUT'])
def ActuEnfermedad(nombre):
    # Hacemos referencia a nuestro usuario global
    global Enfermedades
    for i in range(len(Enfermedades)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == Enfermedades[i].getNombre():
            Enfermedades[i].setNum(Enfermedades[i].getNum()+1)
            return jsonify({'Mensaje':'Articulo añadido'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'}) 

# METODO - ELIMINAR UN DATO
@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    # Referencia al arreglo global
    global Personas
    for i in range(len(Personas)):

        if nombre == Personas[i].getNomUsuario():
            #eliminar el objeto
            del Personas[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})


@app.route('/Doctor/<string:nombre>', methods=['DELETE'])
def EliminarDoc(nombre):
    # Referencia al arreglo global
    global Doctores

    for i in range(len(Doctores)):
        if nombre == Doctores[i].getNomUsuario():
            #eliminar el objeto

            del Doctores[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
    

@app.route('/Medicina/<int:ids>', methods=['DELETE'])
def EliminarMedicina(ids):
    # Referencia al arreglo global
    global Medicinas
    for i in range(len(Medicinas)):
        if ids == Medicinas[i].getId():
            del Medicinas[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/MedicinaFac', methods=['DELETE'])
def EliminarMedicinaPedido():
    # Referencia al arreglo global
    global MedicinaPedido
    for i in range(len(MedicinaPedido)):
        del MedicinaPedido[0]
    return jsonify({'Mensaje':'Eliminado'})        


@app.route('/MedicinaFac/<int:ids>', methods=['DELETE'])
def EliminarMedicinaPedidoBoton(ids):
    # Referencia al arreglo global
    global MedicinaPedido
    for i in range(len(MedicinaPedido)):
        if ids== MedicinaPedido[i].getId():
            del MedicinaPedido[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})        


if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)