import unittest

def suma(num_1, num_2):
    return num_1 + num_2


#Se generarán pruebas, para ello se define la clase:
class CajaNegraTest(unittest.TestCase): #Se especifica que esto es un caso de prueba
    #Se generará un Test Development:
        #Antes de escribir la función, se escriben las pruebas de esta función
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1,num_2)
        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

# def run():
#     pass    


#Se define como módulo principal la prueba
if __name__ == "__main__":
    unittest.main(verbosity=2)
