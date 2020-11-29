import datetime as dt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter , A4
from reportlab.lib.units import cm

class Pedidos2:
    def __init__(self,fecha,nombre,apellido,codigocliente,sector,urbanizacion,direccion,productos,cantidades,precios,costos):#orden de precios y costos Piña Orito/kg Maracuya/kg Papaya/1	Verde/1	Sandia/1 Naranja/8 Limones/10 Aguacates	Platanos/10 miel

        self.fecha=fecha
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.sector=sector
        self.urbanizacion=urbanizacion
        self.direccion=direccion
        self.productos=productos  
        self.cantidades=cantidades
        self.precios=precios
        self.costos=costos



class Pedidos3:
    def __init__(self,fecha,nombre,apellido,codigocliente,sector,urbanizacion,direccion,productos,cantidades,precios,costos,pago):#orden de precios y costos Piña Orito/kg Maracuya/kg Papaya/1	Verde/1	Sandia/1 Naranja/8 Limones/10 Aguacates	Platanos/10 miel

        self.fecha=fecha
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.sector=sector
        self.urbanizacion=urbanizacion
        self.direccion=direccion
        self.productos=productos  
        self.cantidades=cantidades
        self.precios=precios
        self.costos=costos
        self.pago=pago


class Clientes2:
    def __init__(self,nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.telefono=telefono
        self.sector=sector
        self.urbanizacion=urbanizacion
        self.direccion=direccion

def sacarInfoPedidos(archivo):#,fechaInicio):
    lista=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        #print(int(a[4][1]),int(a[4][2]),a[5],a[6])
        #print(a[7],len(a[7]))
        prod=a[7][1:len(a[7])-1]
        #prod=prod.replace("' ","")
        
        
        productos=prod.split(",")
        #print(productos)
        #print(pro)
        #productos=a[7]
        c=a[8][1:len(a[8])-1]
        cantidades=c.split(",")
        print(cantidades)
        pr=a[9][1:len(a[9])-1]
        precios=pr.split(",")
        ct=a[10][1:len(a[10])-1]
        costos=ct.split(",")
        #pd=Pedidos(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10]) #clase anterior
        '''
        for i in range(len(cantidades)):
            cantidades[i]=float(cantidades[i])
            precios[i]=float(precios[i])
            costos[i]=float(costos[i])     
            productos[i]=productos[i].replace(" ","").replace("'","")'''
        
        #print(cantidades,precios,costos)
        pd=Pedidos2(float(a[0]),a[1],a[2],a[3],a[4],a[5],productos,cantidades,precios,costos)
        lista.append(pd)
    file.close()
    return lista

def sacarInfoPedidoFecha2(archivo,fechainicio,fechafin):#,fechaInicio):
    lista=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        #fecha,nombre,apellido,codigocliente,sector,urbanizacion,direccion,productos,cantidades,precios,costos
        fecha=float(a[0])
        nombre=a[1]
        apellido=a[2]
        codigocliente=a[3]
        sector=a[4]
        urbanizacion=a[5]
        direccion=a[6]
        #print(int(a[4][1]),int(a[4][2]),a[5],a[6])
        #print(a[1],a[10],a[10][1:len(a[10])-1])
        prod=a[7][1:len(a[7])-1]
        #prod=prod.replace("' ","") 
        
        productos=prod.split(",")
        #print(productos)
        #print(pro)
        #productos=a[7]
        c=a[8][1:len(a[8])-1]
        cantidades=c.split(",")
        #print(cantidades)
        pr=a[9][1:len(a[9])-1]
        precios=pr.split(",")
        #print(precios)
        
        ct=a[10][1:len(a[10])-1]
        costos=ct.split(",")
        #print(costos)
        #pd=Pedidos(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10]) #clase anterior
        #print(a[1])
        for i in range(len(productos)):
            cantidades[i]=float(cantidades[i])
            precios[i]=float(precios[i])
            costos[i]=float(costos[i])     
            productos[i]=productos[i].replace(" '","").replace("'","")
        
        #print(nombre,productos,cantidades,costos)
        
        #fecha,nombre,apellido,codigocliente,sector,urbanizacion,direccion,productos,cantidades,precios,costos
        pd=Pedidos2(fecha,nombre,apellido,codigocliente,sector,urbanizacion,direccion,productos,cantidades,precios,costos)
        if pd.fecha>=fechainicio and pd.fecha<=fechafin:
            lista.append(pd)
    file.close()
    return lista

def sacarInfoPedidoFecha3(archivo,fechainicio,fechafin):#,fechaInicio):
    lista=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        fecha=float(a[0])
        nombre=a[1]
        apellido=a[2]
        codigocliente=a[3]
        sector=a[4]
        urbanizacion=a[5]
        direccion=a[6]
        pago=a[7]
        prod=a[8][1:len(a[8])-1]        
        productos=prod.split(",")
        c=a[9][1:len(a[9])-1]
        cantidades=c.split(",")
        pr=a[10][1:len(a[10])-1]
        precios=pr.split(",")        
        ct=a[11][1:len(a[11])-1]
        costos=ct.split(",")
        for i in range(len(productos)):
            cantidades[i]=float(cantidades[i])
            precios[i]=float(precios[i])
            costos[i]=float(costos[i])     
            productos[i]=productos[i].replace(" '","").replace("'","")
        
        pd=Pedidos2(fecha,nombre,apellido,codigocliente,sector,urbanizacion,direccion,pago,productos,cantidades,precios,costos)
        if pd.fecha>=fechainicio and pd.fecha<=fechafin:
            lista.append(pd)
    file.close()
    return lista

def sacarInfoPedidoFecha4(archivo,fechainicio,fechafin):#,fechaInicio):
    lista=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        fecha=float(a[0])
        nombre=a[1]
        apellido=a[2]
        codigocliente=a[3]
        sector=a[4]
        urbanizacion=a[5]
        direccion=a[6]
        pago=a[7]
        prod=a[8][1:len(a[8])-1]        
        productos=prod.split(",")
        c=a[9][1:len(a[9])-1]
        cantidades=c.split(",")
        pr=a[10][1:len(a[10])-1]
        precios=pr.split(",")        
        ct=a[11][1:len(a[11])-1]
        costos=ct.split(",")
        pago=a[12]
        for i in range(len(productos)):
            cantidades[i]=float(cantidades[i])
            precios[i]=float(precios[i])
            costos[i]=float(costos[i])     
            productos[i]=productos[i].replace(" '","").replace("'","")
        
        pd=Pedidos3(fecha,nombre,apellido,codigocliente,sector,urbanizacion,direccion,pago,productos,cantidades,precios,costos,pago)
        if pd.fecha>=fechainicio and pd.fecha<=fechafin:
            lista.append(pd)
    file.close()
    return lista

#sacarInfoPedidoFecha2("pedidosprueba3.dat",dt.datetime.today(),dt.datetime.today())
def crearCliente3(archivo):
    clientes=sacarInfoClientes2(archivo)
    file=open(archivo,"a")

    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    telefono=input("Telfono: ")
    sectores=["Miravalle","Nayon","Cumbaya","Lumbisi","La Primavera","Tumbaco","Puembo","Quito"]
    for i in range(len(sectores)):
        print(i+1, sectores[i])
    sector=int(input("Sector: "))
    #print(sector)
    urbanizacion=input("Urbanizacion: ")
    direccion=input("Direccion: ")
    codigoCliente=nombre[0].capitalize()+apellido[0].capitalize()+sectores[sector-1][0:2].lower()
    #CLientes2: nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion
    clienten=Clientes2(nombre,apellido,codigoCliente,telefono,sectores[sector-1],urbanizacion,direccion)
    clientes.append(clienten)
    #print(clienten)
    
    clientesordenados=[]
    for sector in sectores:
        for cliente in clientes:
            if sector==cliente.sector:
                clientesordenados.append(cliente)

    for cliente in clientesordenados:
        file.write(cliente.nombre.title()+";"+cliente.apellido.title()+";"+cliente.codigocliente+";"+cliente.telefono+";"+cliente.sector+";"+cliente.urbanizacion+";"+cliente.direccion+"\n")
    
    
    file.close()

def crearCliente2(archivo):
    #clientes=sacarInfoClientes2(archivo)
    file=open(archivo,"a")

    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    telefono=input("Telfono: ")
    sectores=["Miravalle","Nayon","Cumbaya","Lumbisi","La Primavera","Tumbaco","Puembo","Quito"]
    for i in range(len(sectores)):
        print(i+1, sectores[i])
    sector=int(input("Sector: "))
    #print(sector)
    urbanizacion=input("Urbanizacion: ")
    direccion=input("Direccion: ")
    codigoCliente=nombre[0].capitalize()+apellido[0].capitalize()+sectores[sector-1][0:2].lower()
    #CLientes2: nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion
    cliente=Clientes2(nombre,apellido,codigoCliente,telefono,sectores[sector-1],urbanizacion,direccion)
    #clientes.append(clienten)
    #print(clienten)
    
    #clientesordenados=[]
    #for sector in sectores:
    #for cliente in clientes:
    #    if sector==cliente.sector:
    #        clientesordenados.append(cliente)

    #for cliente in clientes:
    file.write(cliente.nombre.title()+";"+cliente.apellido.title()+";"+cliente.codigocliente+";"+cliente.telefono+";"+cliente.sector+";"+cliente.urbanizacion+";"+cliente.direccion+"\n")
    
    
    file.close()


def sacarInfoClientes2(archivo):
    clientes=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        #print(a[1])
        #nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion
        cl=Clientes2(a[0],a[1],a[2],a[3],a[4],a[5],a[6])
        clientes.append(cl)
    file.close()
    return clientes

#crearCliente2("clientesprueba3.dat")

def agregarProducto(archivoproductos):
    file=open(archivoproductos,"a")
    producto=input("Producto: ")
    precio=float(input("Precio: "))
    costo=float(input("Costo: "))
    file.write(producto.capitalize()+";"+str(precio)+";"+str(costo))
    #productosls.append(producto)
    #preciosls.append(precio)
    #costosls.append(costo)
    file.close()

#agregarProducto("productosprueba.dat")

def sacarInfoProductos(archivoproductos):
    file=open(archivoproductos,"r")
    file.readline()
    productos=[]
    precios=[]
    costos=[]
    for line in file:
        a=line.strip().split(";")
        #print(a)
        productos.append(str(a[0]))
        precios.append(float(a[1]))
        costos.append(float(a[2]))

    file.close()
    return productos,precios,costos

#productos,precios,costos=sacarInfoProductos("productosprueba.dat")
#print(productos[1],precios,costos)

def ingresarPedido3(archivoClientes,archivoPedidos,archivoProductos):
    productos,precios,costos=sacarInfoProductos(archivoProductos)
    clientes=sacarInfoClientes2(archivoClientes)
    file=open(archivoPedidos,"a")
    f=dt.datetime.today()
    fecha=dt.datetime.timestamp(f)
    pedidocliente=input("Codigo cliente o nombre: ")

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
            print(productosfl)
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
          
            file.write(str(fecha)+";"+cliente.nombre+";"+cliente.apellido+";"+cliente.codigocliente+";"+cliente.sector+";"+cliente.urbanizacion+";"+cliente.direccion+";")
            file.write(str(productosfl)+";"+str(cantidadesfl)+";"+str(preciosfl)+";"+str(costosfl)+"\n")
            break
    file.close()


def agregarProducto(archivoproductos):
    file=open(archivoproductos,"a")
    producto=input("Producto: ")
    precio=float(input("Precio: "))
    costo=float(input("Costo: "))
    file.write(producto.capitalize()+";"+str(precio)+";"+str(costo))
    #productosls.append(producto)
    #preciosls.append(precio)
    #costosls.append(costo)
    file.close()

#agregarProducto("productosprueba.dat")

def sacarInfoProductos(archivoproductos):
    file=open(archivoproductos,"r")
    file.readline()
    productos=[]
    precios=[]
    costos=[]
    for line in file:
        a=line.strip().split(";")
        #print(a)
        productos.append(str(a[0]))
        precios.append(float(a[1]))
        costos.append(float(a[2]))

    file.close()
    return productos,precios,costos

#productos,precios,costos=sacarInfoProductos("productosprueba.dat")
#print(productos[1],precios,costos)

def ingresarPedido4(archivoClientes,archivoPedidos,archivoProductos):
    productos,precios,costos=sacarInfoProductos(archivoProductos)
    clientes=sacarInfoClientes2(archivoClientes)
    file=open(archivoPedidos,"a")
    f=dt.datetime.today()
    fecha=dt.datetime.timestamp(f)
    pedidocliente=input("Codigo cliente o nombre: ")

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
            print("Pedido de:", cliente.nombre,cliente.apellido, "Codigo:", cliente.codigocliente)
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
            print(productosfl)
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
            pago="p" #pendiente
            file.write(str(fecha)+";"+cliente.nombre+";"+cliente.apellido+";"+cliente.codigocliente+";"+cliente.sector+";"+cliente.urbanizacion+";"+cliente.direccion+";")
            file.write(str(productosfl)+";"+str(cantidadesfl)+";"+str(preciosfl)+";"+str(costosfl)+";"+pago+"\n")
    file.close()

#ingresarPedido3("clientesprueba3.dat","pedidosprueba5.dat","productosprueba.dat")

def imprimirPedidoInd2(nombre,apellido,direccion,sector,tamanox,tamanoy,documento,productos,cantidad,precios,movex,movey,numeropedido): #,posinicialx,posinicialy
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

def dividirPaginas(documento,height,width):
    for i in range(0,int(height),2):
        documento.drawString(int(width)/2,i+1,"|")
    for j in range(0,int(width),2):
        documento.drawString(j+1,int(height)/2,"-")

def imprimirPedidos2(nombrearcivo,width,height,pedidos):

    documento=canvas.Canvas(nombrearchivo,pagesize=A4)
    paginas=len(pedidos)//4
    #if len(pe)/4!=0:
    #    paginas+=0

    #print(pe[7])
    #for i in range(paginas):
    for n in range(paginas):
        #print(n)
        dividirPaginas(documento,height,width)
        imprimirPedidoInd2(pedidos[0+4*n].nombre,pedidos[0+4*n].apellido,pedidos[0+4*n].direccion,pedidos[0+4*n].sector,int(width)/2,int(height),documento,pedidos[0+4*n].productos,pedidos[0+4*n].cantidades,pedidos[0+4*n].precios,0,0,0+4*n+1)
        imprimirPedidoInd2(pedidos[1+4*n].nombre,pedidos[1+4*n].apellido,pedidos[1+4*n].direccion,pedidos[1+4*n].sector,int(width)/2,int(height),documento,pedidos[1+4*n].productos,pedidos[1+4*n].cantidades,pedidos[1+4*n].precios,1,0,1+4*n+1)
        imprimirPedidoInd2(pedidos[2+4*n].nombre,pedidos[2+4*n].apellido,pedidos[2+4*n].direccion,pedidos[2+4*n].sector,int(width)/2,int(height),documento,pedidos[2+4*n].productos,pedidos[2+4*n].cantidades,pedidos[2+4*n].precios,0,1,2+4*n+1)
        imprimirPedidoInd2(pedidos[3+4*n].nombre,pedidos[3+4*n].apellido,pedidos[3+4*n].direccion,pedidos[3+4*n].sector,int(width)/2,int(height),documento,pedidos[3+4*n].productos,pedidos[3+4*n].cantidades,pedidos[3+4*n].precios,1,1,3+4*n+1)
        documento.showPage()
    #dividirPaginas(documento,height,width)
    possobraninicial=paginas*4
    possobran=len(pedidos)
    
    if len(pedidos)%4==3:
        imprimirPedidoInd2(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,pedidos[possobraninicial].productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        imprimirPedidoInd2(pedidos[possobraninicial+1].nombre,pedidos[possobraninicial+1].apellido,pedidos[possobraninicial+1].direccion,pedidos[possobraninicial+1].sector,int(width)/2,int(height),documento,pedidos[possobraninicial+1].productos,pedidos[possobraninicial+1].cantidades,pedidos[possobraninicial+1].precios,1,0,possobraninicial+1+1)
        imprimirPedidoInd2(pedidos[possobraninicial+2].nombre,pedidos[possobraninicial+2].apellido,pedidos[possobraninicial+2].direccion,pedidos[possobraninicial+2].sector,int(width)/2,int(height),documento,pedidos[possobraninicial+2].productos,pedidos[possobraninicial+2].cantidades,pedidos[possobraninicial+2].precios,0,1,possobraninicial+2+1)
        dividirPaginas(documento,height,width)
    elif len(pedidos)%4==2:
        imprimirPedidoInd2(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,pedidos[possobraninicial].productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        imprimirPedidoInd2(pedidos[possobraninicial+1].nombre,pedidos[possobraninicial+1].apellido,pedidos[possobraninicial+1].direccion,pedidos[possobraninicial+1].sector,int(width)/2,int(height),documento,pedidos[possobraninicial+1].productos,pedidos[possobraninicial+1].cantidades,pedidos[possobraninicial+1].precios,1,0,possobraninicial+1+1)
        dividirPaginas(documento,height,width)
    elif len(pedidos)%4==1:
        imprimirPedidoInd2(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,pedidos[possobraninicial].productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        dividirPaginas(documento,height,width)
    documento.save()

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
nombrearchivo="pedidos3_"+fechainicio+"_"+fechafin+".pdf"
#print(nombrearchivo)
fechainiciopedidos=dt.datetime.timestamp(fechai)
fechafinpedidos=dt.datetime.timestamp(fechaf)
pedidosimprimir=sacarInfoPedidoFecha2("pedidosprueba4.dat",fechainiciopedidos,fechafinpedidos)
'''for pedido in pedidosimprimir:
    print(pedido.nombre,pedido.apellido,pedido.sector,pedido.urbanizacion,pedido.direccion)
    print(pedido.productos,pedido.precios,pedido.costos)'''


#imprimirPedidos2(nombrearchivo,width,height,pedidosimprimir)

def ordenarentregas(pedidos,clientes):
    lista=[]
    for cliente in clientes:

        for pedido in pedidos:

            if cliente.nombre==pedido.nombre and cliente.apellido==pedido.apellido and cliente.codigocliente==pedido.codigocliente:
                lista.append(pedido)

    return lista

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
nombrearchivo="pedidos3_"+fechainicio+"_"+fechafin+".pdf"
#print(nombrearchivo)
fechainiciopedidos=dt.datetime.timestamp(fechai)
fechafinpedidos=dt.datetime.timestamp(fechaf)
pedidosimprimir=sacarInfoPedidoFecha2("pedidosprueba4.dat",fechainiciopedidos,fechafinpedidos)
#print(len(pedidosimprimir))

#paginas=len(pe)//4

#imprimirPedidos2(nombrearchivo,width,height,pedidosimprimir)