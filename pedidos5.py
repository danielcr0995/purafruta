#!/usr/bin/python3

import datetime as dt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter , A4
from reportlab.lib.units import cm
import pandas as pd

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

class Pedidos4:
    def __init__(self,fecha,nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion,productos,cantidades,precios,costos,pago):#orden de precios y costos Piña Orito/kg Maracuya/kg Papaya/1	Verde/1	Sandia/1 Naranja/8 Limones/10 Aguacates	Platanos/10 miel

        self.fecha=fecha
        self.nombre=nombre
        self.apellido=apellido
        self.codigocliente=codigocliente
        self.telefono=telefono
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
        #pago=a[7]
        prod=a[7][1:len(a[7])-1]        
        productos=prod.split(",")
        c=a[8][1:len(a[8])-1]
        cantidades=c.split(",")
        pr=a[9][1:len(a[9])-1]
        precios=pr.split(",")        
        ct=a[10][1:len(a[10])-1]
        costos=ct.split(",")
        pago=a[11]
        for i in range(len(productos)):
            cantidades[i]=float(cantidades[i])
            precios[i]=float(precios[i])
            costos[i]=float(costos[i])     
            productos[i]=productos[i].replace(" '","").replace("'","")
        
        pd=Pedidos3(fecha,nombre,apellido,codigocliente,sector,urbanizacion,direccion,productos,cantidades,precios,costos,pago)
        if pd.fecha>=fechainicio and pd.fecha<=fechafin:
            lista.append(pd)
    file.close()
    return lista

def sacarInfoPedidoFecha5(archivo,fechainicio,fechafin):#,fechaInicio):
    lista=[]
    file=open(archivo,"r")
    file.readline()
    for line in file:
        a=line.strip().split(";")
        fecha=float(a[0])
        nombre=a[1]
        apellido=a[2]
        codigocliente=a[3]
        telefono=a[4]
        sector=a[5]
        urbanizacion=a[6]
        direccion=a[7]
        #pago=a[7]
        prod=a[8][1:len(a[8])-1]        
        productos=prod.split(",")
        c=a[9][1:len(a[9])-1]
        cantidades=c.split(",")
        pr=a[10][1:len(a[10])-1]
        precios=pr.split(",")        
        ct=a[11][1:len(a[11])-1]
        costos=ct.split(",")
        pago=a[12]
        #print(pago, nombre,apellido)
        for i in range(len(productos)):
            #print(productos[i])
            if 'Notas' in productos[i]:
                cantidades[i]=cantidades[i].replace(" '","").replace("'","")
                precios[i]=float(precios[i])
                costos[i]=float(costos[i])     
                productos[i]=productos[i].replace(" '","").replace("'","")    

            else:
                cantidades[i]=float(cantidades[i])
                precios[i]=float(precios[i])
                costos[i]=float(costos[i])     
                productos[i]=productos[i].replace(" '","").replace("'","")
        
        pd=Pedidos4(fecha,nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion,productos,cantidades,precios,costos,pago)
        if pd.fecha>=fechainicio and pd.fecha<=fechafin:
            lista.append(pd)
    file.close()
    return lista

def crearCliente2(archivo):
    #clientes=sacarInfoClientes2(archivo)
    file=open(archivo,"a")

    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    telefono=input("Telfono: ")
    sectores=["Miravalle","Nayon","Cumbaya","Lumbisi","San Juan","Primavera","Intervalles","Tumbaco","Puembo","Quito"]
    for i in range(len(sectores)):
        print(i+1, sectores[i])
    sectorop=int(input("Sector: "))
    sector=sectores[sectorop-1]
    #print(sector)
    urbanizacion=input("Urbanizacion: ")
    direccion=input("Direccion: ")
    #codigoCliente=nombre[0].capitalize()+apellido[0].capitalize()+sectores[sector-1][0:2].lower()   #codigo cliente anterior
    codigoCliente=nombre[0:2].lower()+apellido[0:2].lower()+sector[0:2].lower()
    #CLientes2: nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion
    cliente=Clientes2(nombre,apellido,codigoCliente,telefono,sectores[sectorop-1],urbanizacion,direccion)
    #clientes.append(clienten)
    #print(clienten)
    
    #clientesordenados=[]
    #for sector in sectores:
    #for cliente in clientes:
    #    if sector==cliente.sector:
    #        clientesordenados.append(cliente)

    #for cliente in clientes:
    file.write(cliente.nombre.title()+";"+cliente.apellido.title()+";"+cliente.codigocliente+";"+cliente.telefono+";"+cliente.sector+";"+cliente.urbanizacion.title()+";"+cliente.direccion+"\n")
    
    
    file.close()

