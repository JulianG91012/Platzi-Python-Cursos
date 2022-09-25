



from unittest.util import sorted_list_difference


def run():
    #Aquí se explicarán y se darán ejemplos de las funciones principales que tiene una lista en Python:
    my_list = list(range(0,101,5))

    #Extend: extiende la lista con valores dentro de un iterable como un range()
    my_list.extend(range(0,31,3))

    #Insert: Agrega un elemento a la lista en el índice especificado, seguido del elemento a agregar
    my_list.insert(len(my_list),"Hola")

    #Pop: Saca de la lista el último elemento que tenga, a menos que se especifique el índice del elemento a sacar
    my_list.pop(0)

    #Remove: Elimina el primer elemento que tenga el valor especificado
    my_list.remove("Hola")

    #Index: Retorna la posición del primer elemento que tenga el valor especificado
    print(f'El valor especificado es 50, su posición en la lista es: {my_list.index(50)}')

    #Index: Retorna la posición del primer elemento que tenga el valor específicado, buscando desde donde se le especifique y
        #terminando donde se le especifique
    print(f'El valor especificado es 15, se empieza a buscar desde la posición 5 hasta el final, la posición encontrada es: {my_list.index(15,5,len(my_list))}')

    #Count: Cuenta cuántas veces aparece el valor especificado en la lista
    print(f'El valor especificado es 30, aparece {my_list.count(30)} veces\n')

    #Sort: Organiza los elementos de una lista de mayor a menor, a menos que se le indique lo contrario
    #my_list.sort()
    
    #Copy: Clona una lista
    sorted_list = list.copy(my_list)
    sorted_list.sort()
    reverse_list = list.copy(my_list)
    reverse_list.sort(reverse=True)
    

    #Se comprueba si son listas diferentes
    print(f"El Id de my_list es {id(my_list)}")
    print(f"El Id de reverse_list es {id(reverse_list)}")
    print(f"El Id de sorted_list es: {id(sorted_list)}")
    

    print(f"La lista normal es: {my_list}\n")
    print(f"La lista ordenada es: {sorted_list}\n")
    print(f"La lista ordenada de mayor a menor es: {reverse_list}")
    


if __name__ == "__main__":
    run()

