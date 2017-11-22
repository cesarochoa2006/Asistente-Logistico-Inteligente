import openpyxl


class Repartidor:
    def __init__(self, nombre, envios):
        self.nombre = nombre
        self.envios = envios


class Envio:
    def __init__(self, celda,cliente, valorfact, fechamin, fechamax, fechaentrega, operador, fecharepro,direccion,prioridad,distancia):
        self.celda = celda
        self.cliente=cliente
        self.valorfact = valorfact
        self.fechamin = fechamin
        self.fechamax = fechamax
        self.fechaentrega = fechaentrega
        self.operador = operador
        self.fecharepro = fecharepro
        self.prioridad=prioridad
        self.distancia=distancia
        self.direccion = direccion

    def to_list(self):
        res = []
        res.append(self.celda)
        res.append(self.cliente)
        res.append(self.valorfact)
        res.append(self.fechamin)
        res.append(self.fechamax)
        res.append(self.fechaentrega)
        res.append(self.operador)
        res.append(self.direccion)
        res.append(self.prioridad)
        res.append(self.distancia)
        return res

def table_head(filepath):
    if filepath:
        doc = openpyxl.load_workbook(filepath)
        hoja1 = doc.get_sheet_by_name('Hoja1')
        doc.close()
        return ["N°",
            hoja1.cell(row=1,column=2).value,
            #hoja1.cell(row=1, column=3).value,
            hoja1.cell(row=1, column=4).value,
            hoja1.cell(row=1, column=6).value,
            hoja1.cell(row=1, column=7).value,
            hoja1.cell(row=1, column=8).value,
            hoja1.cell(row=1, column=10).value,
            #hoja1.cell(row=1, column=11).value,
            hoja1.cell(row=1, column=12).value,
            ]

def list_of_list(filepath):
    if filepath:
        doc = openpyxl.load_workbook(filepath)
        hoja1 = doc.get_sheet_by_name('Hoja1')

        lista_envios = []
        for i in range(93 - 1):
            cliente = hoja1.cell(row=i + 2, column=2).value  # se guarda la variable cliente
            factura = hoja1.cell(row=i + 2, column=3).value  # se guarda la variable factura
            valorfact = hoja1.cell(row=i + 2, column=4).value  # se guarda la variable valor de factura
            fechamin = hoja1.cell(row=i + 2, column=6).value  # se guarda la fecha minima
            fechamax = hoja1.cell(row=i + 2, column=7).value  # se guarda la fecha maxima
            fechaentrega = hoja1.cell(row=i + 2, column=8).value  # se guarda la fecha de entrega
            operador = hoja1.cell(row=i + 2, column=10).value  # se guarda el operador
            fecharepro = hoja1.cell(row=i + 2, column=11).value  # se guarda la reprogramacion
            direccion = hoja1.cell(row=i + 2, column=12).value  # se guarda la direccion
            fechamin = list(map(int, fechamin.strip().split("-")))
            fechamax = list(map(int, fechamax.strip().split("-")))
            fechaentrega = list(map(int, fechaentrega.strip().split("-")))



            envio = Envio(i + 2, cliente, valorfact, fechamin, fechamax, fechaentrega, operador, fecharepro, direccion,
                          0, 0)
            aux=envio.to_list()
            aux.pop(9)
            aux.pop(8)
            lista_envios.append(aux)
            doc.close()
        return lista_envios

