#Se importa el módulo de funciones
import logic as t


#PROGRAMA PRINCIPAL

#Creacionn de los 4 productos
p1 = t.crear_producto("Agua",  "Agua x 600 ml", "Bebidas", 1800, 30, 18, 5)
p2 = t.crear_producto("Chocoramo", "Chocoramo individual", "Panadería", 800, 25, 15, 10)
p3 = t.crear_producto("Huevos", "Caja de 6 huevos", "Víveres", 1900, 35, 38, 7)
p4 = t.crear_producto("Coca-Cola", "Botella de 330 ml", "Bebidas", 2200, 20, 3, 6)

print("Los productos de la tienda son: \n")
print(p1,p2,p3,p4)

t.subir_precios(p1,p2,p3,p4)

print("Los productos de la tienda con el precio aumentado son: \n")
print(p1,p2,p3,p4)

imc = t.producto_inventario_mas_costoso(p1,p2,p3,p4)
print(f"El producto con el inventario más costoso es {imc}")

ppt = t.cuantos_productos_por_tipo(p1,p2,p3,p4)
print(f"Numero de productos por tipo: {ppt}")