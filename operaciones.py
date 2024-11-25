def sumar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Ambos valores deben ser int o float.")
    else:
        return (num1+num2)

def restar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Ambos valores deben ser int o float.")
    else:
        return (num1-num2)

def multiplicar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Ambos valores deben ser int o float.")
    else:
        i = 1
        resultado = num1
        while (i <= num2):
            resultado = resultado + num1
            i = i + 1
        return (num1)

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
