from menu import mostrar_menu
from operaciones import dividir

if __name__ == "__main__":
    while True:
        # Mostrar el menú
        opcion = mostrar_menu()

        # Comprobar la opción seleccionada
        if opcion == '1':
            # Implementar sumar (esto sería otro código)
            pass
        elif opcion == '2':
            # Implementar restar (esto sería otro código)
            pass
        elif opcion == '3':
            # Implementar multiplicar (esto sería otro código)
            pass
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
            break
        else:
            print("Opción no válida, por favor elige una opción entre 1 y 5.")
