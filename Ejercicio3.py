#3 - Dados dos conjuntos de números, escribe un programa para encontrar los números que faltan en el segundo conjunto en comparación con el primero y viceversa.

conjunto1 = {2,6,9,6,5,4}
conjunto2 = {9,6,8,7,5,2}

#numeros del conjunto1 que faltan en conjunto2
print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")
conjunto_faltan_en2 = conjunto1 - conjunto2
print(f"Numeros que faltan en el conjunto 2: {conjunto_faltan_en2}")

conjunto_faltan_en1 = conjunto2 - conjunto1
print(f"Numeros que faltan en el conjunto 1: {conjunto_faltan_en1}")