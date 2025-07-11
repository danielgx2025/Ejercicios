# Escriba un programa en Python para eliminar todos los duplicados de una lista de cadenas dada y devolver una lista de cadenas únicas.
# creo lista
Lista = []
#ingreso numeros hasta que ingrese el 0
while True:
    Numero = input("Ingresa numeros para crear una Lista, o ingresa 0 para dejar de ingresar: ")
    if Numero == '0':
        break
    Lista.append(Numero)

print(f"La Lista ingresado es: {Lista}")

# una vez ingresada la lista con repetidos lo llevo a un conjunto lo que me elimina los repetidos por el solo hecho de llevarlo a un set
lista_sin_duplicados = list(set(Lista))
print(f"La Lista sin duplicado es: {lista_sin_duplicados}")