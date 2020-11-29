#sacarPedidosExel.py
#from pedidos2 import sacarInfoProductos
import datetime as dt

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

def sacarInfoPedidoexel(archivo1,archivo2):#,fechaInicio):
    lista=[]
    file=open(archivo1,"r")
    file.readline()
    file2=open(archivo2,"w")
    file2.write("fecha;nombre;apellido;codigocliente;sector;direccion;cantidad;precio;costo\n")
    for line in file:
        a=line.strip().split(",")     
        #f=dt.datetime.strptime(a[0],"%m/%d/%y")
        f=dt.datetime.today()
        fecha=dt.datetime.timestamp(f)

        codigocliente=a[1][0].capitalize()+a[2][0].capitalize()+a[5][0:2].lower()

        cantidades=[float(a[7]),float(a[8]),float(a[9]),float(a[10]),float(a[11]),float(a[12]),float(a[13]),float(a[14]),float(a[15]),float(a[16]),float(a[17]),float(a[18]),float(a[19]),float(a[20])]
        #print(a[1],cantidades)
        precios=[float(a[21]),float(a[22]),float(a[23]),float(a[24]),float(a[25]),float(a[26]),float(a[27]),float(a[28]),float(a[29]),float(a[30]),float(a[31]),float(a[32]),float(a[33]),float(a[34])]
        #costos=[float(a[29]),float(a[30]),float(a[31]),float(a[32]),float(a[33]),float(a[34]),float(a[35]),float(a[36]),float(a[37]),float(a[38]),float(a[39])]
        costos=[float(a[35]),float(a[36]),float(a[37]),float(a[38]),float(a[39]),float(a[40]),float(a[41]),float(a[42]),float(a[43]),float(a[44]),float(a[45]),float(a[46]),float(a[47]),float(a[48])]
        file2.write(str(fecha)+";"+a[1].title()+";"+a[2].title()+";"+codigocliente+";"+a[5]+";"+a[6]+";"+str(cantidades)+";"+str(precios)+";"+str(costos)+"\n")
    file.close()
    file2.close()
#sacarInfoPedidoexel("pedidos300420.csv","pedidos300420.txt")
productos,precios,costos=sacarInfoProductos("productosprueba.dat")

def sacarInfoPedidoexel3(archivo1,archivo2,precios,costos):#,fechaInicio):
    lista=[]
    file=open(archivo1,"r")
    file.readline()
    file2=open(archivo2,"w")
    file2.write("fecha;nombre;apellido;codigocliente;sector;direccion;cantidad;precio;costo\n")
    for line in file:
        a=line.strip().split(",")     
        #f=dt.datetime.strptime(a[0],"%m/%d/%y")
        f=dt.datetime.today()
        fecha=dt.datetime.timestamp(f)

        codigocliente=a[1][0].capitalize()+a[2][0].capitalize()+a[5][0:2].lower()

        cantidades=[float(a[7]),float(a[8]),float(a[9]),float(a[10]),float(a[11]),float(a[12]),float(a[13]),float(a[14]),float(a[15]),float(a[16]),float(a[17]),float(a[18]),float(a[19]),float(a[20]),float(a[21]),float(a[22]),float(a[23])]
        #print(a[1],cantidades)
        #precios=[float(a[21]),float(a[22]),float(a[23]),float(a[24]),float(a[25]),float(a[26]),float(a[27]),float(a[28]),float(a[29]),float(a[30]),float(a[31]),float(a[32]),float(a[33]),float(a[34])]
        #costos=[float(a[29]),float(a[30]),float(a[31]),float(a[32]),float(a[33]),float(a[34]),float(a[35]),float(a[36]),float(a[37]),float(a[38]),float(a[39])]
        #costos=[float(a[35]),float(a[36]),float(a[37]),float(a[38]),float(a[39]),float(a[40]),float(a[41]),float(a[42]),float(a[43]),float(a[44]),float(a[45]),float(a[46]),float(a[47]),float(a[48])]
        file2.write(str(fecha)+";"+a[1].title()+";"+a[2].title()+";"+codigocliente+";"+a[5]+";"+a[6]+";"+str(cantidades)+";"+str(precios)+";"+str(costos)+"\n")
    file.close()
    file2.close()