def Obtenerlista(filepath):
    doc = openpyxl.load_workbook(filepath)
    # print(doc.get_sheet_names())
    hoja1 = doc.get_sheet_by_name('Hoja1')
    # print(hoja.cell(row=2,column=10).value)
    texto = ""
    lista_envios = []
    for i in range(93 - 1):
        cliente = hoja1.cell(row=i + 2, column=2).value#se guarda la variable cliente
        factura = hoja1.cell(row=i + 2, column=3).value#se guarda la variable factura
        valorfact = hoja1.cell(row=i + 2, column=4).value#se guarda la variable valor de factura
        fechamin = hoja1.cell(row=i + 2, column=6).value#se guarda la fecha minima
        fechamax = hoja1.cell(row=i + 2, column=7).value#se guarda la fecha maxima
        fechaentrega = hoja1.cell(row=i + 2, column=8).value#se guarda la fecha de entrega
        operador = hoja1.cell(row=i + 2, column=10).value#se guarda el operador
        fecharepro = hoja1.cell(row=i + 2, column=11).value#se guarda la reprogramacion
        direccion = hoja1.cell(row=i + 2, column=12).value#se guarda la direccion
        fechamin = list(map(int, fechamin.strip().split("-")))
        fechamax = list(map(int, fechamax.strip().split("-")))
        fechaentrega = list(map(int, fechaentrega.strip().split("-")))

        if(fechaentrega[1] == fechamax[1]):
          prioridad = fechaentrega[2]-fechamax[2]
        else:
          prioridad = fechaentrega[2]+30-fechamax[2]

        envio = Envio(i + 2,cliente, valorfact, fechamin, fechamax, fechaentrega, operador, fecharepro,direccion,prioridad,0)
        lista_envios.append(envio)
        # doc.save("DATOS.xlsx")
    doc.close()
    return lista_envios

def clasificacion_clase(lista_envios,kvecinos):
    clases_nombre =[]
    clases_valor=[]
    for i in range(kvecinos):
        if(lista_envios[i].operador in clases_nombre):
            #print("sumo")
            clases_valor[clases_nombre.index(lista_envios[i].operador)] = clases_valor[clases_nombre.index(lista_envios[i].operador)] + 1
        else:
            #print("creo")
            clases_nombre.append(lista_envios[i].operador)
            clases_valor.append(1)
    #print(clases_nombre)
    #print(clases_valor)
    #print("la clase ganadora es: "+str(clases_nombre[clases_valor.index(max(clases_valor))]))
    #return str(clases_nombre[clases_valor.index(max(clases_valor))])


def clasificador(lista_envios,objeto):
    #test data
    if len(objeto)<1:
        celda = 94
        cliente = "Almacenes Exito S.A."
        valorfact = "500000"
        fechamin = [ 17, 9, 5]
        fechamax = [ 17, 9, 9]
        fechaentrega = [0,0,0] #dato a clasificar
        operador = "" #dato a clasificar
        fecharepro = "NA/A"
        direccion = "Parque Industrial Malambo PIMSA"
    else:
        celda = objeto[0]
        cliente = objeto[1]
        valorfact = objeto[2]
        fechamin = objeto[3]
        fechamax = objeto[4]
        fechaentrega = [0, 0, 0]  # dato a clasificar
        operador = ""  # dato a clasificar
        fecharepro = objeto[5]
        direccion = objeto[6]
    envio_clasificar = Envio(celda,cliente, valorfact , fechamin, fechamax, fechaentrega, operador, fecharepro,direccion,0,0)
    lista_similares = []

    for i in range(len(lista_envios)):

        if(lista_envios[i].cliente == envio_clasificar.cliente):
            lista_envios[i].distancia = ((int(envio_clasificar.valorfact)-lista_envios[i].valorfact)**2)**(1/2)
            lista_similares.append(lista_envios[i])

    lista_similares.sort(key=lambda Envio: Envio.distancia)
    #mostrarListaEnvios(lista_similares);
    kvecinos= 5
    prioridad = 0
    #print(mostrarListaEnvios(lista_similares))
    for i in range(kvecinos):
        prioridad=prioridad +lista_similares[i].prioridad

    prioridad = prioridad/kvecinos
    operador=clasificacion_clase(lista_similares,kvecinos)
    #print(prioridad)

    envio_clasificar.fechaentrega = [fechamax[0],fechamax[1],fechamax[2]+int(prioridad)]
    envio_clasificar.operador = operador
    envio_clasificar.prioridad = int(prioridad)
    #print(mostrarEnvio(envio_clasificar))

#clasificador(Obtenerlista(),objetoaclasificar)