def crearCliente3(archivo): #mira que no se repitan codigos
    clientes=sacarInfoClientes2(archivo)
    codigos=[]
    for cliente in clientes:
        codigos.append(cliente.codigocliente)
    file=open(archivo,"a")

    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    telefono=input("Telfono: ")
    sectores=["Miravalle","Nayon","Cumbaya","Lumbisi","San Juan","Primavera","Intervalles","Tumbaco","Puembo","Quito"]
    for i in range(len(sectores)):
        print(i+1, sectores[i])
    sectorop=int(input("Sector: "))
    sector=sectores[sectorop-1]
    #print(sector)
    urbanizacion=input("Urbanizacion: ")
    direccion=input("Direccion: ")
    #codigoCliente=nombre[0].capitalize()+apellido[0].capitalize()+sectores[sector-1][0:2].lower()   #codigo cliente anterior
    
    codigoCliente=nombre[0:2].lower()+apellido[0:2].lower()+sector[0:2].lower()
    
    while codigoCliente in codigos:
        codigoCliente=input('Codigo ya existe, ingrese otro: ')
    #CLientes2: nombre,apellido,codigocliente,telefono,sector,urbanizacion,direccion
    cliente=Clientes2(nombre,apellido,codigoCliente,telefono,sectores[sectorop-1],urbanizacion,direccion)

    file.write(cliente.nombre.title()+";"+cliente.apellido.title()+";"+cliente.codigocliente+";"+cliente.telefono+";"+cliente.sector+";"+cliente.urbanizacion.title()+";"+cliente.direccion+"\n")
    
    
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

#crearCliente3("clientesprueba4.dat")

def cambiarCodigoCliente(archivoclientesviejo,archivoclientesnuevo):
    clientes=sacarInfoClientes2(archivoclientesviejo)
    file=open(archivoclientesnuevo,"w")
    file.write("nombre;apellido;codigocliente;telefono;sector;urbanizacion;direccion\n")
    sectores=["Miravalle","Nayon","Cumbaya","Lumbisi","San Juan","Primavera","Intervalles","Tumbaco","Puembo","Quito"]

    for cliente in clientes:
        cliente.codigocliente=cliente.nombre[0:2].lower()+cliente.apellido[0:2].lower()+cliente.sector[0:2].lower()
        file.write(cliente.nombre.title()+";"+cliente.apellido.title()+";"+cliente.codigocliente+";"+cliente.telefono+";"+cliente.sector+";"+cliente.urbanizacion.title()+";"+cliente.direccion+"\n")
#cambiarCodigoCliente("clientesprueba3.dat",'clientesprueba4.dat')

def agregarProducto(archivoproductos):
    file=open(archivoproductos,"a")
    producto=input("Producto: ")
    precio=float(input("Precio: "))
    costo=float(input("Costo: "))
    file.write(producto.capitalize()+";"+str(precio)+";"+str(costo)+"\n")
    #productosls.append(producto)
    #preciosls.append(precio)
    #costosls.append(costo)
    file.close()

#agregarProducto('productosprueba.dat')

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


def ingresarPedido4(archivoClientes,archivoPedidos,archivoProductos):
    productos,precios,costos=sacarInfoProductos(archivoProductos)
    clientes=sacarInfoClientes2(archivoClientes)
    file=open(archivoPedidos,"a")
    f=dt.datetime.today()
    fecha=dt.datetime.timestamp(f)
    pedidocliente=input("Codigo cliente o nombre: ")
    
    #if len(pedidocliente)>4: con codigo anterior en clientesprueba3.dat
    if len(pedidocliente)>6:
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
            print("Codigo:", cliente.codigocliente)
            print("Urbanizacion: ", cliente.urbanizacion)
            print("Direccion: ",cliente.direccion)
            
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
            #print(productosfl)
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
#ingresarPedido4("clientesprueba3.dat","pedidosprueba6.dat","productosprueba.dat")

def ingresarPedido5(archivoClientes,archivoPedidos,archivoProductos): # pone el telefono del cliente
    productos,precios,costos=sacarInfoProductos(archivoProductos)
    clientes=sacarInfoClientes2(archivoClientes)
    file=open(archivoPedidos,"a")
    f=dt.datetime.today()
    fecha=dt.datetime.timestamp(f)
    pedidocliente=input("Codigo cliente o nombre: ")
    
    #if len(pedidocliente)>4: con codigo anterior en clientesprueba3.dat
    if len(pedidocliente)>6:
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
            print("Codigo:", cliente.codigocliente)
            print("Urbanizacion: ", cliente.urbanizacion)
            print("Direccion: ",cliente.direccion)
            
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
            #print(productosfl)
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
            file.write(str(fecha)+";"+cliente.nombre+";"+cliente.apellido+";"+cliente.codigocliente+";"+cliente.telefono+";"+cliente.sector+";"+cliente.urbanizacion+";"+cliente.direccion+";")
            file.write(str(productosfl)+";"+str(cantidadesfl)+";"+str(preciosfl)+";"+str(costosfl)+";"+pago+"\n")
    file.close()

