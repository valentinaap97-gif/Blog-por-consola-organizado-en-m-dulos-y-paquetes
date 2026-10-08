"""Archivo principal: coordina el menú y llama a las operaciones del blog."""

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


def validar_todos(lista):
    """Valida cada post y muestra cuáles son válidos y cuáles tienen errores."""
    for i, post in enumerate(lista, start=1):
        errores = validar_post(post)
        titulo = post.get("titulo") or "(sin título)" if isinstance(post, dict) else "(no es un post)"
        if errores:
            print(f"Post {i} - {titulo}: INVÁLIDO")
            for error in errores:
                print(f"   - {error}")
        else:
            print(f"Post {i} - {titulo}: válido")


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            listar_posts(posts)
        elif opcion == "2":
            termino = pedir_texto("Término a buscar: ")
            resultados = buscar_por_titulo(posts, termino)
            if resultados:
                listar_posts(resultados)
            else:
                print(f"No se encontraron posts con '{termino}' en el título.")
        elif opcion == "3":
            tag = pedir_texto("Tag a filtrar: ")
            resultados = filtrar_por_tag(posts, tag)
            if resultados:
                listar_posts(resultados)
            else:
                print(f"No hay posts con el tag '{tag}'.")
        elif opcion == "4":
            validar_todos(posts)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elegí un número del 1 al 5.")


if __name__ == "__main__":
    main()
