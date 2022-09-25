"""
@author Julián Gómez
@description: Programa acerca de los docstrings
"""

def funcionSuma(numero1, numero2):
    """Realiza la adición de dos números del mismo tipo\n
        numero1 int: Cualquier nro entero
        numero2 int: Cualquier nro entero\n
        returns numero1 + numero2
    """
    return numero1 + numero2


def run():
    num1 = 5
    num2 = 2
    valor_suma = funcionSuma(num1,num2)
    print(f"La suma de el número {num1} y el número {num2} es: {valor_suma}")
    documentacion = str(funcionSuma.__doc__)
    print(f"La documentación de la función llamada 'funcionSuma' es:\n {documentacion}")
    
    # print(help(funcionSuma))


if __name__ == "__main__":
    run()