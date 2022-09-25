import unittest

#[1] Se asume que el código ya está escrito, así que es lo que haremos primero
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
    #Se debe revisar todos los caminos, en este caso son 2 test


class PruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)

# def run():
#     pass    

if __name__ == "__main__":
    unittest.main(verbosity=2)
