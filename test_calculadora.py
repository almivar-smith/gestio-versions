from calculadora import sumar, restar

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
