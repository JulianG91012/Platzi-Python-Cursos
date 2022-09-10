def conversor(tipo_pesos, valor_dolar):
    cantidad_pesos = float(input("Ingrese la cantidad de pesos " + tipo_pesos + "que posee: "))
    conversion_a_dolar = round(cantidad_pesos / valor_dolar,2)
    conversion_a_dolar = str(conversion_a_dolar)
    print("Sus pesos Colombianos convertidos a dolares da un total de: $" + conversion_a_dolar)




menu = """
Bienvenido al conversor de dolares 🪙

1. A Pesos Colombianos
2. A Pesos Mexicanos
3. A Pesos Argentinos

Elige una de las 3 opciones: """

opcion = int(input(menu))

if opcion == 1:
    # cantidad_pesos = float(input("Ingrese la cantida de pesos Colombianos que posee: "))
    # valor_dolar = 4408
    # conversion_a_dolar = round(cantidad_pesos / valor_dolar,2)
    # conversion_a_dolar = str(conversion_a_dolar)
    # print("Sus pesos Colombianos convertidos a dolares da un total de: $" + conversion_a_dolar)
    conversor("Colombianos", 4408)
elif opcion == 2:
    # cantidad_pesos = float(input("Ingrese la cantida de pesos Mexicanos que posee: "))
    # valor_dolar = 20.54
    # conversion_a_dolar = round(cantidad_pesos / valor_dolar,2)
    # conversion_a_dolar = str(conversion_a_dolar)
    # print("Sus pesos Mexicanos convertidos a dolares da un total de: $" + conversion_a_dolar)
    conversor("Mexicanos", 20.54)
elif opcion == 3:
    # cantidad_pesos = float(input("Ingrese la cantida de pesos Argentinos que posee: "))
    # valor_dolar = 129.05 
    # conversion_a_dolar = round(cantidad_pesos / valor_dolar,2)
    # conversion_a_dolar = str(conversion_a_dolar)
    # print("Sus pesos Argentinos convertidos a dolares da un total de: $" + conversion_a_dolar)
    conversor("Argentinos", 129.05)
else: 
    print("El valor que ha ingresado no está en las opciones.")