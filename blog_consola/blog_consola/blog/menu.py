"""Menú e interacción con el usuario (input)."""


def mostrar_menu():
    """Muestra el menú, pide una opción y la devuelve."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    return input("Elegí una opción: ").strip()


def pedir_texto(mensaje):
    """Pide un texto al usuario y lo devuelve sin espacios sobrantes."""
    return input(mensaje).strip()
