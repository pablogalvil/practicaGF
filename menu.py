from operaciones import sumar, restar, multiplicar, dividir,factorial_iterativo, factorial_rescursivo, fibonacci

def mostrar_menu():
    print("Menú de opciones:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("8- Fibonacci")
    
    # Pedir al usuario que seleccione una opción
    opcion = input("Seleccione una opcion (1-5): ")

    if opcion == '1':
        num1 = input("Introduce el primer numero: ")
        num2 = input("Introduce el segundo numero: ")
        
        num1 = float(num1)
        num2 = float(num2)
        
        resultado = sumar(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == '2':
        num1 = input("Introduce el primer numero: ")
        num2 = input("Introduce el segundo numero: ")
        
        num1 = float(num1)
        num2 = float(num2)
        
        resultado = restar(num1, num2)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == '3':
        num1 = input("Introduce el primer numero: ")
        num2 = input("Introduce el segundo numero: ")
        
        num1 = float(num1)
        num2 = float(num2)
        
        resultado = multiplicar(num1, num2)
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == '4':
        # Opción de dividir
        try:
            # Pedir los dos números al usuario
            num1 = input("Introduce el primer valor (int o float): ")
            num2 = input("Introduce el segundo valor (int o float): ")
            # Convertir las entradas a tipo float
            num1 = float(num1)
            num2 = float(num2)
            # Llamar a la función dividir
            resultado, residuo = dividir(num1, num2)
            # Mostrar el resultado de la división
            print(f"Resultado de la división: {resultado}, Residuo: {residuo}")
        except ValueError as e:
            # Si hay un error con el tipo de dato o la división por cero
            print(f"Error: {e}")
    elif opcion == '5':
        # Opción de salir
        print("Saliendo...")
    elif opcion == 6:
        numero = int(input("Ingrese un número para calcular su factorial: "))
        resultado = factorial_iterativo(numero)
        print(f"El factorial de {numero} es {resultado}")
    elif opcion == '6':
        num1 = input("Introduce el primer numero: ")
        
        num1 = int(num1)
        
        print(f"El factorial de {num1} es {factorial_rescursivo(num1)}")
    elif opcion == '8':
        num1 = input("Introduce el primer numero: ")

        num1 = int(num1)

        print(f"El fibonacci de {num1} es {fibonacci_iterativo(num1)}")
    else:
        print("Opcion no valida")
    return opcion