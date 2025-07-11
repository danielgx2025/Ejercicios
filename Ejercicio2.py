# Crea un programa que permita crear un conjunto desde cero y después me permita eliminar un elemento de un conjunto si está presente en el conjunto.
# creo el conjunto
conjunto = set()
#ingreso numeros hasta que ingrese el 0
while True:
    Numero = input("Ingresa numeros para crear un conjunto, o ingresa 0 para dejar de ingresar: ")
    if Numero == '0':
        break
    conjunto.add(Numero)

print(f"El conjunto ingresado es: {conjunto}")

# aqui voy a eliminar un item del conjunto
while True:
    NumeroEliminar = input("Ingrese el numero a eliminar, o ingresa 0 para salir del while: ")
    if NumeroEliminar == '0':
        break
    if NumeroEliminar in conjunto:
        conjunto.discard(NumeroEliminar)
    else:
        print(f"El numero a eliminar no exite en el conjunto")

    if not conjunto:
        print(f"El conjunto quedo vario")
        break
    
print(f"El conjunto de salida es: {conjunto}")