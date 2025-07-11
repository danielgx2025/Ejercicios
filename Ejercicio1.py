# 1 - Crea una función que reciba una lista de números y la ordene de menor a mayor. La función debe devolver la lista ordenada (Debe usar set).
#############################################################################
def ordenarLista(lista_numeros):
    #Ordenar una lista de numeros de menor a mayor
    #con el set elimino los duplicados, y luego de eliminar los duplicados, lo llevo de nuevo a la lista sin duplicados
    lista_sin_duplicados = list(set(lista_numeros))
    #Ordeno la lista
    lista_ordenada = sorted(lista_sin_duplicados)
    #retorno la lista
    return lista_ordenada

#llama a la funcion
lista = [5,8,9,6,5,72,39,52,45,8,39]
print(f"Lista Orginal : {lista}")
lista_final = ordenarLista(lista)
print(f"Lista Ordenada: {lista_final}")
#########################################################################