def ingresarPedido6(archivoClientes,archivoPedidos,archivoProductos): # pone el telefono del cliente con menu para productos 
    productos,precios,costos=sacarInfoProductos(archivoProductos)
    clientes=sacarInfoClientes2(archivoClientes)
    file=open(archivoPedidos,"a")
    f=dt.datetime.today()
    fecha=dt.datetime.timestamp(f)
    pedidocliente=input("Codigo cliente o nombre: ")
    
    #if len(pedidocliente)>4: con codigo anterior en clientesprueba3.dat
    if len(pedidocliente)>6:
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
            print("Codigo:", cliente.codigocliente)
            print("Urbanizacion: ", cliente.urbanizacion)
            print("Direccion: ",cliente.direccion)
            
            #f=dt.datetime.today()
            #fecha=dt.datetime.timestamp(f)
            cantidadesfl=[]#guardados en el archivo
            productosfl=[] #guardados en el archivo
            preciosfl=[] #guardados en el archivo
            costosfl=[] #guardados en el archivo
            posproductos=[]

            numerocolumnas=len(productos)//4
            tcolumn=25
            print('\n')
            for i in range(numerocolumnas):
                
                print((0+4*i)+1,' '+productos[0+4*i],' '*(tcolumn-len(str((0+4*i)+1))-len(productos[0+4*i])),(1+4*i)+1,' '+productos[1+4*i],
                        ' '*(tcolumn-len(str((1+4*i)+1))-len(productos[1+4*i])),(2+4*i)+1,productos[2+4*i],
                        ' '*(tcolumn-len(str((2+4*i)+1))-len(productos[2+4*i])),(3+4*i)+1,' '+productos[3+4*i])
            if len(productos)%4==3:
                print((0+4*numerocolumnas)+1,' '+productos[0+4*numerocolumnas],' '*(tcolumn-len(str((0+4*numerocolumnas)+1))-len(productos[0+4*numerocolumnas])),
                        (1+4*numerocolumnas)+1,' '+productos[1+4*numerocolumnas],' '*(tcolumn-len(str((1+4*numerocolumnas)+1))-len(productos[1+4*numerocolumnas])),
                        (2+4*numerocolumnas)+1,' '+productos[2+4*numerocolumnas])
            if len(productos)%4==2:
                print((0+4*numerocolumnas)+1,' '+productos[0+4*numerocolumnas],' '*(tcolumn-len(str((0+4*numerocolumnas)+1))-len(productos[0+4*numerocolumnas])),
                        (1+4*numerocolumnas)+1,' '+productos[1+4*numerocolumnas])
            if len(productos)%4==1:
                print((0+4*numerocolumnas)+1,' '+productos[0+4*numerocolumnas],)
            
            print('\n')

            prod=int(input('Producto: '))
            while prod!=000:
                if productos[prod-1]=='Extras':
                    cantidadextra=float(input('Cantidad '+productos[prod-1].upper()+': '))
                    if cantidadextra!=0:
                        prodextra=input('Producto'+productos[prod-1].upper()+': ')
                        precioextra=float(input('Precio: '))
                        costoextra=float(input('Costo: '))
                        #cantidadextra=float(input('Cantidad: '))
                        cantidadesfl.append(cantidadextra)
                        productosfl.append(prodextra.title())
                        preciosfl.append(precioextra)
                        costosfl.append(costoextra)
                        posproductos.append(prod-1)
                elif productos[prod-1]=='Notas':
                    nota=input("Nota: ")
                    if nota!='xxx':
                        cantidadesfl.append(nota.capitalize())
                        productosfl.append(productos[prod-1])
                        preciosfl.append(0)
                        costosfl.append(0)
                        posproductos.append(prod-1)
                else:
                    cantidad=float(input('Cantidad '+productos[prod-1].upper()+": "))
                    if cantidad!=0:
                        if productos[prod-1] in productosfl:
                            posproducto=productosfl.index(productos[prod-1])
                            cantidadesfl[posproducto]+=cantidad
                        else:
                            cantidadesfl.append(cantidad)
                            productosfl.append(productos[prod-1])
                            preciosfl.append(precios[prod-1])
                            costosfl.append(costos[prod-1])
                            posproductos.append(prod-1)
                prod=int(input('Producto: '))

                #print(productosfl,posproductos)

            for i in range(len(posproductos)):
                for j in range(len(posproductos)):
                    if posproductos[i]<posproductos[j]:
                        posproductos[i],posproductos[j]=posproductos[j],posproductos[i]
                        cantidadesfl[i],cantidadesfl[j]=cantidadesfl[j],cantidadesfl[i]
                        productosfl[i],productosfl[j]=productosfl[j],productosfl[i]
                        preciosfl[i],preciosfl[j]=preciosfl[j],preciosfl[i]
                        costosfl[i],costosfl[j]=costosfl[j],costosfl[i]

            #print(productosfl,posproductos)
