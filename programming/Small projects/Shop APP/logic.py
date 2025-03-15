
def crear_producto(nombre: str, descripcion: str, tipo: str, valor_unitario: float, cantidad_bodega: int, cantidad_vendida: int, cantidad_minima: int) -> dict:

    dic = { "nombre": nombre,
           "descripcion": descripcion,
           "tipo": tipo,
           "valor_unitario": valor_unitario,
           "cantidad_bodega": cantidad_bodega,
           "cantidad_vendida": cantidad_vendida,
           "cantidad_minima": cantidad_minima }
    return dic

def subir_precio_producto(producto):
    if producto["valor_unitario"] < 1000:
        producto["valor_unitario"] += producto["valor_unitario"]*0.01

    elif producto["valor_unitario"] <= 2000:
        producto["valor_unitario"] += producto["valor_unitario"]*0.02

    elif producto["valor_unitario"] > 2000:
        producto["valor_unitario"] += producto["valor_unitario"]*0.03

def subir_precios(p1,p2,p3,p4):
    subir_precio_producto(p1)
    subir_precio_producto(p2)
    subir_precio_producto(p3)
    subir_precio_producto(p4)

    
def producto_inventario_mas_costoso(p1,p2,p3,p4):
    ci2 = p2["valor_unitario"] * p2["cantidad_bodega"]
    ci3 = p3["valor_unitario"] * p3["cantidad_bodega"]
    ci4 = p4["valor_unitario"] * p4["cantidad_bodega"]


    imc = p1

    if ci2 > imc["valor_unitario"] * imc["cantidad_bodega"]:
        imc = p2

    if ci3 > imc["valor_unitario"] * imc["cantidad_bodega"]:
        imc = p3

    if ci4 > imc["valor_unitario"] * imc["cantidad_bodega"]:
        imc = p4
    return imc
    
def cuantos_productos_por_tipo(p1,p2,p3,p4):
    ppt = {}

    tipo1 = p1["tipo"]
    tipo2 = p2["tipo"]
    tipo3 = p3["tipo"]
    tipo4 = p4["tipo"]

    ppt[tipo1] = 1

    if tipo2 in ppt:
        ppt[tipo2] += 1
    else:
        ppt[tipo2] = 1

    if tipo3 in ppt:
        ppt[tipo3] += 1
    else:
        ppt[tipo3] = 1

    if tipo4 in ppt:
        ppt[tipo4] += 1
    else:
        ppt[tipo4] = 1

    return ppt


  



