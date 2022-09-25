"""
@author: Julian Gómez
@description: Programa que explica el tipo de dato "rangos"
"""

def run():
    #Generar rango que imprima numeros impares
    rango_impares = range(0,100,2)
    for i in rango_impares:
        print(f"N° impar: {i+1}\t",end="")

if __name__ == "__main__":
    run()