print(precios)
sacarInfoPedidoexel3("pedido060520_2.csv","pedidos060520_22.dat",precios,costos)

def sacarInfoPedido2exel(archivo1,archivo2,archivoproductos):#,fechaInicio):
    lista=[]
    productos,precios,costos=sacarInfoProductos(archivoproductos)
    file=open(archivo1,"r")
    file.readline()
    file2=open(archivo2,"w")
    file2.write("fecha;nombre;apellido;codigocliente;sector;urbanizacion;direccion;productos;cantidades;precios;costos\n")
    for line in file:
        a=line.strip().split(",")     
        #f=dt.datetime.strptime(a[0],"%m/%d/%y")
        f=dt.datetime.today()
        fecha=dt.datetime.timestamp(f)
        nombre=a[1].title()
        apellido=a[2].title()
        #a[4] es el telefono en el archivo
        sector=a[5]
        #print(sector,nombre)
        codigocliente=nombre[0].capitalize()+apellido[0].capitalize()+sector[0:2].lower()      
        urbanizacion=a[6]
        direccion=a[7]
        codigocliente=a[1][0].capitalize()+a[2][0].capitalize()+a[5][0:2].lower()


        cantidades=[float(a[8]),float(a[9]),float(a[10]),float(a[11]),float(a[12]),float(a[13]),float(a[14]),float(a[15]),float(a[16]),float(a[17]),float(a[18]),float(a[19]),float(a[20]),float(a[21]),float(a[22]),float(a[23]),float(a[24])]
        cantidades2=[]
        productos2=[]
        precios2=[]
        costos2=[]
        
        for i in range(len(productos)):
            #print(cantidades)
            if cantidades[i]!=0:
                cantidades2.append(cantidades[i])
                precios2.append(precios[i])
                costos2.append(costos[i])
                productos2.append(productos[i])
            #print(nombre,cantidades2,precios2,costos2)
        #print(a[1],cantidades2)

        #precios=[float(a[21]),float(a[22]),float(a[23]),float(a[24]),float(a[25]),float(a[26]),float(a[27]),float(a[28]),float(a[29]),float(a[30]),float(a[31]),float(a[32]),float(a[33]),float(a[34])]
        #costos=[float(a[29]),float(a[30]),float(a[31]),float(a[32]),float(a[33]),float(a[34]),float(a[35]),float(a[36]),float(a[37]),float(a[38]),float(a[39])]
        #costos=[float(a[35]),float(a[36]),float(a[37]),float(a[38]),float(a[39]),float(a[40]),float(a[41]),float(a[42]),float(a[43]),float(a[44]),float(a[45]),float(a[46]),float(a[47]),float(a[48])]
        
        file2.write(str(fecha)+";"+nombre+";"+ apellido+";"+codigocliente+";"+sector+";"+urbanizacion+";"+ direccion+";"+str(productos2)+";"+str(cantidades2)+";"+str(precios2)+";"+str(costos2)+"\n")
    file.close()
    file2.close()
sacarInfoPedido2exel("pedido060520.csv","pedidosprueba5.dat","productosprueba.dat")



def sacarInfoclientes(archivo1,archivo2):
    file=open(archivo1,"r")
    file.readline()
    file2=open(archivo2,"w")
    file2.write("nombre;apellido;codigocliente;telefono;sector;urbanizacion;direccion\n")
    for line in file:
        a=line.strip().split(",")
        nombre=a[0].title()
        apellido=a[1].title()
        sector=a[4]
        #print(sector,nombre)
        codigocliente=nombre[0].capitalize()+apellido[0].capitalize()+sector[0:2].lower()        
        telefono=a[3]        
        urbanizacion=a[5]
        direccion=a[6]
        
        
        file2.write(nombre+";"+apellido+";"+codigocliente+";"+telefono+";"+sector+";"+urbanizacion+";"+direccion+"\n")

    file.close()
    file2.close()

#sacarInfoclientes("clientesordenados2.csv","clientesprueba3.dat")

