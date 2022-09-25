#Variable con Scope Global, todos pueden acceder a ella
var_global = 10

def funcionVarLocal():
    var_global = "Hola"
    print(f"La variable local, que se llama como la global tiene el valor de: {var_global}")


#Función con Scope global
def pruebaGlobal(variable):
    #Se define una variable que puede ser accedida por todos
    global x
    x = 20*variable


#Función con Scope global, todos pueden acceder a ella
def funcionInFuncion():
    print(f'El valor de la función global "funcionInFuncion" es el valor global "var_global": {var_global}\n')

def funcion(var_global):
    #Variable con Scope local, sólo esta función puede acceder a ella
    por_tres = var_global*3
    print(f"El valor de la variable Local 'por_tres' es de {por_tres}, en la función 'funcion'\n")

    #Función con Scope local, sólo esta función a la que pertenece la puede usar y por eso se puede repetir en otros lados
    def funcionInFuncion(var):

        #Variable con scope local, solo esta función puede acceder a ella
        valor = var*var_global
        print(f"El valor del a variable local 'valor', de la función local (En la sub-función 'funcionInFuncion') es de {valor}\n")
        print(f"El valor de la variable local de la función a la que pertenezco es de: {por_tres}")

    return funcionInFuncion(por_tres)

def run():
    #Variables locales de la función principal "Run"
    var = "Soy una variable local de la función 'Run'"
    y = 2

    #Llamado a función global
    funcionInFuncion()
    #Llamado a función global, dándole el parámetro de la variable global
    funcion(var_global)
    #Se imprime el valor de la variable local
    print(f"El valor de la variable local de la función global principal 'Run' es de: {var}")
    
    pruebaGlobal(2)

    print(f"Accediendo a una variable global, que no es de mi Scope, encuentro que la variable global X tiene el valor de: {x}")
    print(f"El valor de la otra variable global es de: {var_global}")

    funcionVarLocal()


if __name__ == "__main__":
    run()
