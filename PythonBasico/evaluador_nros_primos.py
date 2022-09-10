def es_primo(numero):
    #Se crea un contador que servirá para saber la cantida de veces que es divisible el numero ingresado
    contador = 0

#Se crea un ciclo que evalúa cada número desde 1 hasta el número ingresado
    for i in range(1, numero+1):
        #Si el número es 1 o es el mismo número evaluado significa que si es primo, por lo que se evalúa el siguiente (Si lo hay)
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero): #No es necesario el == True, debido a que Python lo sobreentiende
        print("Es Primo")
    else:
        print("No es Primo")

if __name__ == "__main__":
    run()