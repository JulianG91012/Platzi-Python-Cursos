"""
@author Julian Gómez
@description: Código que crea tuplas y trabaja con ellas.
"""
from curses.ascii import isdigit


def crearTuplas(tamanno):
    """Crea tuplas según lo solicitado por el usuario\n
    tamanno int: Cualquier int > 0\n
    returns mensaje de creacion de tupla + tupla
    """
    l_temporal = []
    
    for i in range (0,int(tamanno)):
        values = input("Ingrese un valor a agregar en la tupla: ")
        if values.isdigit():
            if type(values) == int:
                print(f"El valor ingresado es de tipo: {type(values)}")
                values = int(values)
        l_temporal.append(values)

    tupla = tuple(l_temporal)
    print(f"La tupla fue creada exitosamente, tiene un tamaño de: {len(tupla)} y es: {tupla}")

def run():
    n_valores = input("Ingrese la cantidad de valores que desea que tenga su tupla: ")
    crearTuplas(n_valores)

if __name__ == "__main__" :
    run()
