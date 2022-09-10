#Imprimir todas las potencias de 2 hasta llegar a 1k
def potencias_de_dos(numero):
    BASE = 2
    exponente = 0
    resultado = 0 
    while resultado < numero:
        resultado = BASE ** exponente
        print("La operación 2^" + str(exponente) + " es igual a: " + str(resultado))
        exponente = exponente +1
        resultado = BASE ** exponente


def run():
    numero = int(input("Escriba el número hasta el que desea imprimir las potencias de 2: "))
    potencias_de_dos(numero)


if __name__ == "__main__":
    run()
