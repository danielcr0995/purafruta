import datetime as dt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter , A4
from reportlab.lib.units import cm

'''
class Pedidos:
    def __init__(self,fecha,nombre,apellido,codigocliente,aguacate,orito,maracuya,naranjas,papaya,pina,sandia):
        self.fecha=fecha
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.aguacate=aguacate
        self.orito=orito
        self.maracuya=maracuya
        self.naranjas=naranjas
        self.papaya=papaya
        self.pina=pina
        self.sandia=sandia
'''
class Pedidos:
    def __init__(self,fecha,nombre,apellido,codigocliente,sector,direccion,cantidades,precios,costos):#orden de precios y costos Piña Orito/kg Maracuya/kg Papaya/1	Verde/1	Sandia/1 Naranja/8 Limones/10 Aguacates	Platanos/10 miel

        self.fecha=fecha
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.sector=sector
        self.direccion=direccion  
        self.cantidades=cantidades
        self.precios=precios
        self.costos=costos

class Pedidos2:
    def __init__(self,fecha,nombre,apellido,codigocliente,sector,direccion,productos,cantidades,precios,costos):#orden de precios y costos Piña Orito/kg Maracuya/kg Papaya/1	Verde/1	Sandia/1 Naranja/8 Limones/10 Aguacates	Platanos/10 miel

        self.fecha=fecha
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.sector=sector
        self.direccion=direccion
        self.productos=productos  
        self.cantidades=cantidades
        self.precios=precios
        self.costos=costos        

