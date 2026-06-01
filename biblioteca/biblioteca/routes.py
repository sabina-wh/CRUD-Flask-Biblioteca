# routes.py
from .views import inicio, libros_list, libros_view, libros_modificar, libros_eliminar
from .views import autores_list, autores_view, autores_modificar, autores_eliminar
from .views import editores_list, editores_view, editores_modificar, editores_eliminar

# app.add_url_rule(
#     '/libros',          # URL
#     'libros_listar',    # endpoint (nombre interno)
#     libros_listar       # función vista
# )

def registrar_rutas(app):
    
    app.add_url_rule('/', 'inicio', inicio)

    # Rutas Libros
    app.add_url_rule('/libros', 'libros_listar', libros_list)
    app.add_url_rule('/libros/nuevo', 'libros_crear', libros_view, methods=['GET', 'POST'])
    app.add_url_rule('/libros/editar/<int:id_libro>', 'libros_editar', libros_modificar, methods=['GET', 'POST'])
    app.add_url_rule('/libros/eliminar/<int:id_libro>', 'libros_eliminar', libros_eliminar, methods=['GET', 'POST'])

    # Rutas Autores
    app.add_url_rule('/autores', 'autores_listar', autores_list)
    app.add_url_rule('/autores/nuevo', 'autores_crear', autores_view, methods=['GET', 'POST'])
    app.add_url_rule('/autores/editar/<int:id_autor>', 'autores_editar', autores_modificar, methods=['GET', 'POST'])
    app.add_url_rule('/autores/eliminar/<int:id_autor>', 'autores_eliminar', autores_eliminar, methods=['GET', 'POST'])

    # Rutas Editores
    app.add_url_rule('/editor', 'editor_listar', editores_list)
    app.add_url_rule('/editor/nuevo', 'editor_crear', editores_view, methods=['GET', 'POST'])
    app.add_url_rule('/editor/editar/<int:id_editor>', 'editor_editar', editores_modificar, methods=['GET', 'POST'])
    app.add_url_rule('/editor/eliminar/<int:id_editor>', 'editor_eliminar', editores_eliminar, methods=['GET', 'POST'])
