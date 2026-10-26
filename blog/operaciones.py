"""Operaciones del menú: piden datos al usuario y llaman a los métodos de Blog."""

from blog.datos import guardar_posts
from blog.menu import pedir_texto
from blog.modelos import Autor
from blog.validaciones import ESTADOS_POST


def ver_posts(blog):
    """Opción 1: muestra todos los posts."""
    blog.listar_posts()


def buscar_posts(blog):
    """Opción 2: busca posts por título."""
    termino = pedir_texto("Título a buscar: ")
    if not termino:
        print("Error: tenés que escribir algo para buscar.")
        return
    resultados = blog.buscar_por_titulo(termino)
    if not resultados:
        print(f"No se encontraron posts con '{termino}' en el título.")
        return
    blog.listar_posts(resultados)


def filtrar_posts(blog):
    """Opción 3: filtra posts por tag."""
    tag = pedir_texto("Tag a filtrar: ")
    if not tag:
        print("Error: tenés que escribir un tag.")
        return
    resultados = blog.filtrar_por_tag(tag)
    if not resultados:
        print(f"No hay posts con el tag '{tag}'.")
        return
    blog.listar_posts(resultados)


def crear_post(blog):
    """Opción 4: pide los datos y crea un nuevo Post dentro del Blog."""
    print("\n--- Nuevo post ---")
    titulo = pedir_texto("Título: ")
    contenido = pedir_texto("Contenido: ")
    nombre = pedir_texto("Nombre del autor: ")
    bio = pedir_texto("Bio del autor (opcional): ")
    tags_texto = pedir_texto("Tags separados por coma (opcional): ")
    estado = pedir_texto(f"Estado {ESTADOS_POST} [borrador]: ").lower() or "borrador"

    tags = [t.strip().lower() for t in tags_texto.split(",") if t.strip()]
    autor = Autor(nombre, bio)

    try:
        post = blog.crear_post(titulo, contenido, autor, tags, estado)
    except ValueError as error:
        print(f"No se pudo crear el post: {error}")
        return
    print(f"Post creado con id {post.id}. Recordá guardarlo con la opción 6.")


def validar_posts(blog):
    """Opción 5: indica qué posts son válidos y cuáles tienen errores."""
    resultados = blog.validar_posts()
    if not resultados:
        print("No hay posts para validar.")
        return
    for i, (post, errores) in enumerate(resultados, start=1):
        titulo = str(post.titulo).strip() or "(sin título)"
        if errores:
            print(f"{i}. {titulo}: INVÁLIDO")
            for error in errores:
                print(f"   - {error}")
        else:
            print(f"{i}. {titulo}: válido")


def guardar(blog):
    """Opción 6: guarda los posts en posts.json."""
    guardar_posts(blog)
