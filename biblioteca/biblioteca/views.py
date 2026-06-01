import os

from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from flask import current_app

from biblioteca.models import db, Editor, Libro, Autor
from biblioteca.forms import AutorForm, EditorForm, LibroForm
# Create your views here.

def inicio():
    return render_template('index.html')


#VISTAS BASADAS EN FUNCIONES
def editores_list():
    editores = Editor.query.order_by(Editor.id).all()
    return render_template('editor_mostrar.html', editores=editores)

def editores_view():
        form = EditorForm()# Creamos el formulario
        
        if form.validate_on_submit():# POST + validación

            editor = Editor(# Creamos el objeto Editor
                nombre=form.nombre.data,
                domicilio=form.domicilio.data,
                ciudad=form.ciudad.data,
                estado=form.estado.data,
                pais=form.pais.data,
                website=form.website.data
            )

            #form.save() → en Flask no existe: 
            # hay que crear el objeto y hacer 
            # db.session.add(obj) + db.session.commit().

            db.session.add(editor)
            db.session.commit()

            #flash('mensaje', 'categoria').
            flash('El Editor ha sido agregado.', 'success')
            return redirect(url_for('editor_listar'))
        
        # GET o formulario inválido        
        return render_template('editor_form.html', form=form)

def editores_modificar(id_editor):
    #realizamos la busqueda
    editor = Editor.query.get_or_404(id_editor)
    
    form = EditorForm(obj=editor)
    
    if form.validate_on_submit():
            #copia datos del form al objeto
            form.populate_obj(editor)

            #En Flask NO se "guarda el formulario", se actualiza el objeto manualmente
            db.session.commit()#guardamos en DB
            
            flash('Tus modificacciones han sido actualizadas.', 'success')
            return redirect(url_for('editor_listar'))

    return render_template('editor_form.html', form=form)

def editores_eliminar(id_editor):
    editor = Editor.query.get_or_404(id_editor)

    if request.method == 'POST':
    #En Flask, eliminar NO necesita formulario, solo confirmación POST
        db.session.delete(editor)
        db.session.commit()
        flash('El Editor ha sido eliminado', 'danger')
        return redirect(url_for('editor_listar'))
    return render_template('editor_eliminar.html', editor=editor)

def libros_list():
    # obtener el parámetro de búsqueda
    q = request.args.get('q', '').strip()
    errors = []

    # Consulta base
    query = Libro.query

    # Filtrar si hay búsqueda
    if q:
        if len(q) > 20:
            errors.append('El término de búsqueda debe ser menor a 20 caracteres')
            libros = []
        else:
            libros = query.filter(Libro.titulo.ilike(f"%{q}%")).all()
    else:
        libros = query.order_by(Libro.titulo).all()

    return render_template(
        'libro_mostrar.html',
        libros=libros,
        q=q,
        errors=errors
    )

def libros_view():
    form = LibroForm()#Flask-WTF recibe request.form y request.files

    # CARGAR OPCIONES (EQUIVALENTE A DJANGO __init__)
    form.editor.choices = [
        (e.id, e.nombre) for e in Editor.query.all()
    ]

    form.autores.choices = [
        (a.id, f"{a.nombre} {a.apellidos}")
        for a in Autor.query.all()
    ]

    if form.validate_on_submit():
        # Crear objeto Libro
        libro = Libro(
            titulo=form.titulo.data,
            editor_id=form.editor.data,  # asumimos que el form devuelve el id del editor
            fecha_publicacion=form.fecha_publicacion.data
        )

        # Guardar portada si hay archivo
        if form.portada.data:
            filename = secure_filename(form.portada.data.filename)
            ruta = os.path.join(current_app.root_path, 'static', 'portadas', filename)
            form.portada.data.save(ruta)
            libro.portada = filename

        # Guardar libro primero
        db.session.add(libro)
        db.session.flush()  # opcional pero recomendado

        # Asignar autores 
        for autor_id in form.autores.data:
            autor = Autor.query.get(autor_id)
            if autor:
                libro.autores.append(autor)

        db.session.commit()

        flash('El libro ha sido agregado.', 'success')
        return redirect(url_for('libros_listar'))

    return render_template('libro_form.html', form=form)

def libros_modificar(id_libro):
    libro = Libro.query.get_or_404(id_libro)

    form = LibroForm(obj=libro)

    # CARGAR SELECTS (OBLIGATORIO EN EDITAR)
    form.editor.choices = [
        (e.id, e.nombre) for e in Editor.query.all()
    ]

    form.autores.choices = [
        (a.id, f"{a.nombre} {a.apellidos}")
        for a in Autor.query.all()
    ]

    # precargar datos 
    if request.method == "GET":
        form.autores.data = [a.id for a in libro.autores]

    if form.validate_on_submit():

        # actualizar campos 
        libro.titulo = form.titulo.data
        libro.editor_id = form.editor.data
        libro.fecha_publicacion = form.fecha_publicacion.data

        if form.portada.data:
            filename = secure_filename(form.portada.data.filename)
            ruta = os.path.join('media/portadas', filename)
            form.portada.data.save(ruta)
            libro.portada = filename

        libro.autores = Autor.query.filter(
            Autor.id.in_(form.autores.data)
        ).all()

        db.session.commit()

        flash('Tus modificaciones han sido actualizadas', 'success')
        return redirect(url_for('libros_listar'))

    return render_template('libro_form.html', form=form)

def libros_eliminar(id_libro):
    libro = Libro.query.get_or_404(id_libro) 

    if request.method == 'POST':
        db.session.delete(libro)
        db.session.commit()
        flash('El libro ha sido eliminado', 'error')  
        return redirect(url_for('libros_listar'))
    
    return render_template('libro_eliminar.html', libro=libro)

def autores_list():
    autores = Autor.query.order_by(Autor.apellidos).all()
    return render_template('autor_mostrar.html', autores=autores)

def autores_view():
    form = AutorForm()

    if form.validate_on_submit():
        
        autores = Autor(
            nombre=form.nombre.data,  
            apellidos=form.apellidos.data,
            email=form.email.data
            )
        
        db.session.add(autores)
        db.session.commit()

        flash('El autor(es) ha sido agregado.', 'success')
        return redirect(url_for('autores_list'))
    
    return render_template('autor_form.html', form=form)

def autores_modificar(id_autor):
    autor = Autor.query.get_or_404(id_autor)

    form = AutorForm(obj=autor)

    if form.validate_on_submit():
        autor.nombre = form.nombre.data
        autor.apellidos = form.apellidos.data
        autor.email = form.email.data

        db.session.commit()

        flash('Tus modificaciones han sido actualizadas', 'success')
        return redirect(url_for('autores_listar'))

    return render_template('autor_form.html',form=form)

def autores_eliminar(id_autor):
    autor = Autor.query.get_or_404(id_autor)

    if request.method == 'POST':
        db.session.delete(autor)
        db.session.commit()

        flash('El autor ha sido eliminado', 'error')
        return redirect(url_for('autores_listar'))
    
    return render_template('autor_eliminar.html', autor=autor)