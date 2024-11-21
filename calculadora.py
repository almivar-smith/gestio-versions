# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if a == 0 and b == 0:
        return "Error: No se puede dividir cero entre cero"
    elif b == 0:
        return "Error: No se puede dividir entre cero"
    elif a == 0:
        return 0  # Dividir 0 por cualquier número no es un error, el resultado es 0
    else:
        return a / b