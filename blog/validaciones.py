"""Reglas de validación de los posts.

Trabajan sobre la versión en diccionario de un post (el resultado de
Post.to_dict()), así que no dependen de las clases y se evitan imports circulares.
"""

ESTADOS_POST = ("borrador", "publicado", "archivado")

CLAVES_REQUERIDAS = ("titulo", "contenido", "autor", "tags", "estado")


def validar_post(post):
    """Valida un post (en forma de diccionario). Devuelve una lista de errores (vacía si es válido)."""
    errores = []

    if not isinstance(post, dict):
        return ["el post no es un diccionario"]

    for clave in CLAVES_REQUERIDAS:
        if clave not in post:
            errores.append(f"falta la clave '{clave}'")

    if "titulo" in post and not str(post["titulo"]).strip():
        errores.append("el título está vacío")

    if "contenido" in post and not str(post["contenido"]).strip():
        errores.append("el contenido está vacío")

    if "autor" in post:
        autor = post["autor"]
        if not isinstance(autor, dict):
            errores.append("el autor debe ser un diccionario")
        elif not str(autor.get("nombre", "")).strip():
            errores.append("el autor no tiene nombre")

    if "tags" in post and not isinstance(post["tags"], list):
        errores.append("los tags deben estar guardados en una lista")

    if "estado" in post and post["estado"] not in ESTADOS_POST:
        errores.append(f"estado inválido: '{post['estado']}'")

    return errores
