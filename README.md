# Blog por consola (POO + JSON)

Sistema de blog por consola organizado en módulos y paquetes. Ahora está modelado con
**clases y objetos** (`Autor`, `Post` y `Blog`) y guarda sus datos en un archivo
**`posts.json`**, así que los posts se conservan entre ejecuciones.

Permite ver posts, buscar por título, filtrar por tag, crear nuevos posts, validarlos
y guardarlos en JSON.

## Cómo ejecutarlo

Desde la carpeta raíz del proyecto (donde está `main.py`):

```bash
python main.py
```

Requiere Python 3. No necesita instalar librerías externas (usa solo `json` y `pathlib`).

## Estructura del proyecto

```
blog_consola/
├── main.py
├── README.md
├── posts.json
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

- `main.py`: punto de entrada (protegido con `if __name__ == "__main__":`). Carga los posts, crea la instancia de `Blog`, muestra el menú y llama a la operación elegida. Si al salir hay cambios sin guardar, los guarda automáticamente.
- `blog/__init__.py`: permite que Python reconozca `blog/` como paquete.
- `blog/modelos.py`: las clases `Autor`, `Post` y `Blog`.
- `blog/datos.py`: persistencia. `cargar_posts()` lee `posts.json` y devuelve un `Blog`; `guardar_posts()` escribe el `Blog` en `posts.json`. También conserva `etiquetas_blog`.
- `blog/menu.py`: muestra el menú y maneja el `input()`.
- `blog/operaciones.py`: una función por opción del menú. Piden datos al usuario y llaman a los métodos de la instancia de `Blog`.
- `blog/validaciones.py`: `validar_post()`, que revisa claves, título, contenido, autor, tags y estado (trabaja sobre el diccionario del post), y la tupla `ESTADOS_POST`.

## Clases principales

### `Autor`
Representa a la persona autora. Atributos: `nombre`, `bio` y `email`.
- `to_dict()`: convierte el autor a diccionario.
- `Autor.from_dict(datos)`: reconstruye un `Autor` desde un diccionario (lanza `ValueError` si falta `nombre`).

### `Post`
Representa una publicación. Atributos: `id`, `titulo`, `contenido`, `autor`, `tags` y `estado`.
El atributo `autor` **debe ser una instancia de `Autor`** (si no, lanza `TypeError`): es la composición entre ambas clases.
- `coincide_titulo(termino)` y `tiene_tag(tag)`: comparaciones sin distinguir mayúsculas.
- `to_dict()`: convierte el post (y su autor) a diccionario.
- `Post.from_dict(datos)`: reconstruye un `Post` desde un diccionario (lanza `ValueError` si está incompleto).

### `Blog`
Centraliza la lógica del sistema. Tiene el atributo `posts`, una lista de objetos `Post`.
- `obtener_posts()`, `listar_posts()`, `buscar_por_titulo()`, `filtrar_por_tag()`.
- `crear_post()`: crea un `Post`, lo valida y lo agrega (asigna un `id` automático).
- `agregar_post()`, `validar_posts()` y `to_list()` (lista de diccionarios lista para JSON).
- `modificado`: indica si hay cambios sin guardar.

## Cómo interactúan las clases con `posts.json`

**Al guardar** (opción 6, o automáticamente al salir si hay cambios):
`Blog.to_list()` → llama a `Post.to_dict()` de cada post → que llama a `Autor.to_dict()` → `json.dumps()` → se escribe `posts.json`.
Primero se convierte todo a texto y recién después se abre el archivo, así que si algo falla no se pisa el archivo anterior.

**Al cargar** (al iniciar el programa):
`posts.json` → `json.loads()` → lista de diccionarios → `Post.from_dict()` de cada uno (que usa `Autor.from_dict()`) → objetos `Post` dentro de un `Blog`.

Ejemplo de un post en `posts.json`:

```json
{
    "id": 1,
    "titulo": "Aprendiendo Python",
    "contenido": "Hoy aprendí a manejar listas y diccionarios.",
    "autor": {
        "nombre": "Ana López",
        "email": "ana@ejemplo.com",
        "bio": "Estudiante de Python y apasionada por el desarrollo web."
    },
    "tags": ["python", "tutorial"],
    "estado": "publicado"
}
```

## Menú

1. Ver todos los posts (título, autor y estado)
2. Buscar por título (total o parcial, sin distinguir mayúsculas)
3. Filtrar por tag (sin distinguir mayúsculas)
4. Crear nuevo post (título, contenido y nombre del autor son obligatorios)
5. Validar posts (indica cuáles son válidos y cuáles tienen errores)
6. Guardar posts en JSON
7. Salir (guarda antes si hay cambios sin guardar)

## Manejo de errores

El programa no se cierra inesperadamente. Avisa con un mensaje claro cuando:
- `posts.json` no existe, está vacío o tiene contenido inválido: arranca con un blog vacío.
- Un post del archivo está incompleto: se omite y se informa cuál y por qué.
- Se elige una opción incorrecta en el menú.
- Se dejan campos vacíos al crear un post.
- No se puede convertir a JSON o escribir el archivo al guardar.

## Qué cambió respecto al checkpoint anterior

- Antes los posts y el autor eran **diccionarios** y las operaciones eran funciones sueltas que recibían una lista. Ahora son **objetos** (`Post`, `Autor`) y las operaciones son **métodos de `Blog`**.
- Nuevo archivo `blog/modelos.py` con las tres clases.
- `blog/datos.py` dejó de tener los posts escritos en el código: ahora **carga y guarda en `posts.json`**.
- `blog/operaciones.py` pasó de implementar la lógica a conectar el menú con la instancia de `Blog`.
- `blog/validaciones.py` ahora define `ESTADOS_POST` (antes lo importaba de `datos.py`) para evitar imports circulares.
- Nuevas opciones de menú: crear post y guardar en JSON.

Nota: el último post de `posts.json` tiene errores a propósito (título vacío y estado inválido) para poder probar la opción 5.
