# Blog por consola (modular)

Sistema de blog por consola organizado en módulos y paquetes. Permite ver posts,
buscar por título, filtrar por tag y validar la estructura de los posts.

## Cómo ejecutarlo

Desde la carpeta raíz del proyecto (donde está `main.py`):

```bash
python main.py
```

Requiere Python 3. No necesita instalar librerías externas.

## Estructura del proyecto

```
blog_consola/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

- `main.py`: archivo principal. Importa las piezas del paquete `blog`, muestra el menú y llama a la función correspondiente según la opción elegida.
- `blog/__init__.py`: permite que Python reconozca `blog/` como paquete.
- `blog/datos.py`: datos base (`perfil_autor`, `estados_post`, `etiquetas_blog`, `posts`). El autor es un diccionario anidado dentro de cada post.
- `blog/menu.py`: muestra el menú y maneja el `input()`.
- `blog/operaciones.py`: `listar_posts`, `buscar_por_titulo` y `filtrar_por_tag` (ignoran mayúsculas con `.lower()`).
- `blog/validaciones.py`: `validar_post`, que revisa claves, título, contenido, autor, tags y estado.

## Menú

1. Ver todos los posts (título, autor y estado)
2. Buscar por título (total o parcial, sin distinguir mayúsculas)
3. Filtrar por tag (sin distinguir mayúsculas)
4. Validar posts (indica cuáles son válidos y cuáles tienen errores)
5. Salir

Nota: el último post de `datos.py` tiene errores a propósito para poder probar la opción 4.