class Clientes:
    def __init__(self,nombre,apellido,codigocliente,telefono,sector,direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.telefono=telefono
        self.sector=sector
        #self.urbanizacion=urbanizacion
        self.direccion=direccion

class Clientes2:
    def __init__(self,nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.telefono=telefono
        self.sector=sector
        self.urbanizacion=urbanizacion
        self.direccion=direccion

    #def codigocliente(self,nombre,apellido,sector):
"""      
file=open("clientes.txt","w")
file.write("nombre;apellido;codigocliente;telefono;sector;direccion")
file.close()
file2=open("pedidos.txt","w")
file2.write("nombre;apellido;codigocliente;fecha;aguacate;orito;maracuya;naranjas;papaya;pina;sandia")
file2.close()

"""

def sacarInfoPedido(archivo):#,fechaInicio):
    lista=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        #print(int(a[4][1]),int(a[4][2]),a[5],a[6])
        #print(a[6],len(a[6]))
        c=a[6][1:len(a[6])-1]
        cantidades=c.split(",")
        #print(cantidades)
        pr=a[7][1:len(a[7])-1]
        precios=pr.split(",")
        ct=a[8][1:len(a[8])-1]
        costos=ct.split(",")
        #pd=Pedidos(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10]) #clase anterior
        
        for i in range(len(cantidades)):
            cantidades[i]=float(cantidades[i])
            precios[i]=float(precios[i])
            costos[i]=float(costos[i])
        #print(cantidades,precios,costos)
        pd=Pedidos(float(a[0]),a[1],a[2],a[3],a[4],a[5],cantidades,precios,costos)
        lista.append(pd)
    file.close()
    return lista

def sacarInfoPedidoFecha(archivo,fechainicio,fechafin):#,fechaInicio):
    lista=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        #print(int(a[4][1]),int(a[4][2]),a[5],a[6])
        #print(a[6],len(a[6]))
        c=a[6][1:len(a[6])-1]
        cantidades=c.split(",")
        #print(cantidades)
        pr=a[7][1:len(a[7])-1]
        precios=pr.split(",")
        ct=a[8][1:len(a[8])-1]
        costos=ct.split(",")
        #pd=Pedidos(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10]) #clase anterior
        
        for i in range(len(cantidades)):
            cantidades[i]=float(cantidades[i])
            precios[i]=float(precios[i])
            costos[i]=float(costos[i])
        #print(cantidades,precios,costos)
        pd=Pedidos(float(a[0]),a[1],a[2],a[3],a[4],a[5],cantidades,precios,costos)
        if pd.fecha>=fechainicio and pd.fecha<=fechafin:
            lista.append(pd)
    file.close()
    return lista

def sacarInfoPedidoFecha2(archivo,fechainicio,fechafin):#,fechaInicio):
    lista=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        #print(int(a[4][1]),int(a[4][2]),a[5],a[6])
        #print(a[6],len(a[6]))
        pr=a[6][1:len(a[6]-1)]
        productos=pr.split(",")
        c=a[7][1:len(a[6])-1]
        cantidades=c.split(",")
        #print(cantidades)
        pr=a[8][1:len(a[7])-1]
        precios=pr.split(",")
        ct=a[9][1:len(a[8])-1]
        costos=ct.split(",")
        #pd=Pedidos(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10]) #clase anterior
        
        for i in range(len(cantidades)):
            cantidades[i]=float(cantidades[i])
            precios[i]=float(precios[i])
            costos[i]=float(costos[i])
        #print(cantidades,precios,costos)
        pd=Pedidos(float(a[0]),a[1],a[2],a[3],a[4],a[5],productos,cantidades,precios,costos)
        if pd.fecha>=fechainicio and pd.fecha<=fechafin:
            lista.append(pd)
    file.close()
    return lista

sacarInfoPedido("pedidos.txt")

def crearCliente(archivo):
    file=open(archivo,"a")
    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    telefono=input("Telfono: ")
    sector=input("Sector: ")
    
    direccion=input("Direccion: ")
    codigoCliente=nombre[0].capitalize()+apellido[0].capitalize()+sector[0:2].lower()
    file.write(nombre.Capitalize()+";"+apellido.capitalize()+";"+codigoCliente+";"+telefono+";"+sector+";"+direccion+"\n")
    file.close()

def crearCliente1(archivo):
    file=open(archivo,"a")
    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    telefono=input("Telfono: ")
    sector=input("Sector: ")
    direccion=input("Direccion: ")
    codigoCliente=nombre[0].capitalize()+apellido[0].capitalize()+sector[0:2].lower()
    file.write(nombre.title()+";"+apellido.title()+";"+codigoCliente+";"+telefono+";"+sector+";"+direccion+"\n")
    file.close()


#crearCliente("clientesprueba.txt")

def sacarInfoClientes(archivo):
    clientes=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        #print(a[1])
        cl=Clientes(a[0],a[1],a[2],a[3],a[4],a[5])
        clientes.append(cl)
    file.close()
    return clientes

def ordenarClientesSectores(archivo):
    clientes=sacarInfoClientes(archivo)
    sectores=["Miravalle","Cumbaya","Tumbaco","Quito"]
    lista=[]
    for sector in sectores:
        for cliente in clientes:
            if sector==cliente.sector:
                lista.append(cliente)

    return lista

def crearCliente2(archivo):
    clientes=sacarInfoClientes(archivo)
    file=open(archivo,"a")

    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    telefono=input("Telfono: ")
    sector=input("Sector: ")
    urbanizacion=input("Urabanizacion: ")
    direccion=input("Direccion: ")
    codigoCliente=nombre[0].capitalize()+apellido[0].capitalize()+sector[0:2].lower()
    #CLientes2: nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion
    cliente=Clientes2(nombre,apellido,codigoCliente,telefono,sector,urbanizacion,direccion)
    clientes.append(cliente)
    sectores=["Miravalle","Cumbaya","Tumbaco","Quito"]
    clientesordenados=[]
    for sector in sectores:
        for cliente in clientes:
            if sector==cliente.sector:
                clientesordenados.append(cliente)

    for cliente in clientesordenados:
        file.write(cliente.nombre.title()+";"+cliente.apellido.title()+";"+cliente.codigoCliente+";"+cliente.telefono+";"+cliente.sector+";"+cliente.urbanizacion+";"+cliente.direccion+"\n")
    
    
    file.close()

def agregarProducto(archivoproductos,productosls,preciosls,costosls):
    file=open(archivoproductos,"a")
    producto=input("Producto: ")
    precio=float(input("Precio: "))
    costo=float(input("Costo: "))
    file.write(producto.capitalize()+";"+str(precio)+";"+str(costo))
    #productosls.append(producto)
    #preciosls.append(precio)
    #costosls.append(costo)
    file.close()

def sacarInfoProductos(archivoproductos):
    file=open(archivoproductos,"r")
    file.readline()
    productos=[]
    precios=[]
    costos=[]
    for line in file:
        a=line.strip().split(";")
        #print(a[1])
        productos.append(a[0])
        precios.append(a[1])
        costos.append(a[2])

    file.close()
    return productos,precios,costos

#sacarInfoClientes("clientes.txt")

def ingresarPedido(archivoClientes,archivoPedidos,precios,costos):
    clientes=sacarInfoClientes(archivoClientes)
    pedidocliente=input("Codigo cliente o nombre: ")
    if len(pedidocliente)>4:
        nombre=pedidocliente.split(" ")
        nombre[0]=nombre[0].capitalize()
        nombre[1]=nombre[1].capitalize()
        print(nombre)
    for cliente in clientes:
        if pedidocliente==cliente.codigocliente or (nombre[0]==cliente.nombre and nombre[1]==cliente.apellido): #or codigoClienteIngresado==:
            file=open(archivoPedidos,"a")
            print("Pedido de:", cliente.nombre,cliente.apellido)
            f=dt.datetime.today()
            fecha=dt.datetime.timestamp(f)

            aguacates=int(input("aguacates: "))#
            orito=int(input("orito: "))#
            maracuya=int(input("marcuya: "))#
            naranjas=int(input("naranjas: "))#
            papaya=int(input("papaya: "))#
            verde=int(input("verde: "))#
            pina=int(input("pina: "))#
            sandia=int(input("sandia: "))#
            limones=int(input("limones: "))#
            platanos=int(input("platanos: "))
            miel=int(input("miel: "))

            cantidad=[pina,orito,maracuya,papaya,verde,sandia,naranjas,limones,aguacates,platanos, miel]
            #pina;orito;maracuya;papaya;verde;sandia;naranjas;limones;aguacates;platanos; miel
            """
            precioaguacates=0.50 #unidades
            precioorito=1.25 #kg
            preciomaracuya=1.25 #kg
            precionaranjas=1 #8uds
            preciopapaya=0.50 #ud
            preciopina=1.25 #ud
            preciosandia=5 #ud
            preciolimones=1 #10 uds
            """

            pago=cantidad[0]*preciopina+cantidad[1]*precioorito+cantidad[2]*preciomaracuya+cantidad[3]*preciopapaya+cantidad[4]*precioverde+cantidad[5]*preciosandia+cantidad[6]*precionaranjas+cantidad[7]*preciolimones+cantidad[8]*precioaguacates+cantidad[9]*precioplatanos+cantidad[10]*preciomiel

            """
            costoaguacates=1
            costoorito=2
            costomaracuya=3
            costonaranjas=4
            costopapaya=1
            costopina=1
            costosandia=1
            """

            gastos=-(cantidad[0]*costopina+cantidad[1]*costoorito+cantidad[2]*costomaracuya+cantidad[3]*costopapaya+cantidad[4]*costoverde+cantidad[5]*costosandia+cantidad[6]*costonaranjas+cantidad[7]*costolimones+cantidad[8]*costoaguacates+cantidad[9]*costoplatanos+cantidad[10]*costomiel)

            ganancia=pago+gastos
            '''
            file.write(str(fecha)+";"+cliente.nombre+";"+cliente.apellido+";"+cliente.codigocliente+";")
            file.write(str(aguacates)+";"+str(orito)+";"+str(maracuya)+";"+str(naranjas)+";"+str(papaya)+";"+str(pina)+";"+str(sandia)+";"+str(pago)+";"+str(gastos)+";"+str(ganancia)+";")
            file.write(str(precioaguacates)+";"+str(precioorito)+";"+str(preciomaracuya)+";"+str(precionaranjas)+";"+str(preciopapaya)+";"+str(preciopina)+";"+str(preciosandia)+";")
            file.write(str(costoaguacates)+";"+str(costoorito)+";"+str(costomaracuya)+";"+str(costonaranjas)+";"+str(costopapaya)+";"+str(costopina)+";"+str(costosandia)+"\n")
            '''
            file.write(str(fecha)+";"+cliente.nombre+";"+cliente.apellido+";"+cliente.codigocliente+";"+cliente.sector+";"+cliente.direccion+";"+str(cantidad)+";"+str(precios)+";"+str(costos)+"\n")
            file.close()

def ingresarPedido2(archivoClientes,archivoPedidos,precios,costos,productos):
    clientes=sacarInfoClientes(archivoClientes)
    pedidocliente=input("Codigo cliente o nombre: ")
    file=open(archivoPedidos,"a")
    f=dt.datetime.today()
    fecha=dt.datetime.timestamp(f)
    if len(pedidocliente)>4:
        '''
        nombre=pedidocliente.split(" ")
        nombre[0]=nombre[0].capitalize()
        nombre[1]=nombre[1].capitalize()
        '''
        pedidocliente=pedidocliente.split(" ")
        pedidocliente[0]=pedidocliente[0].capitalize()
        pedidocliente[1]=pedidocliente[1].capitalize()
        #print(pedidocliente)
    for cliente in clientes:
        #print(cliente.nombre)
        #print(nombre)
        if pedidocliente==cliente.codigocliente or (pedidocliente[0]==cliente.nombre and pedidocliente[1]==cliente.apellido): #or codigoClienteIngresado==:

#        if pedidocliente==cliente.codigocliente or (nombre[0]==cliente.nombre and nombre[1]==cliente.apellido): #or codigoClienteIngresado==:
            #file=open(archivoPedidos,"a")
            print("Pedido de:", cliente.nombre,cliente.apellido)
            #f=dt.datetime.today()
            #fecha=dt.datetime.timestamp(f)
            cantidades=[]
            
            for producto in productos:
                cantidad=float(input(producto+": "))
                cantidades.append(cantidad)
            
            #cantidad=[pina,orito,maracuya,papaya,verde,sandia,naranjas,limones,aguacates,platanos, miel]
            #pina;orito;maracuya;papaya;verde;sandia;naranjas;limones;aguacates;platanos; miel
            # 
            total=0
            tlinea=30#tamno linea
            print(tlinea*"*")
            print("Pedido de:", cliente.nombre,cliente.apellido)
            print(tlinea*"-")
            for i in range(len(productos)):
                
                if cantidades[i]==0:
                    #print(cantidades[i])
                    pass
                else:
                    #print("Pedido de:", cliente.nombre,cliente.apellido)
                    precio=cantidades[i]*precios[i]
                    #print(len(str(cantidad[i])))
                    #print(cantidades[i])
                    espacio=tlinea-len(str(cantidades[i]))-len(str(productos[i]))-len(str(round(precio,2)))-4
                    print(str(cantidades[i])+" "+productos[i]+" "*espacio+" $ "+str(precio) )
                    total+=precio
            print(tlinea*"-")
            print("Total"+ (tlinea-len("Total")-len(str(round(total,2)))-4)*" "+" $ "+ str(round(total,2)))    
          
            file.write(str(fecha)+";"+cliente.nombre+";"+cliente.apellido+";"+cliente.codigocliente+";"+cliente.sector+";"+cliente.direccion+";"+str(cantidades)+";"+str(precios)+";"+str(costos)+"\n")
    file.close()

def ingresarPedido3(archivoClientes,archivoPedidos,archivoProductos):
    productos,precios,costos=sacarInfoProductos(archivoProductos)
    clientes=sacarInfoClientes(archivoClientes)
    pedidocliente=input("Codigo cliente o nombre: ")
    file=open(archivoPedidos,"a")
    f=dt.datetime.today()
    fecha=dt.datetime.timestamp(f)
    if len(pedidocliente)>4:
        '''
        nombre=pedidocliente.split(" ")
        nombre[0]=nombre[0].capitalize()
        nombre[1]=nombre[1].capitalize()
        '''
        pedidocliente=pedidocliente.split(" ")
        pedidocliente[0]=pedidocliente[0].capitalize()
        pedidocliente[1]=pedidocliente[1].capitalize()
        #print(pedidocliente)
    for cliente in clientes:
        #print(cliente.nombre)
        #print(nombre)
        if pedidocliente==cliente.codigocliente or (pedidocliente[0]==cliente.nombre and pedidocliente[1]==cliente.apellido): #or codigoClienteIngresado==:

#        if pedidocliente==cliente.codigocliente or (nombre[0]==cliente.nombre and nombre[1]==cliente.apellido): #or codigoClienteIngresado==:
            #file=open(archivoPedidos,"a")
            print("Pedido de:", cliente.nombre,cliente.apellido)
            #f=dt.datetime.today()
            #fecha=dt.datetime.timestamp(f)
            cantidadesfl=[]#guardados en el archivo
            productosfl=[] #guardados en el archivo
            preciosfl=[] #guardados en el archivo
            costosfl=[] #guardados en el archivo
            for i in range(len(productos)):
            #for producto in productos:
                
                cantidad=float(input(productos[i]+": "))
                if cantidad==0:
                    pass
                else:
                    productosfl.append(productos[i])
                    preciosfl.append(precios[i])
                    costosfl.append(costos[i])
                    cantidadesfl.append(cantidad)
            
            #cantidad=[pina,orito,maracuya,papaya,verde,sandia,naranjas,limones,aguacates,platanos, miel]
            #pina;orito;maracuya;papaya;verde;sandia;naranjas;limones;aguacates;platanos; miel
            # 
            total=0
            tlinea=30#tamno linea
            print(tlinea*"*")
            print("Pedido de:", cliente.nombre,cliente.apellido)
            print(tlinea*"-")
            for i in range(len(productosfl)):
                
                if cantidadesfl[i]==0:
                    #print(cantidades[i])
                    pass
                else:
                    #print("Pedido de:", cliente.nombre,cliente.apellido)
                    precio=cantidadesfl[i]*preciosfl[i]
                    #print(len(str(cantidad[i])))
                    #print(cantidades[i])
                    espacio=tlinea-len(str(cantidadesfl[i]))-len(str(productosfl[i]))-len(str(round(precio,2)))-4
                    print(str(cantidadesfl[i])+" "+productosfl[i]+" "*espacio+" $ "+str(precio) )
                    total+=precio
            print(tlinea*"-")
            print("Total"+ (tlinea-len("Total")-len(str(round(total,2)))-4)*" "+" $ "+ str(round(total,2)))    
          
            file.write(str(fecha)+";"+cliente.nombre+";"+cliente.apellido+";"+cliente.codigocliente+";"+cliente.sector+";"+cliente.direccion+";")
            file.write(str(productosfl)+";"+str(cantidadesfl)+";"+str(preciosfl)+";"+str(costosfl)+"\n")
    file.close()
            
precioaguacates=0.50 #unidades
precioorito=1.25 #kg
preciomaracuya=1.25 #kg
precionaranjas=1 #8uds
preciopapaya=0.50 #ud
preciopina=1.25 #ud
preciosandia=5 #ud
preciolimones=1 #10 uds
precioverde=0.35 #ud
precioplatanos=1.5 #10uds
preciomiel=4 #frasco 
preciomanzanas=1 #5uds
precioperas=1 #5uds
preciofrutillas=2 #caja 500gr

costoaguacates=1
costoorito=2
costomaracuya=3
costonaranjas=4
costopapaya=1
costopina=1
costosandia=1
costolimones=1 #10 uds
costoverde=0.35 #ud
costoplatanos=1.5 #10uds
costomiel=4 #frasco
costomanzanas=0.6 #5uds
costoperas=0.6 #5uds 
costofrutillas=1.5 #caja 500gr

#orden de precios y costos Piña Orito/kg Maracuya/kg Papaya/1	Verde/1	Sandia/1 Naranja/8 Limones/10 Aguacates	Platanos/10 miel

productos=["Pina","Orito","Maracuya","Papaya","Verde","Sandia","Naranjas","Limones","Aguacates","Platanos","Miel","Manzanas","Peras","Frutillas"]
precios=[preciopina,precioorito,preciomaracuya,preciopapaya,precioverde,preciosandia,precionaranjas,preciolimones,precioaguacates,precioplatanos,preciomiel,preciomanzanas,precioperas,preciofrutillas]
costos=[costopina,costoorito,costomaracuya,costopapaya,costoverde,costosandia,costonaranjas,costolimones,costoaguacates,costoplatanos,costomiel,costomanzanas,costoperas,costofrutillas]

#ingresarPedido2("clientesprueba.txt","pedidosprueba.txt",precios,costos,productos)


#agregarProducto()


'''
def imprimirPedidos(archivoclientes,archivopedidos):#fechaInicio):
    clientes=sacarInfoClientes(archivoclientes)
    pedidos=sacarInfoPedido(archivopedidos)#fechaInicio)
    for pedido in pedidos:
        if pedido.fecha>=fecha:
            f=dt.fromtimestamp(fecha)
            nombrepdf="pedidos_"+str(f.year)+str(f.month)+str(f.day)+".pdf"
            c=canvas.Canvas(nombrepdf,pagesize=letter)
            c.drawCentredString(415,500, pedido.nombre)
'''

cl=sacarInfoClientes("clientesprueba.txt")
pe=sacarInfoPedido("pedidos.txt")
#print(len(pe))

#for pedido in pe:
#    print(pedido.cantidades,pedido.precios,pedido.costos)

def imprimirPedidoInd(nombre,apellido,direccion,sector,tamanox,tamanoy,documento,productos,cantidad,precios, movex,movey,numeropedido): #,posinicialx,posinicialy
    cliente=nombre+" "+apellido
    #poscliente= (tamanolinea-len(cliente))/2
    centerText=lambda tamanolineax, texto: (tamanox-len(texto)/2)/2
    tlinea=100
    posclientex= centerText(tamanox,cliente)
    possector=centerText(tamanox,sector)
    posdireccion=centerText(tamanox,direccion)
    documento.drawString(posclientex+movex*tamanox/1,tamanoy-20-movey*tamanoy/2,cliente) #imprime el nombre 
    documento.drawString(posclientex+movex*tamanox/1,tamanoy-40-movey*tamanoy/2,sector)
    
    posimprimirdireccion=tamanoy-40
    letraspagina=30
    for i in range((len(direccion)//letraspagina)+1):
        posimprimirdireccion-=20
        documento.drawString(30+movex*tamanox/1,posimprimirdireccion-movey*tamanoy/2,direccion[i*letraspagina:(i+1)*letraspagina])
    
    documento.drawString(20+movex*tamanox/1,(posimprimirdireccion-10)-movey*tamanoy/2,"-"*(tlinea-40))
    posImprimirproductos=tamanoy-(posimprimirdireccion-20)
    
    #documento.drawString(30+movex*tamanox/1,tamanoy-60-movey*tamanoy/2,direccion)
    #documento.drawString(20+movex*tamanox/1,tamanoy-posimprimirdireccion-10-movey*tamanoy/2,"-"*(tlinea-40))
    posImprimirproductos=posimprimirdireccion-30
    preciototal=0
    separacionprecio=200
    #numeropedido=0
    for i in range(len(productos)):
        #numeropedido+=1
        if cantidad[i]==0:
            pass
        else:
            documento.drawString(30+movex*tamanox/1,tamanoy-20-movey*tamanoy/2,str(numeropedido))
            #documento.drawString(-30+movex*tamanox/1,tamanoy-20-movey*tamanoy/2,str(numeropedido))
            sep=tlinea-len(str(productos[i]))-len(str(precios[i]*cantidad[i]))-1-20-len(str(cantidad[i]))-2#-1 de $ y -2 de espacios
            #print(sp)
            #linea=str(cantidad[i])+"  "+str(productos[i])+" "*sep+" $ "+str(precios[i]*cantidad[i])
            lineaprod=str(cantidad[i])+"  "+str(productos[i])
            lineapr=" $ "+str(round(precios[i]*cantidad[i],2))
            #print(linea)
            #documento.drawString(20,posImprimirproductos,linea)
            documento.drawString(20+movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,lineaprod)
            documento.drawString(separacionprecio+movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,lineapr)
            posImprimirproductos-=20
            preciototal+=precios[i]*cantidad[i]

    documento.drawString(20 +movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,"-"*(tlinea-40))
    #print(preciototal)
    separacionTotal=tlinea-len("Total ")-len(str(preciototal))-1-2 #-1 for $ symbol
    #print(separacionTotal)
    #lineat=" Total "+" "*separacionTotal+" $ "+str(preciototal)
    lineat=" Total "
    lineatpr=" $ "+str(round(preciototal,2))
    
    #documento.drawString(20,posImprimirproductos-30,lineat)
    documento.drawString(20+movex*tamanox/1,posImprimirproductos-20-movey*tamanoy/2,lineat)
    documento.drawString(separacionprecio+movex*tamanox/1,posImprimirproductos-20-movey*tamanoy/2,lineatpr)
    #documento.save()

'''
c=canvas.Canvas("prueba.pdf",pagesize=A4)
width,height=A4
#c.translate(cm,cm)
width,height=A4
#print(width)
#c.drawString(0,0,"000111222333444555666777888999"*int(width/40))

c.drawString(6.5,0,"000111222333444555666777888999"*int(width/40))
for i in range(0,int(height),2):
        c.drawString(int(width)/2,i+1,"|")
for j in range(0,int(width),2):
    c.drawString(j+1,int(height)/2,"-")
#print(pe[0].precio

for pedido in pe:
    for cliente in cl:
        print(cliente)
        if cliente.nombre==pedido.nombre and cliente.apellido==pedido.apellido and cliente.codigocliente==pedido.codigocliente:
            dieccion=cliente.direccion
            sector=cliente.sector
productos=["Pina","Orito","Maracuya","Papaya","Verde","Sandia","Naranjas","Limones","Aguacates","Platanos","Miel"]
'''
#imprimirPedidoInd(cl[0].nombre,cl[0].apellido,cl[0].direccion,cl[0].sector,int(width)/2,int(height),c,productos,pe[0].cantidades,pe[0].precios,0,1)  


def imprimirPaginaPedido(documento):
    for i in range(0,int(height),2):
        documento.drawString(int(width)/2,i+1,"|")
    for j in range(0,int(width),2):
        documento.drawString(j+1,int(height)/2,"-")
    
    

    for  h in range(2):
        for w in range(2):
            #imprimirPedidoInd(cl[h+w].nombre,cl[h+w].apellido,cl[h+w].direccion,cl[h+w].sector,int(width)/2,int(height),c,productos,pe[h+w].cantidades,pe[h+w].precios,w,h)
                #for pedido in pe:
            for pedido in pe:
                for cliente in cl:
                    print(pedido.nombre)
                    if cliente.nombre==pedido.nombre and cliente.apellido==pedido.apellido and cliente.codigocliente==pedido.codigocliente:
                        dieccion=cliente.direccion
                        sector=cliente.sector
                        #productos=["Pina","Orito","Maracuya","Papaya","Verde","Sandia","Naranjas","Limones","Aguacates","Platanos","Miel"]
                        '''for  h in range(2):
                            for w in range(2):'''
                        imprimirPedidoInd(cliente.nombre,cliente.apellido,cliente.direccion,cliente.sector,int(width)/2,int(height),documento,productos,pedido.cantidades,pedido.precios,w,h)
                    
    documento.save()       

#productos=["Pina","Orito","Maracuya","Papaya","Verde","Sandia","Naranjas","Limones","Aguacates","Platanos","Miel"]

#imprimirPaginaPedido(c)
def dividirPaginas(documento,height,width):
    for i in range(0,int(height),2):
        documento.drawString(int(width)/2,i+1,"|")
    for j in range(0,int(width),2):
        documento.drawString(j+1,int(height)/2,"-")

#width,height=A4
#c.translate(cm,cm)
#width,height=A4  
#paginas=len(pe)//4

def imprimirPedidos(nombrearcivo,width,height,pedidos,productos):

    documento=canvas.Canvas(nombrearchivo,pagesize=A4)
    paginas=len(pedidos)//4
    #if len(pe)/4!=0:
    #    paginas+=0

    #print(pe[7])
    #for i in range(paginas):
    for n in range(paginas):
        #print(n)
        dividirPaginas(documento,height,width)
        imprimirPedidoInd(pedidos[0+4*n].nombre,pedidos[0+4*n].apellido,pedidos[0+4*n].direccion,pedidos[0+4*n].sector,int(width)/2,int(height),documento,productos,pedidos[0+4*n].cantidades,pedidos[0+4*n].precios,0,0,0+4*n+1)
        imprimirPedidoInd(pedidos[1+4*n].nombre,pedidos[1+4*n].apellido,pedidos[1+4*n].direccion,pedidos[1+4*n].sector,int(width)/2,int(height),documento,productos,pedidos[1+4*n].cantidades,pedidos[1+4*n].precios,1,0,1+4*n+1)
        imprimirPedidoInd(pedidos[2+4*n].nombre,pedidos[2+4*n].apellido,pedidos[2+4*n].direccion,pedidos[2+4*n].sector,int(width)/2,int(height),documento,productos,pedidos[2+4*n].cantidades,pedidos[2+4*n].precios,0,1,2+4*n+1)
        imprimirPedidoInd(pedidos[3+4*n].nombre,pedidos[3+4*n].apellido,pedidos[3+4*n].direccion,pedidos[3+4*n].sector,int(width)/2,int(height),documento,productos,pedidos[3+4*n].cantidades,pedidos[3+4*n].precios,1,1,3+4*n+1)
        documento.showPage()
    #dividirPaginas(documento,height,width)
    possobraninicial=paginas*4
    possobran=len(pedidos)
    
    if len(pedidos)%4==3:
        imprimirPedidoInd(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        imprimirPedidoInd(pedidos[possobraninicial+1].nombre,pedidos[possobraninicial+1].apellido,pedidos[possobraninicial+1].direccion,pedidos[possobraninicial+1].sector,int(width)/2,int(height),documento,productos,pedidos[possobraninicial+1].cantidades,pedidos[possobraninicial+1].precios,1,0,possobraninicial+1+1)
        imprimirPedidoInd(pedidos[possobraninicial+2].nombre,pedidos[possobraninicial+2].apellido,pedidos[possobraninicial+2].direccion,pedidos[possobraninicial+2].sector,int(width)/2,int(height),documento,productos,pedidos[possobraninicial+2].cantidades,pedidos[possobraninicial+2].precios,0,1,possobraninicial+2+1)
        dividirPaginas(documento,height,width)
    elif len(pedidos)%4==2:
        imprimirPedidoInd(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        imprimirPedidoInd(pedidos[possobraninicial+1].nombre,pedidos[possobraninicial+1].apellido,pedidos[possobraninicial+1].direccion,pedidos[possobraninicial+1].sector,int(width)/2,int(height),documento,productos,pedidos[possobraninicial+1].cantidades,pedidos[possobraninicial+1].precios,1,0,possobraninicial+1+1)
        dividirPaginas(documento,height,width)
    elif len(pedidos)%4==1:
        imprimirPedidoInd(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        dividirPaginas(documento,height,width)
    documento.save()

#cl=sacarInfoClientes("clientes.txt")
#pe=sacarInfoPedido("pedidos.txt")
#width,height=A4
#c.translate(cm,cm)
width,height=A4  
#paginas=len(pe)//4
#productos=["Pina","Orito","Maracuya","Papaya","Verde","Sandia","Naranjas","Limones","Aguacates","Platanos","Miel","Manzanas","Peras","Frutillas"]
ano=2020
mes=4
dia=10
fechai=dt.datetime(ano,mes,dia)
fechainicio=str(fechai.year)+str(fechai.month)+str(fechai.day)#fechai.strtime("%d%m%y")
fechaf=dt.datetime.today()
fechafin=str(fechaf.year)+str(fechaf.month)+str(fechaf.day)#fechaf.strtime("%d%m%y")#str(fecahf.year)+str(fecahf.month)+str(fecahf.day)
nombrearchivo="pedidos4444_"+fechainicio+"_"+fechafin+".pdf"
#print(nombrearchivo)
fechainiciopedidos=dt.datetime.timestamp(fechai)
fechafinpedidos=dt.datetime.timestamp(fechaf)
pedidosimprimir=sacarInfoPedidoFecha("pedidos060520_22.dat",fechainiciopedidos,fechafinpedidos)
#print(len(pedidosimprimir))
#paginas=len(pe)//4
productos,precios,costos=sacarInfoProductos("productosprueba.dat")
print(precios)
imprimirPedidos(nombrearchivo,width,height,pedidosimprimir,productos)

def imprimirPedido(cliente,pedido):
    f= pedido.fecha
    fecha=dt.datetime.fromtimestamp(float(f))
    ano=fecha.year
    mes=fecha.month
    dia=fecha.day
    #nombrepdf="pedidos_"+str(f.year)+str(f.month)+str(f.day)+".pdf"
    width,height=letter #width=612,height=792
    c=canvas.Canvas("prueba.pdf",pagesize=letter)
    cl=pedido.nombre + pedido.apellido
    c.drawCentredString(100,782,cl)
    c.drawCentredString(110,772,cl)
    #dividir la pagin en 4
    for i in range(0,int(height),2):
        c.drawString(int(width)/2,i+1,"|")
    for j in range(0,int(width),2):
        c.drawString(j+1,int(height)/2,"-")

    for i in range(2):
        for j in range(2):
            pass   
    c.save()

#imprimirPedido(cl[0],pe[0])
'''
    c=canvas.Canvas(nombrearchivo,pagesize=A4)
    width,height=A4
    #c.translate(cm,cm)
    width,height=A4  
    paginas=len(pe)//4
    #if len(pe)/4!=0:
    #    paginas+=0

    #print(pe[7])
    #for i in range(paginas):
    for n in range(paginas):
        print(n)
        dividirPaginas(c,height,width)
        imprimirPedidoInd(pe[0+4*n].nombre,pe[0+5*n].apellido,pe[0+5*n].direccion,pe[0+5*n].sector,int(width)/2,int(height),c,productos,pe[0+5*n].cantidades,pe[0+5*n].precios,0,0)
        imprimirPedidoInd(pe[1+4*n].nombre,pe[1+5*n].apellido,pe[1+5*n].direccion,pe[1+5*n].sector,int(width)/2,int(height),c,productos,pe[1+5*n].cantidades,pe[1+5*n].precios,1,0)
        imprimirPedidoInd(pe[2+4*n].nombre,pe[1+5*n].apellido,pe[2+5*n].direccion,pe[2+5*n].sector,int(width)/2,int(height),c,productos,pe[2+5*n].cantidades,pe[2+5*n].precios,0,1)
        imprimirPedidoInd(pe[3+4*n].nombre,pe[3+5*n].apellido,pe[3+5*n].direccion,pe[3+5*n].sector,int(width)/2,int(height),c,productos,pe[3+5*n].cantidades,pe[3+5*n].precios,1,1)
        c.showPage()
        #dividirPaginas(c,height,width)
    possobraninicial=paginas*4
    possobran=len(pe)
    dividirPaginas(c,height,width)
    if len(pe)%4==3:
        imprimirPedidoInd(pe[possobraninicial].nombre,pe[0+5*n].apellido,pe[0+5*n].direccion,pe[0+5*n].sector,int(width)/2,int(height),c,productos,pe[0+5*n].cantidades,pe[0+5*n].precios,0,0)
        imprimirPedidoInd(pe[possobraninicial+1].nombre,pe[1+5*n].apellido,pe[1+5*n].direccion,pe[1+5*n].sector,int(width)/2,int(height),c,productos,pe[1+5*n].cantidades,pe[1+5*n].precios,1,0)
        imprimirPedidoInd(pe[possobraninicial+2].nombre,pe[1+5*n].apellido,pe[2+5*n].direccion,pe[2+5*n].sector,int(width)/2,int(height),c,productos,pe[2+5*n].cantidades,pe[2+5*n].precios,0,1)
    elif len(pe)%4==2:
        imprimirPedidoInd(pe[possobraninicial].nombre,pe[0+5*n].apellido,pe[0+5*n].direccion,pe[0+5*n].sector,int(width)/2,int(height),c,productos,pe[0+5*n].cantidades,pe[0+5*n].precios,0,0)
        imprimirPedidoInd(pe[possobraninicial+1].nombre,pe[1+5*n].apellido,pe[1+5*n].direccion,pe[1+5*n].sector,int(width)/2,int(height),c,productos,pe[1+5*n].cantidades,pe[1+5*n].precios,1,0)
    elif len(pe)%4==1:
        imprimirPedidoInd(pe[possobraninicial].nombre,pe[0+5*n].apellido,pe[0+5*n].direccion,pe[0+5*n].sector,int(width)/2,int(height),c,productos,pe[0+5*n].cantidades,pe[0+5*n].precios,0,0)
    c.save()
'''
clientess=sacarInfoClientes("clientesprueba2.data")
pedidoss=sacarInfoPedido("pedidosprueba2.txt")
def ordenarentregas(pedidos,clientes):
    lista=[]
    for cliente in clientes:

        for pedido in pedidos:

            if cliente.nombre==pedido.nombre and cliente.apellido==pedido.apellido and cliente.codigocliente==pedido.codigocliente:
                lista.append(pedido)

    return lista


#entregas=ordenarentregas(pedidoss,clientess)
#print("hola",len(entregas),len(pedidoss),len(clientess))
#for entrega in entregas:
    #print(entrega.nombre,entrega.apellido)
def printhola():
    print("hola")

