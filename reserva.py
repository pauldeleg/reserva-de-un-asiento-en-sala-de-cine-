#crear una matriz 3x4 llamada asientos
asientos = [[0 for columna in range(4)]for fila in range(3)]

#pedir datos al usuario
fila = int(input("ingrese la fila  (0 - 2): "))
columna = int(input("ingrese la columna (0 - 3): ")) 

#marcar asiento como ocupado
if 0 <= fila < 3 and 0 <= columna < 4:
    if asientos[fila - 1][columna - 1] == 0:
        asientos [fila - 1][columna - 1] = 1
        print("asiento reservado correctamente.")
    else:
        print("ese asiento ya esta ocupado.")
else:
    print("posición invalida.")


#mostrar la matriz completa en formato tabla 
print("\nestado de la sala:")
for fila in range(3):
    for columna in range(4):
        print(asientos[fila][columna], end="\t")
    print()    