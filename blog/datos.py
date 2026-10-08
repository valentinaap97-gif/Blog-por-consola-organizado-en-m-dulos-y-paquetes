"""Datos base del blog: perfil del autor, estados, etiquetas y posts."""

perfil_autor = {
    "nombre": "Ana López",
    "email": "ana@ejemplo.com",
    "bio": "Estudiante de Python y apasionada por el desarrollo web.",
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"python", "web", "datos", "tutorial", "consola"}

posts = [
    {
        "titulo": "Aprendiendo Python",
        "contenido": "Hoy aprendí a manejar listas y diccionarios.",
        "autor": perfil_autor,
        "tags": ["python", "tutorial"],
        "estado": "publicado",
    },
    {
        "titulo": "Mi primer blog por consola",
        "contenido": "Construí un menú interactivo con input().",
        "autor": perfil_autor,
        "tags": ["consola", "python"],
        "estado": "borrador",
    },
    {
        "titulo": "Introducción al desarrollo web",
        "contenido": "Un repaso por los conceptos básicos de la web.",
        "autor": perfil_autor,
        "tags": ["web"],
        "estado": "archivado",
    },
    {
        # Post con errores a propósito, para probar la opción 4
        "titulo": "",
        "contenido": "Este post no tiene título.",
        "autor": "Ana López",
        "tags": "python",
        "estado": "pendiente",
    },
]
