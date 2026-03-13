# inventario.py

# Solicitar el nombre del producto (tipo string)
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio del producto con validación
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# Solicitar la cantidad del producto con validación
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")

# Calcular el costo total multiplicando precio por cantidad
costo_total = precio * cantidad

# Mostrar los resultados en la consola
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

# Este programa solicita al usuario el nombre, precio y cantidad de un producto.
# Luego valida que los datos numéricos sean correctos, calcula el costo total
# multiplicando el precio por la cantidad y finalmente muestra toda la información
# del producto en la consola.