#
#            for i in range(len(productos)):
            #for producto in productos:
                
#                cantidad=float(input(productos[i]+": "))
#                if cantidad==0:
#                   pass
#               else:
#                    productosfl.append(productos[i])
#                    preciosfl.append(precios[i])
#                    costosfl.append(costos[i])
#                    cantidadesfl.append(cantidad)
          
            #cantidad=[pina,orito,maracuya,papaya,verde,sandia,naranjas,limones,aguacates,platanos, miel]
            #pina;orito;maracuya;papaya;verde;sandia;naranjas;limones;aguacates;platanos; miel
            # 
            total=0
            tlinea=30#tamno linea
            print(tlinea*"*")
            print("Pedido de:", cliente.nombre,cliente.apellido)
            print(tlinea*"-")
            #print(productosfl)
            for i in range(len(productosfl)):
                
                if cantidadesfl[i]==0:
                    #print(cantidades[i])
                    pass
                elif productosfl[i]=='Notas':
                    pass
                else:
                    #print("Pedido de:", cliente.nombre,cliente.apellido)
                    precio=cantidadesfl[i]*preciosfl[i]
                    #print(productosfl)
                    #print(len(str(cantidad[i])))
                    #print(cantidades[i])
                    espacio=tlinea-len(str(cantidadesfl[i]))-len(str(productosfl[i]))-len(str(round(precio,2)))-4
                    print(str(cantidadesfl[i])+" "+productosfl[i]+" "*espacio+" $ "+str(precio) )
                    total+=precio
            print(tlinea*"-")
            print("Total"+ (tlinea-len("Total")-len(str(round(total,2)))-4)*" "+" $ "+ str(round(total,2)))
            posnotas=productosfl.index("Notas")
            #print(posnotas)
            print('Nota: '+cantidadesfl[posnotas])    
            pago="p" #pendiente
            file.write(str(fecha)+";"+cliente.nombre+";"+cliente.apellido+";"+cliente.codigocliente+";"+cliente.telefono+";"+cliente.sector+";"+cliente.urbanizacion+";"+cliente.direccion+";")
            file.write(str(productosfl)+";"+str(cantidadesfl)+";"+str(preciosfl)+";"+str(costosfl)+";"+pago+"\n")
    file.close()

#ingresarPedido6("clientesprueba4.dat","pedidosprueba7.dat","productosprueba.dat")

def imprimirPedidoInd(nombre,apellido,direccion,sector,tamanox,tamanoy,documento,productos,cantidad,precios,movex,movey,numeropedido): #,posinicialx,posinicialy
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

def imprimirPedidoInd3(nombre,apellido,urbanizacion,direccion,sector,tamanox,tamanoy,documento,productos,cantidad,precios,movex,movey,numeropedido): #,posinicialx,posinicialy
    cliente=nombre+" "+apellido
    #poscliente= (tamanolinea-len(cliente))/2
    centerText=lambda tamanolineax, texto: (tamanox-len(texto)/2)/2
    tlinea=100
    posclientex= centerText(tamanox,cliente)
    possector=centerText(tamanox,sector)
    #print(urbanizacion)
    posdireccion=centerText(tamanox,direccion)
    documento.drawString(posclientex+movex*tamanox/1,tamanoy-20-movey*tamanoy/2,cliente) #imprime el nombre 
    documento.drawString(posclientex+movex*tamanox/1-80,tamanoy-40-movey*tamanoy/2,sector+'-'+urbanizacion)
    
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

