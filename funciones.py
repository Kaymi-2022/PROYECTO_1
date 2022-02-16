listado=[]
def IngresoDatos(cliente,cantidad,precio,total,igv,total_pagoT):
    listado.extend([cliente,cantidad,precio,total,igv,total_pagoT])

def calcularTotal(cantidad):
    precioTotal=Precio(cantidad)*cantidad
    return precioTotal

def igv (cantidad):
    IGV=calcularTotal(cantidad)*0.18
    return IGV

def pagoTotal (precio,cantidad):
    PagoTotal=calcularTotal(precio,cantidad)-igv(precio,cantidad)
    return PagoTotal

def Precio(cantidad):
    if cantidad<5:
        precio=300
    elif cantidad<10:
        precio=250
    else:
        precio=200
    return precio


