def calculartotal(precio, cantidad):
    total = precio * cantidad
    return total

precio = float(input("ingrese el precio del producto: "))
cantidad = int(input("ingrse la cantidad: "))


resultado = calculartotal(precio, cantidad)
print("el total de la compra es:", resultado)