def imprimirPedidoInd4(nombre,apellido,urbanizacion,direccion,sector,tamanox,tamanoy,documento,productos,cantidad,precios,movex,movey,numeropedido): #,posinicialx,posinicialy
    cliente=nombre+" "+apellido
    #poscliente= (tamanolinea-len(cliente))/2
    centerText=lambda tamanolineax, texto: (tamanox-len(texto)/2)/2
    tlinea=100
    posclientex= centerText(tamanox,cliente)
    possector=centerText(tamanox,sector)
    #print(urbanizacion)
    posdireccion=centerText(tamanox,direccion)
    documento.drawString(posclientex+movex*tamanox/1,tamanoy-20-movey*tamanoy/2,cliente) #imprime el nombre 
    documento.drawString(posclientex+movex*tamanox/1-80,tamanoy-40-movey*tamanoy/2,sector+' - '+urbanizacion)
    
    posimprimirdireccion=tamanoy-40
    letraspagina=40
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
        if productos[i]=='Canasta basica':
            productoscanasta=['Pina','Orito','Maracuya','Papaya','Naranja','Limones','Manzana roja','Pera','Frutillas']
            cantidadescanasta=[1,1,1,4,2,2,1,1,1]
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

            #imprime cada cosa que va en la canasta
            for j in range(len(productoscanasta)):
                lineaprodcanasta=str(cantidadescanasta[j])+"  "+str(productoscanasta[j])
                documento.drawString(50+movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,lineaprodcanasta)
                posImprimirproductos-=20
        
        elif productos[i]=='Canasta mediana':
            productoscanasta=['Pina','Papaya','Sandia','Naranja','Limones','Manzana roja','Manzana verde','Pera','Frutillas']
            cantidadescanasta=[1,6,1,2,2,1,1,1,1]
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

            #imprime cada cosa que va en la canasta
            for j in range(len(productoscanasta)):
                lineaprodcanasta=str(cantidadescanasta[j])+"  "+str(productoscanasta[j])
                documento.drawString(50+movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,lineaprodcanasta)
                posImprimirproductos-=20

        elif productos[i]=='Canasta tropical':
            productoscanasta=['Pina','Orito','Maracuya','Papaya','Verde','Maduro','Sandia','Naranja','Platano',]
            cantidadescanasta=[2,1,2,2,2,2,1,1,1.7]
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

            #imprime cada cosa que va en la canasta
            for j in range(len(productoscanasta)):
                lineaprodcanasta=str(cantidadescanasta[j])+"  "+str(productoscanasta[j])
                documento.drawString(50+movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,lineaprodcanasta)
                posImprimirproductos-=20
        
        elif productos[i]=='Canasta premium':
            productoscanasta=['Pina','Papaya','Sandia','Naranja','Miel de abeja','Manzana verde','Pera','Futillas','Uva rosada']
            cantidadescanasta=[2,6,1,2,1,2,1,2,2]
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

            #imprime cada cosa que va en la canasta
            for j in range(len(productoscanasta)):
                lineaprodcanasta=str(cantidadescanasta[j])+"  "+str(productoscanasta[j])
                documento.drawString(50+movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,lineaprodcanasta)
                posImprimirproductos-=20
                

        elif productos[i]!='Notas':
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
    posImprimirproductos-=40
    documento.drawString(20+movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,'Notas:')
    #posImprimirproductos-=20
    if 'Notas' in productos:
        posnotas=productos.index('Notas')
        nota=cantidad[posnotas]
        for i in range((len(nota)//letraspagina)+1):
            posImprimirproductos-=20
            documento.drawString(20+movex*tamanox/1,posImprimirproductos-movey*tamanoy/2,nota[i*letraspagina:(i+1)*letraspagina])

   

def dividirPaginas(documento,height,width):
    for i in range(0,int(height),2):
        documento.drawString(int(width)/2,i+1,"|")
    for j in range(0,int(width),2):
        documento.drawString(j+1,int(height)/2,"-")

def imprimirPedidos3(nombrearchivo,width,height,pedidos):

    documento=canvas.Canvas(nombrearchivo,pagesize=A4)
    paginas=len(pedidos)//4
    #if len(pe)/4!=0:
    #    paginas+=0

    #print(pe[7])
    #for i in range(paginas):
    for n in range(paginas):
        #print(n)
        dividirPaginas(documento,height,width)
        #cambiado imprimirPedidoInd3 para que imprima lo que va encada canasta
        imprimirPedidoInd4(pedidos[0+4*n].nombre,pedidos[0+4*n].apellido,pedidos[0+4*n].urbanizacion,pedidos[0+4*n].direccion,pedidos[0+4*n].sector,int(width)/2,int(height),documento,pedidos[0+4*n].productos,pedidos[0+4*n].cantidades,pedidos[0+4*n].precios,0,0,0+4*n+1)
        imprimirPedidoInd4(pedidos[1+4*n].nombre,pedidos[1+4*n].apellido,pedidos[1+4*n].urbanizacion,pedidos[1+4*n].direccion,pedidos[1+4*n].sector,int(width)/2,int(height),documento,pedidos[1+4*n].productos,pedidos[1+4*n].cantidades,pedidos[1+4*n].precios,1,0,1+4*n+1)
        imprimirPedidoInd4(pedidos[2+4*n].nombre,pedidos[2+4*n].apellido,pedidos[2+4*n].urbanizacion,pedidos[2+4*n].direccion,pedidos[2+4*n].sector,int(width)/2,int(height),documento,pedidos[2+4*n].productos,pedidos[2+4*n].cantidades,pedidos[2+4*n].precios,0,1,2+4*n+1)
        imprimirPedidoInd4(pedidos[3+4*n].nombre,pedidos[3+4*n].apellido,pedidos[3+4*n].urbanizacion,pedidos[3+4*n].direccion,pedidos[3+4*n].sector,int(width)/2,int(height),documento,pedidos[3+4*n].productos,pedidos[3+4*n].cantidades,pedidos[3+4*n].precios,1,1,3+4*n+1)
        documento.showPage()
    #dividirPaginas(documento,height,width)
    possobraninicial=paginas*4
    possobran=len(pedidos)
    
    if len(pedidos)%4==3:
        imprimirPedidoInd4(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].urbanizacion,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,pedidos[possobraninicial].productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        imprimirPedidoInd4(pedidos[possobraninicial+1].nombre,pedidos[possobraninicial+1].apellido,pedidos[possobraninicial+1].urbanizacion,pedidos[possobraninicial+1].direccion,pedidos[possobraninicial+1].sector,int(width)/2,int(height),documento,pedidos[possobraninicial+1].productos,pedidos[possobraninicial+1].cantidades,pedidos[possobraninicial+1].precios,1,0,possobraninicial+1+1)
        imprimirPedidoInd4(pedidos[possobraninicial+2].nombre,pedidos[possobraninicial+2].apellido,pedidos[possobraninicial+2].urbanizacion,pedidos[possobraninicial+2].direccion,pedidos[possobraninicial+2].sector,int(width)/2,int(height),documento,pedidos[possobraninicial+2].productos,pedidos[possobraninicial+2].cantidades,pedidos[possobraninicial+2].precios,0,1,possobraninicial+2+1)
        dividirPaginas(documento,height,width)
    elif len(pedidos)%4==2:
        imprimirPedidoInd4(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].urbanizacion,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,pedidos[possobraninicial].productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        imprimirPedidoInd4(pedidos[possobraninicial+1].nombre,pedidos[possobraninicial+1].apellido,pedidos[possobraninicial+1].urbanizacion,pedidos[possobraninicial+1].direccion,pedidos[possobraninicial+1].sector,int(width)/2,int(height),documento,pedidos[possobraninicial+1].productos,pedidos[possobraninicial+1].cantidades,pedidos[possobraninicial+1].precios,1,0,possobraninicial+1+1)
        dividirPaginas(documento,height,width)
    elif len(pedidos)%4==1:
        imprimirPedidoInd4(pedidos[possobraninicial].nombre,pedidos[possobraninicial].apellido,pedidos[possobraninicial].urbanizacion,pedidos[possobraninicial].direccion,pedidos[possobraninicial].sector,int(width)/2,int(height),documento,pedidos[possobraninicial].productos,pedidos[possobraninicial].cantidades,pedidos[possobraninicial].precios,0,0,possobraninicial+1)
        dividirPaginas(documento,height,width)
    documento.save()

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
'''
ano=2020
mes=7
dia=21
fechai=dt.datetime(ano,mes,dia)
fechainicio=str(fechai.year)+str(fechai.month)+str(fechai.day)#fechai.strtime("%d%m%y")
fechaf=dt.datetime.today()
fechafin=str(fechaf.year)+str(fechaf.month)+str(fechaf.day)#fechaf.strtime("%d%m%y")#str(fecahf.year)+str(fecahf.month)+str(fecahf.day)
nombrearchivo="pedidos_"+fechainicio+"_"+fechafin+".pdf"
print(nombrearchivo)
fechainiciopedidos=dt.datetime.timestamp(fechai)
fechafinpedidos=dt.datetime.timestamp(fechaf)
pedidosimprimir=sacarInfoPedidoFecha5("pedidosprueba7.dat",fechainiciopedidos,fechafinpedidos)
imprimirPedidos3(nombrearchivo,width,height,pedidosimprimir)

archivoclientes="clientesprueba3.dat"
archivoproductos="productosprueba.dat"
archivopedidos="pedidosprueba7.dat"
'''
#productos,precios,costos=sacarInfoProductos(archivoproductos)
#productoslista=pd.read_csv(archivoproductos,sep=';');
#productosdf=productoslista["producto"]
#preciosdf=productoslista["precio"]
#costosdf=productoslista['costo']
#cantidades=[]
#fechai=dt.datetime(ano,mes,dia)
#fechainicio=str(fechai.year)+str(fechai.month)+str(fechai.day)#fechai.strtime("%d%m%y")
#fechaf=dt.datetime.today()
#fechafin=str(fechaf.year)+str(fechaf.month)+str(fechaf.day)#fechaf.strtime("%d%m%y")#str(fecahf.year)+str(fecahf.month)+str(fecahf.day)
#nombrearchivoexel="pedidos_"+fechainicio+"_"+fechafin+".xlsx"
#for i in range (len(productos)):
#    cantidades.append(0)
    
def cambiarPedido(dataframepedidos,archivopedidos,archivoproductos):
    numeropedido=int(input('Numero de pedido: '))
    pedido=dataframepedidos.iloc[numeropedido]
    print(pedido)    
    file=open(archivopedidos,"a")
    productos,precios,costos=sacarInfoProductos(archivoproductos)
    
    f=dt.datetime.today()
    fecha=dt.datetime.timestamp(f)
    nombre=pedido['Nombre']
    apellido=pedido['Apellido']
    codigocliente=pedido['Codigo Cliente']
    telefono=pedido['Telefono']
    sector=pedido['Sector']
    urbanizacion=pedido['Urbanizacion']
    direccion=pedido['Direccion']
    pago='p'
    cantidades=[]
    for prod in productos:
        cantidades.append(pedido[prod])
    #print(cantidades)
    
    numerocolumnas=len(productos)//4
    tcolumn=25
    print('\n')
    
    for i in range(numerocolumnas):
                
            print((0+4*i)+1,' '+productos[0+4*i],' '*(tcolumn-len(str((0+4*i)+1))-len(productos[0+4*i])),(1+4*i)+1,' '+productos[1+4*i],
                        ' '*(tcolumn-len(str((1+4*i)+1))-len(productos[1+4*i])),(2+4*i)+1,productos[2+4*i],
                        ' '*(tcolumn-len(str((2+4*i)+1))-len(productos[2+4*i])),(3+4*i)+1,' '+productos[3+4*i])
    if len(productos)%4==3:
        print((0+4*numerocolumnas)+1,' '+productos[0+4*numerocolumnas],' '*(tcolumn-len(str((0+4*numerocolumnas)+1))-len(productos[0+4*numerocolumnas])),
                (1+4*numerocolumnas)+1,' '+productos[1+4*numerocolumnas],' '*(tcolumn-len(str((1+4*numerocolumnas)+1))-len(productos[1+4*numerocolumnas])),
                (2+4*numerocolumnas)+1,' '+productos[2+4*numerocolumnas])
    if len(productos)%4==2:
        print((0+4*numerocolumnas)+1,' '+productos[0+4*numerocolumnas],' '*(tcolumn-len(str((0+4*numerocolumnas)+1))-len(productos[0+4*numerocolumnas])),
                (1+4*numerocolumnas)+1,' '+productos[1+4*numerocolumnas])
    if len(productos)%4==1:
        print((0+4*numerocolumnas)+1,' '+productos[0+4*numerocolumnas],)

    print('\n')
    
    prod=int(input('Producto: '))
    while prod!=000:
        cantidad=float(input('Cantidad '+productos[prod-1].upper()+": "))
        cantidades[prod-1]+=cantidad
        prod=int(input('Producto: '))
        
    cantidadesfl=[]#guardados en el archivo
    productosfl=[] #guardados en el archivo
    preciosfl=[] #guardados en el archivo
    costosfl=[]
    
    for i in range(len(cantidades)):
        if cantidades[i]!=0:
            cantidadesfl.append(cantidades[i])
            productosfl.append(productos[i])
            preciosfl.append(precios[i])
            costosfl.append(costos[i])
    #print(nombre,cantidadesfl,productosfl,preciosfl,costosfl)
    file.write(str(fecha)+";"+nombre+";"+apellido+";"+codigocliente+";"+telefono+";"+sector+";"+urbanizacion+
               ";"+direccion+";")
    file.write(str(productosfl)+";"+str(cantidadesfl)+";"+str(preciosfl)+";"+str(costosfl)+";"+pago+"\n")
    file.close()



#print(tablapedidos)
#def eliminarPedido()

def tablapedidosf(productos,dataframe,columnas,precios,costos,pedidos,pedido):
    cantidades=[0 for c in range(len(productos))]
    
    dataframe=dataframe.append({columnas[0]:pedido.fecha,columnas[1]:pedido.nombre,
                                     columnas[2]:pedido.apellido,columnas[3]:pedido.codigocliente,columnas[4]:pedido.sector,
                                     columnas[5]:pedido.urbanizacion,columnas[6]:pedido.direccion},ignore_index=True)

    total=0
    for i in range(len(productos)):
        if productos[i] in pedido.productos:
            posproductopedido=pedido.productos.index(productos[i]) #del pedido
            posproducto=productos.index(productos[i])#en la lista de productos
            cantidades[posproducto]=pedido.cantidades[posproductopedido]
            #tablapedidos=tablapedidos.append({productos[i]:cantidades[i]},ignore_index=True)
            #print(pedidosls2.index(pedido))
            dataframe.at[pedidos.index(pedido),productos[i]]=cantidades[i]
            total+=cantidades[i]*precios[i]
    dataframe.at[pedidos.index(pedido),'Total']=round(total,2)
    dataframe.fillna(0,inplace=True)
    return dataframe

#def cambiarPedido(nombre, apeillido, fecha,pedido):
    
'''

pedidosls=pd.read_csv(archivopedidos,sep=';',quotechar=None, quoting=3)
pd.set_option('display.max_rows', None)


columnas1=['Fecha','Nombre','Apellido','Codigo Cliente','Sector','Urbanizacion','Direccion','Total']
columnas2=columnas1+productos
tablapedidos=pd.DataFrame(columns=columnas2)
pd.set_option('display.max_columns', None)

pedidosls2=sacarInfoPedidoFecha4("pedidosprueba6.dat",fechainiciopedidos,fechafinpedidos)

for pedido in pedidosls2:
    tablapedidosf(productos,tablapedidos,columnas2,precios,costos,pedidosls2)
    

tablapedidos['Fecha'] = pd.to_datetime(tablapedidos['Fecha'],unit='s')
tablapedidos['Fecha'] =tablapedidos['Fecha'].dt.date

'''

#imprimir dataframe sin funcion
'''
pedidosls=pd.read_csv(archivopedidos,sep=';',quotechar=None, quoting=3)
pd.set_option('display.max_rows', None)


columnas1=['Fecha','Nombre','Apellido','Codigo Cliente','Sector','Urbanizacion','Direccion','Total']
columnas2=columnas1+productos
tablapedidos=pd.DataFrame(columns=columnas2)
pd.set_option('display.max_columns', None)

pedidosls2=sacarInfoPedidoFecha4("pedidosprueba6.dat",fechainiciopedidos,fechafinpedidos)

for pedido in pedidosls2:
    #cantidades=[0 for c in cantidades]
    
    cantidades=[0 for c in range(len(productos))]
    
    for i in range(len(pedido.productos)):
        #print(productos.index(pedido.productos[i]))
        cantidades[productos.index(pedido.productos[i])]=pedido.cantidades[i]


    tablapedidos=tablapedidos.append({columnas2[0]:pedido.fecha,columnas2[1]:pedido.nombre,
                                     columnas2[2]:pedido.apellido,columnas2[3]:pedido.codigocliente,columnas2[4]:pedido.sector,
                                     columnas2[5]:pedido.urbanizacion,columnas2[6]:pedido.direccion},ignore_index=True)   
    total=0
    for i in range(len(productos)):
        if productos[i] in pedido.productos:
            posproductopedido=pedido.productos.index(productos[i]) #del pedido
            posproducto=productos.index(productos[i])#en la lista de productos
            cantidades[posproducto]=pedido.cantidades[posproductopedido]
            #tablapedidos=tablapedidos.append({productos[i]:cantidades[i]},ignore_index=True)
            #print(pedidosls2.index(pedido))
            tablapedidos.at[pedidosls2.index(pedido),productos[i]]=cantidades[i]
            total+=cantidades[i]*precios[i]
    tablapedidos.at[pedidosls2.index(pedido),'Total']=round(total,2)
    #print(cantidades)
    
    total=0
    #for j in range(len(cantidades)):
     #   tablapedidos=tablapedidos.append({productos[i]:cantidades[i]},ignore_index=True)
    #print(pedido.nombre,pedido.apellido,cantidades)
tablapedidos.fillna(0,inplace=True)
#tablapedidos.to_datetime 
#tablapedidos['Fecha']=tablapedidos.to_datetime(tablapedidos["Fecha"],unit='s')
tablapedidos['Fecha'] = pd.to_datetime(tablapedidos['Fecha'],unit='s')
tablapedidos['Fecha'] =tablapedidos['Fecha'].dt.date

'''


    