def sumar(num1, num2):
    if ((num1.isinteger() or num1.isdecimal()) and (num2.isinteger() or num2.isdecimal())):
        return (num1+num2)
    else:
        print("No son enteros o float")

def restar(num1, num2):
    if ((num1.isinteger() or num1.isdecimal()) and (num2.isinteger() or num2.isdecimal())):
        return (num1-num2)
    else:
        print("No son enteros o float")

def multiplicar(num1, num2):
    if ((num1.isinteger() or num1.isdecimal()) and (num2.isinteger() or num2.isdecimal())):
        i = 1
        resultado = num1
        while (i <= num2):
            resultado = resultado + num1
            i = i + 1
        return (num1)
    else:
        print("No son enteros o float")

def dividir(a, b):
    # Comprobar que los valores sean int o float
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos valores deben ser int o float.")
    
    # Comprobar que el divisor no sea cero
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    
    # Realizar la división de forma iterativa
    resultado = 0
    while a >= b:
        a -= b
        resultado += 1

    # Si la división no es exacta, se devuelve el residuo
    residuo = a
    return resultado, residuo
