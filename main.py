# Importar la función mostrar_menu desde menu.py
from menu import mostrar_menu

if __name__ == "__main__":
    # Llamar a la función mostrar_menu
    opcion = mostrar_menu()
    print(f"Has seleccionado la opción: {opcion}")
