cantidad_pesos = float(input("Ingrese la cantida de pesos Colombianos que posee: "))
cantidad_dolares = float(input("Ingrese la cantidad de dolares que posee: "))
valor_dolar = 4408
valor_cop = 0.00023

conversion_a_dolar = round(cantidad_pesos / valor_dolar,2)
conversion_a_dolar = str(conversion_a_dolar)

conversion_a_peso = round(cantidad_dolares / valor_cop,2)
conversion_a_peso = str(conversion_a_peso)


print("Sus pesos colombianos convertidos a dolares da un total de: $" + conversion_a_dolar)
print("Sus dólares convertidos a pesos colombianos da un total de: $" + conversion_a_peso)