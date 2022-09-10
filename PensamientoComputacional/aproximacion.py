def aproximacion_raiz(objetivo):
    respuesta = 0.0
    str_respuesta = ""
    epsilon = 0.01 #Medida de qué tan precisos queremos ser
    paso = epsilon**2 #Qué tanto nos iremos acercando a la respuesta en cada iteracion

    #Usaremos la función abs, que regresa el valor absoluto.
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if(abs(respuesta**2 - objetivo) >= epsilon):
        str_respuesta = f'No se encontro la raiz cuadrada de {objetivo}'
    else:
        str_respuesta = f'La raiz cuadrada de {objetivo} es {respuesta}'
    return str_respuesta


def run():
    objetivo = int(input("Ingrese un número a encontrarle raíz: "))
    print(aproximacion_raiz(objetivo))
    



if __name__ == "__main__":
    run()