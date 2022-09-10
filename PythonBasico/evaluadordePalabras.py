def evaluadorLetraO(cadena_ingresada):
    caracter_a_evaluar = "O"
    i = 0
    for letra in cadena_ingresada:
        if letra.upper() != caracter_a_evaluar:
            print("El caracter #" + str(i) + " Es una: " + letra)
            i+=1
        elif letra.upper() == caracter_a_evaluar:
            print("El caracter #" + str(i) + " No pasa la prueba")
            i+=1
        else:
            print("El caracter no es una letra.")


def run():
    #Imprimiendo #s pares desde 0 hasta 1000
    # for contador in range(1001):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    #Interrumpiendo contador con número específico
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    cadena_ingresada = input("Ingrese una frase, el sistema evaluará si contine la letra O: ")
    evaluadorLetraO(cadena_ingresada)

    # i = 0
    # while i < len(cadena_ingresada):
    #     print("La posicion 1 de su cadena tiene el caracter: " + cadena_ingresada[i])
    #     i +=1

    


if __name__ == "__main__":
    run()

