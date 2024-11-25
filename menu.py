from operaciones import sumar, restar, multiplicar

def mostrar_menu():
    print("Menú de opciones:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    
    # Pedir al usuario que seleccione una opción
    opcion = input("Seleccione una opcion (1-5): ")

    if opcion = 1:
        num1 = input("Introduce el primer numero: ")
        num2 = input("Introduce el segundo numero: ")
        sumar(num1, num2)
    elif opcion = 2:
        num1 = input("Introduce el primer numero: ")
        num2 = input("Introduce el segundo numero: ")
        restar(num1, num2)
    elif opcion = 3:
        num1 = input("Introduce el primer numero: ")
        num2 = input("Introduce el segundo numero: ")
        multiplicar(num1, num2)
    else:
        print("Opcion no valida")
    return opcion