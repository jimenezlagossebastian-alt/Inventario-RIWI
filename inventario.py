# inventario.py

# pedir nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# pedir precio (float) con validación
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# pedir cantidad (int) con validación
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")

# mostrar los datos ingresados
print("\nProducto registrado:")
print("Nombre:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)