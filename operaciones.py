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

# operaciones.py

def factorial_iterativo(n):
    # Verificar si el número es un entero
    if not isinstance(n, int):
        return "Error: El valor ingresado no es un número entero."
    
    # Verificar si el número es negativo
    if n < 0:
        return "Error: El número debe ser mayor o igual a 0."

    # Calcular el factorial de manera iterativa
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# operaciones.py

def factorial_iterativo(n):
    # Verificar si el número es un entero
    if not isinstance(n, int):
        return "Error: El valor ingresado no es un número entero."
    
    # Verificar si el número es negativo
    if n < 0:
        return "Error: El número debe ser mayor o igual a 0."

    # Calcular el factorial de manera iterativa
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_rescursivo(num1):
    if not isinstance(num1, (int)):
        raise ValueError("El valor debe ser int.")
    else:
        if num1 == 0:
            return 1
        else:
            return num1 * factorial_rescursivo(num1-1)
            def fibonacci_iterativo(num):
    if not isinstance(num, (int)):
        raise ValueError("El valor debe ser int.")
    else:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            a = 0
            b = 1
            for i in range(2, num):
                c = a + b
                a = b
                b = c
            return b