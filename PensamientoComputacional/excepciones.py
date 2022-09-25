def divide_elementos_de_lista(lista, divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

def run():
    lista = list(range(10))
    divisor = 0

    print(divide_elementos_de_lista(lista, divisor))

if __name__ == "__main__":
    run()

