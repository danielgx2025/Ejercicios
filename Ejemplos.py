
def sumar(a:int|float,b:int|float) -> int|float:
    """Sumar dos valores que se ingresar como enteros

    Args:
        a (int): Primer argumento a sumar
        b (int): Segundo argumento a sumar

    Returns:
        int: la suma de los valores
    """
    return a + b

valor = sumar(6.8,9.6)
print(valor)

#List Compreention
cuadrados = [x**2 for x in range(6)]
print(cuadrados)

#Que es un generador
