
#Imprimir el menú general con las opciones válidas.
def printMenu():
    options =""" 
    1. Raíz Cuadrada por Enumeración 
    2. Raíz Cuadrada por Aproximación
    3. Raíz Cuadrada por Búsqueda Binaria
    4. Si desea salir del programa
    """
    print(options) 

#Validar la respuesta del usuario con las opciones disponibles.
def printOpciones():
    option_selected = input()
    while option_selected not in ["1","2","3","4"]:
        print(f"No ha ingresado una opción válida. Intente nuevamente")
        option_selected = input()
    return option_selected

#Recibe la respuesta del usuario y en base a ello realiza lo solicitado
def opcionElegida(eleccion, number):
    if eleccion == "1":
        enumeracion(number)
    elif eleccion == "2":
        aproximacion(number)
    elif eleccion == "3":
        busqueda_binaria(number)
    if eleccion == "4":
        print("Cerrando programa...")
        return 1

#Resolver una raíz cuadrada por el método de la Enumeración
def enumeracion(number):
    respuesta = 0
    number = int(number)
    while respuesta**2 < number:
        respuesta +=1 
    if respuesta**2 == number:
        print(f'La raíz cuadrada de {number} es {respuesta}\n')
    else:
        print(f'El {number} no tiene una raiz cuadrada exacta\n')

#Resolver una raíz cuadrada por el método de la aproximación
def aproximacion(number):
    epsilon = 0.01
    number = int(number)
    respuesta = 0.0
    paso = epsilon**2 #Qué tanto nos iremos acercando a la respuesta en cada iteracion
    while abs(respuesta**2 - number) >= epsilon and respuesta <= number:
        print(abs(respuesta**2 - number), respuesta)
        respuesta += paso

    if(abs(respuesta**2 - number) >= epsilon):
        str_respuesta = print(f'No se encontro la raiz cuadrada de {number}\n')
    else:
        str_respuesta = print(f'La raiz cuadrada de {number} es {respuesta}\n')
        print(f'Para este Método, se usó la medida epsilon de {epsilon} (Esto es la medida de qué tan precisos queremos ser)')

#Resolver una raíz cuadrada por el método de la Búsqueda Binaria
def busqueda_binaria(number):
    number = int(number)
    epsilon = 0.01
    print(f'Para este Método, se usó la medida epsilon de {epsilon} (Esto es la medida de qué tan precisos queremos ser)')
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
    print(f'La raiz cuadrada de {number} es {result}\n')

#Preguntarle al usuario si desea realizar la raíz con otro método
def lastMenu(number):
    print("¿Desea usar algún otro método?")
    print("Escriba 1 para intentar otro método")
    print("Escriba 2 Para salir del programa")
    respuesta = input()
    while respuesta not in ["1","2"]:
        respuesta = input("Ingrese una de las opciones correctas\n")
    if respuesta == "1":
        print(f"Vamos a trabajar con el número {number}, que se ingresó al principio.")
        printMenu()
        eleccion = printOpciones()
        if opcionElegida(eleccion, number) != 1:
            lastMenu(number)
    if respuesta == "2":
        print("Gracias, terminando programa...")


def run():
    print("Hola, mediante este algoritmo puedes realizar la raíz cuadrada de un número\n")
    number = input("Ingresa el número al que quieres sacar la raíz cuadrada: ")
    print("Ahora ingresa el método con el que quieres realizar la raíz: ")
    printMenu()
    eleccion = printOpciones()
    if opcionElegida(eleccion, number) != 1:
        lastMenu(number)


if __name__ =="__main__":
    run()