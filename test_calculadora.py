from calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar (2,3 == 5)
    assert sumar (0,sumar(1,1) == 2)
    assert sumar (8,-8) == 0
    assert sumar (1234, 1234 == 2468) 

def test_restar():
    assert restar (2,3 == -1)
    assert restar (0,restar(4,2) == 2)
    assert restar (8,-8 == 0)
    assert restar (-1234, -1234 == -2468 ) 

def test_multiplicar(self):
        # Prueba básica de multiplicación
        self.assertEqual(multiplicar(2, 3), 6)

        # Prueba con números negativos
        self.assertEqual(multiplicar(-2, 3), -6)
        self.assertEqual(multiplicar(2, -3), -6)

        # Prueba con cero
        self.assertEqual(multiplicar(0, 3), 0)
        self.assertEqual(multiplicar(3, 0), 0)

        # Prueba con números grandes
        self.assertEqual(multiplicar(1000000, 1000000), 1000000000000)


def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-6, 3), -2)
        self.assertEqual(dividir(0, 3), 0)
        self.assertEqual(dividir(6, 0), "Error: No se puede dividir entre cero")
        self.assertEqual(dividir(0, 0), "Error: No se puede dividir cero entre cero")