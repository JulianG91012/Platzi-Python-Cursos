def binarySearch(number):
    epsilon = 0.01
    low = 0.0
    high = max(1.0, number)#Si el objetivo es menor a 1.0 se empieza en 1.0
    result = (high + low /2)

    while abs(result**2 -number) >= epsilon:
        print(f'Low value is: {low} and high value is {high}, respuesta is {result}')
        if result**2 < number:
            low = result
        else:
            high = result
        result = (high + low)/2
    print(f'La raiz cuadrada de {number} es {result}')

def run():
    objetivo = int(input("Escoge un numero: \n"))
    binarySearch(objetivo)


if __name__ == "__main__":
    run()
