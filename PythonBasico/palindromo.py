def palindromo(palabra):
    #Primero se debe eliminar los espacios intermedios
    palabra = palabra.replace(" ", "")
    #Convertimos todo a minúsculas
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es Palíndromo")
    else:
        print("No es Palíndromo")


if __name__ == "__main__":
    run()