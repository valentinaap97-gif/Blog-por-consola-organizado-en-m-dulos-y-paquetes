"""Datos base y persistencia del blog (carga y guardado en posts.json)."""

import json
from pathlib import Path

from blog.modelos import Blog, Post

# posts.json queda en la carpeta raíz del proyecto, junto a main.py
RUTA_POSTS = Path(__file__).resolve().parent.parent / "posts.json"

etiquetas_blog = {"python", "web", "datos", "tutorial", "consola"}


def cargar_posts(ruta=RUTA_POSTS):
    """Lee posts.json y devuelve un Blog con objetos Post.

    Si el archivo no existe, está vacío o es inválido, avisa y devuelve un Blog vacío.
    Los posts incompletos se omiten con un aviso.
    """
    blog = Blog()
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"Aviso: no existe {Path(ruta).name}. Se empieza con un blog vacío.")
        return blog
    except OSError as error:
        print(f"Error: no se pudo leer {Path(ruta).name}: {error}")
        return blog

    if not contenido.strip():
        print(f"Aviso: {Path(ruta).name} está vacío. Se empieza con un blog vacío.")
        return blog

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError as error:
        print(f"Error: {Path(ruta).name} tiene contenido inválido ({error}). Se empieza con un blog vacío.")
        return blog

    if not isinstance(datos, list):
        print(f"Error: {Path(ruta).name} debe contener una lista de posts. Se empieza con un blog vacío.")
        return blog

    for i, item in enumerate(datos, start=1):
        try:
            blog.agregar_post(Post.from_dict(item))
        except (ValueError, TypeError) as error:
            print(f"Aviso: se omitió el post #{i} del archivo: {error}")

    blog.modificado = False
    return blog


def guardar_posts(blog, ruta=RUTA_POSTS):
    """Guarda los posts del blog en posts.json. Devuelve True si se guardó bien."""
    try:
        # Primero se convierte todo a texto: si algo falla, el archivo anterior no se pisa
        texto = json.dumps(blog.to_list(), ensure_ascii=False, indent=4)
    except TypeError as error:
        print(f"Error: hay datos que no se pueden convertir a JSON ({error}).")
        return False

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except OSError as error:
        print(f"Error: no se pudo guardar {Path(ruta).name}: {error}")
        return False

    blog.modificado = False
    print(f"Se guardaron {len(blog.posts)} posts en {Path(ruta).name}.")
    return True
