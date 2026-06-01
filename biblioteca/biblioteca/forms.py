#WTF para gestionar formularios
from flask_wtf import FlaskForm
from wtforms import DateField, FileField, SelectField, SelectMultipleField, StringField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Email, Optional, URL, Length

from biblioteca.models import Editor, Libro, Autor

class EditorForm(FlaskForm):
	nombre = StringField(
        'Nombre',
        validators=[DataRequired(message="El nombre es obligatorio")],
        render_kw={"class": "form-control"}
    )
	domicilio = StringField(
        'Domicilio',
        validators=[Optional()],
        render_kw={"class": "form-control"}
    )
	ciudad = StringField(
        'Ciudad',
        validators=[Optional()],
        render_kw={"class": "form-control"}
    )
	estado = StringField(
        'Estado',
        validators=[Optional()],
        render_kw={"class": "form-control"}
    )
	pais = StringField(
        'Pais',
        validators=[Optional()],
        render_kw={"class": "form-control"}
    )
	website = StringField(
        'Sitio Web',
        validators=[Optional(), URL(message="Debe ser una URL válida")],
        render_kw={"class": "form-control"}
    )

class LibroForm(FlaskForm):

    titulo = StringField(
        'Titulo',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )

    # SELECT SIMPLE (Editor)
    editor = SelectField(
        'Editor',
        coerce=int,   # convierte string -> int
        validators=[DataRequired()],
        render_kw={"class": "form-control form-select"}
    )

    # MULTISELECT (Autores)
    autores = SelectMultipleField(
        'Autores',
        coerce=int,
        validators=[Optional()],
        render_kw={"class": "form-control js-example-basic-multiple"}
    )

    fecha_publicacion = DateField(
        'Fecha Publicación',
        format='%Y-%m-%d',
        validators=[Optional()],
        render_kw={"class": "form-control"}
    )

    portada = FileField(
        'Portada',
        validators=[
            Optional(),
            FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imágenes')
        ],
        render_kw={"class": "form-control"}
    )



class AutorForm(FlaskForm):
	nombre = StringField(
        'Nombre',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
	apellidos = StringField(
        'Apellidos',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
	email = StringField(
        'Email',
        validators=[Optional(), Email()],
        #render_kw={"class": "form-control"}
    )
