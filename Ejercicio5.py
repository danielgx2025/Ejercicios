# Crea una función llamada factorial que reciba un número entero positivo y devuelva su factorial. Ejemplo: factorial(4) debe devolver 24

Numero = int(input("Ingrese un numero para calcular su factorial: "))
factorial = 1
if Numero == 0:
    factorial = 1
elif Numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    # Por ejemplo, si Numero es 5, queremos multiplicar 5 * 4 * 3 * 2 * 1
    for i in range(1, Numero + 1):
        factorial = factorial * i

print(f"El factorial del numero: {Numero} es: {factorial}")


