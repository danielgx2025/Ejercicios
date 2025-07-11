# Dado un texto con información estructurada, escribí un programa que extraiga los datos usando
# slicing y los devuelva como un diccionario. A partir de un texto como el siguiente, la funcion deberia retornar el siguiente diccionario:
# Trabajo practico 1 text = "Nombre: Juan Pérez | Edad: 30 | Ciudad: Salta" slicing_function(text) # {"nombre": "Juan Perez", "edad" : 30, "ciudad": "Salta"}

def slicing_function(text):
    data = {}
    # Dividir el texto en partes individuales por el separador '|'
    parts = text.split('|')

    for part in parts:
        # En cada parte, encontrar la posición del ":"
        colon_index = part.find(':')

        if colon_index != -1:
            # Extraer el nombre del campo (antes del ":") y limpiarlo
            field_name = part[:colon_index].strip().lower()

            # Extraer el valor (después del ":") y limpiarlo
            field_value = part[colon_index + 1:].strip()

            # Intentar convertir el valor a entero si es posible (para 'edad')
            try:
                data[field_name] = int(field_value)
            except ValueError:
                data[field_name] = field_value

    return data

# Ejemplo de uso:
text = "Nombre: Juan Pérez | Edad: 30 | Ciudad: Salta"
result = slicing_function(text)
print(result)

# Otro ejemplo
text2 = "Pais: Argentina | Provincia: Salta | Habitantes: 1400000"
result2 = slicing_function(text2)
print(result2)