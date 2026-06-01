from . import db
#creamos el objeto una instancia de SQLAlchemy()
#objeto global de la DB



#Relacion de modelos
libro_autor = db.Table(
    'libro_autor',  # nombre de la tabla en la base de datos
    db.Column('libro_id', db.Integer, db.ForeignKey('libro.id'), primary_key=True),
    db.Column('autor_id', db.Integer, db.ForeignKey('autor.id'), primary_key=True)
)

# Create your models here.
class Editor(db.Model):
    __tablename__ = 'editor'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30),nullable=False)
    domicilio = db.Column(db.String(50))
    ciudad = db.Column(db.String(60))
    estado = db.Column(db.String(30))
    pais = db.Column(db.String(50))
    website = db.Column(db.String(2048))

    libros = db.relationship(
        'Libro',
        back_populates='editor'
    )

    def __repr__(self):
        return self.nombre

class Autor(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apellidos = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=True)

    libros = db.relationship(
        'Libro',
        secondary=libro_autor,
        back_populates='autores'
    )

    def __repr__(self):
        return f"{self.nombre} {self.apellidos}"

class Libro(db.Model):
    #Definir el nombre de la tabla (opcional)
    __tablename__ = 'libro'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100),nullable=False)

    autores = db.relationship(
        'Autor',
        secondary=libro_autor,
        back_populates='libros'
    )

    editor_id = db.Column(db.Integer, db.ForeignKey('editor.id'),nullable=False)
    editor = db.relationship('Editor', back_populates='libros')

    
    fecha_publicacion = db.Column(db.Date, nullable=True)
    portada = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return self.titulo