"""
@author Julian Gómez
@description: Realiza el factorial de un n número
"""

from curses.ascii import isdigit


def factorial(n):
    """Calcula el factorial de n\n
    n int > 0\n
    returns n!
    """
    #Se define un caso base, para evitar un infite loop
    if n==1:
        return 1

    #Recursividad al llamar a la misma función
    return n*factorial(n-1)

def run():
    numero = input("Ingrese el valor al que desea sacar el factorial: ")
    while numero.isdigit() == False:
        print("Ingrese un número por favor")
        numero = input()
    respuesta = factorial(int(numero))
    print(f"El factorial del número {numero} es {respuesta}")

if __name__ == "__main__":
    run()