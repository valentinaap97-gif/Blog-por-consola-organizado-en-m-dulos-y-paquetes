"""Punto de entrada del blog por consola."""

from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu
from blog import operaciones


def main():
    blog = cargar_posts()

    acciones = {
        "1": operaciones.ver_posts,
        "2": operaciones.buscar_posts,
        "3": operaciones.filtrar_posts,
        "4": operaciones.crear_post,
        "5": operaciones.validar_posts,
        "6": operaciones.guardar,
    }

    while True:
        opcion = mostrar_menu()
        if opcion == "7":
            if blog.modificado:
                print("Hay cambios sin guardar. Guardando antes de salir...")
                guardar_posts(blog)
            print("¡Hasta luego!")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida. Elegí un número del 1 al 7.")
        else:
            accion(blog)


if __name__ == "__main__":
    main()
