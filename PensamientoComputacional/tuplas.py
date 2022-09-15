"""
@author Julian Gómez
@description: Código que crea tuplas y trabaja con ellas.
"""

def validar_num(num):
    """Recibe un valor que debería ser un número y lo valida como tal\n
    num string: cualquier string\n
    num_t numero: copia del valor original convertido en numero\n
    returns int(num_t)
    """
    num_t = num
    if num.isnumeric():
        num_t = int(num)
    else:
        while num_t.isnumeric() == False:
            num_t = input("Ingrese un valor numérico.\n")
        num_t = int(num_t)
    return num_t
    



def crearTuplas(tamanno):
    """Crea tuplas según lo solicitado por el usuario\n
    tamanno int: Cualquier int > 0\n
    returns mensaje de creacion de tupla + tupla
    """
    l_temporal = []
    
    for i in range (0,int(tamanno)):
        values = input("Ingrese un valor a agregar en la tupla: ")
        if values.isnumeric():
            print("¿Desea ingresarlo como String o como número?")
            resp = input("Escriba S para string, N para número: ")

            while resp not in ["s","n"]:
                resp = input("Ingrese una letra correcta.\n")
            if resp.lower() == "s":
                values = str(values)
            elif resp.lower() == "n":
                values = int(values)
            
        l_temporal.append(values)

    tupla = tuple(l_temporal)
    print(f"La tupla fue creada exitosamente, tiene un tamaño de: {len(tupla)} y es: {tupla}")

def run():

    n_valores = input("Ingrese la cantidad de valores que desea que tenga su tupla: ")
    crearTuplas(validar_num(n_valores))

if __name__ == "__main__" :
    run()
