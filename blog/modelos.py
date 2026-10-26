"""Modelos del blog: Autor, Post y Blog."""

from blog.validaciones import validar_post

CLAVES_POST = ("titulo", "contenido", "autor", "tags", "estado")


class Autor:
    """Persona autora de uno o más posts."""

    def __init__(self, nombre, bio="", email=""):
        self.nombre = nombre
        self.bio = bio
        self.email = email

    def to_dict(self):
        """Convierte el autor a un diccionario compatible con JSON."""
        return {"nombre": self.nombre, "email": self.email, "bio": self.bio}

    @classmethod
    def from_dict(cls, datos):
        """Crea un Autor desde un diccionario. Lanza ValueError si está incompleto."""
        if not isinstance(datos, dict):
            raise ValueError("el autor debe ser un diccionario")
        if "nombre" not in datos:
            raise ValueError("al autor le falta la clave 'nombre'")
        return cls(datos["nombre"], datos.get("bio", ""), datos.get("email", ""))

    def __str__(self):
        return str(self.nombre).strip() or "(sin nombre)"


class Post:
    """Publicación del blog. Su autor es una instancia de Autor."""

    def __init__(self, titulo, contenido, autor, tags=None, estado="borrador", id=None):
        if not isinstance(autor, Autor):
            raise TypeError("el autor de un Post debe ser una instancia de Autor")
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags if tags is not None else []
        self.estado = estado

    def coincide_titulo(self, termino):
        """True si el término está en el título (sin distinguir mayúsculas)."""
        return termino.lower() in str(self.titulo).lower()

    def tiene_tag(self, tag):
        """True si el post tiene ese tag (sin distinguir mayúsculas)."""
        return tag.lower() in [str(t).lower() for t in self.tags]

    def to_dict(self):
        """Convierte el post (y su autor) a un diccionario compatible con JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": list(self.tags),
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un Post desde un diccionario. Lanza ValueError si está incompleto."""
        if not isinstance(datos, dict):
            raise ValueError("el post debe ser un diccionario")
        faltantes = [clave for clave in CLAVES_POST if clave not in datos]
        if faltantes:
            raise ValueError("faltan las claves: " + ", ".join(faltantes))
        if not isinstance(datos["tags"], list):
            raise ValueError("'tags' debe ser una lista")
        autor = Autor.from_dict(datos["autor"])
        return cls(
            datos["titulo"],
            datos["contenido"],
            autor,
            datos["tags"],
            datos["estado"],
            datos.get("id"),
        )


class Blog:
    """Colección de posts. Centraliza la lógica principal del sistema."""

    def __init__(self, posts=None):
        self.posts = list(posts) if posts else []
        self.modificado = False  # True si hay cambios sin guardar

    def obtener_posts(self):
        """Devuelve todos los posts cargados."""
        return self.posts

    def _siguiente_id(self):
        ids = [p.id for p in self.posts if isinstance(p.id, int)]
        return max(ids, default=0) + 1

    def agregar_post(self, post):
        """Agrega un Post a la lista (le asigna un id si no tiene)."""
        if not isinstance(post, Post):
            raise TypeError("solo se pueden agregar objetos de la clase Post")
        if post.id is None:
            post.id = self._siguiente_id()
        self.posts.append(post)
        self.modificado = True

    def crear_post(self, titulo, contenido, autor, tags=None, estado="borrador"):
        """Crea un Post, lo valida y lo agrega. Lanza ValueError si los datos son inválidos."""
        post = Post(titulo, contenido, autor, tags, estado)
        errores = validar_post(post.to_dict())
        if errores:
            raise ValueError("; ".join(errores))
        self.agregar_post(post)
        return post

    def listar_posts(self, posts=None):
        """Muestra título, autor y estado. Si no se pasa una lista, muestra todos los posts."""
        if posts is None:
            posts = self.posts
        if not posts:
            print("No hay posts para mostrar.")
            return
        for i, post in enumerate(posts, start=1):
            print(f"{i}. {str(post.titulo).strip() or '(sin título)'}")
            print(f"   Autor: {post.autor}")
            print(f"   Estado: {post.estado}")

    def buscar_por_titulo(self, termino):
        """Devuelve los posts cuyo título contiene el término."""
        return [p for p in self.posts if p.coincide_titulo(termino)]

    def filtrar_por_tag(self, tag):
        """Devuelve los posts que tienen el tag indicado."""
        return [p for p in self.posts if p.tiene_tag(tag)]

    def validar_posts(self):
        """Devuelve una lista de tuplas (post, errores) para cada post."""
        return [(p, validar_post(p.to_dict())) for p in self.posts]

    def to_list(self):
        """Convierte todos los posts a una lista de diccionarios."""
        return [p.to_dict() for p in self.posts]
