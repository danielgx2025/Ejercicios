# Crea una función recursiva llamada suma_recursiva que reciba un número n y devuelva la suma de los primeros  n números naturales. Ejemplo:
# suma_recursiva(5) debe devolver 15 (1+2+3+4+5).

def suma_recursiva(numero):
    if numero <= 0:
        return 0
    else:
        return numero + suma_recursiva(numero - 1)
    
Numero = int(input("Ingrese un numero para calcular : "))    
numerovalor = suma_recursiva(Numero)
print(f"El valor de la suma del numero: {Numero} es: {numerovalor}")
