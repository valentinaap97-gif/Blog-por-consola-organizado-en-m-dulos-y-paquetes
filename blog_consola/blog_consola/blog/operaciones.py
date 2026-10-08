"""Operaciones del blog: listado, búsqueda y filtrado."""


def _nombre_autor(post):
    """Devuelve el nombre del autor, o un texto aclaratorio si el dato es inválido."""
    autor = post.get("autor")
    if isinstance(autor, dict):
        return autor.get("nombre") or "(sin nombre)"
    return "(autor inválido)"


def listar_posts(lista):
    """Muestra título, autor y estado de cada post."""
    if not lista:
        print("No hay posts para mostrar.")
        return
    for i, post in enumerate(lista, start=1):
        print(f"{i}. {post.get('titulo') or '(sin título)'}")
        print(f"   Autor: {_nombre_autor(post)}")
        print(f"   Estado: {post.get('estado', '(sin estado)')}")


def buscar_por_titulo(lista, termino):
    """Devuelve los posts cuyo título contiene el término (sin distinguir mayúsculas)."""
    termino = termino.lower()
    return [p for p in lista if termino in str(p.get("titulo", "")).lower()]


def filtrar_por_tag(lista, tag):
    """Devuelve los posts que tienen el tag indicado (sin distinguir mayúsculas)."""
    tag = tag.lower()
    resultado = []
    for p in lista:
        tags = p.get("tags")
        if isinstance(tags, list) and tag in [t.lower() for t in tags]:
            resultado.append(p)
    return resultado
