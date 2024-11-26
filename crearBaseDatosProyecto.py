from conector import ConectorMongoDB

class CrearBaseDatosProyecto:

    def __init__(self):
        self.cliente = ConectorMongoDB().conectarse()
        self.db = self.cliente["app_cursos_online"]

    def crear_colecciones(self):
        # Crear colección 'usuarios'
        usuarios = [
            {"id_usuario": "1", "nombre": "Juan Pérez", "email": "juanperez@gmail.com", "estado": "activo", "presentacion_video": None},
            {"id_usuario": "2", "nombre": "María López", "email": "marialopez@gmail.com", "estado": "inactivo", "presentacion_video": "https://video.maria.com"},
            {"id_usuario": "3", "nombre": "Carlos Gómez", "email": "carlosgomez@gmail.com", "estado": "activo", "presentacion_video": None},
        ]
        self.db["usuarios"].insert_many(usuarios)

        # Crear colección 'cursos'
        cursos = [
            {"id_curso": "101", "titulo": "Curso de Python", "descripcion": "Aprende Python desde cero",
             "fecha_publicacion": "2024-01-01", "fecha_disponibilidad": "2024-02-01", "fecha_finalizacion": "2024-06-01",
             "nombre_propietario": "Juan Pérez", "disponible": True, "idiomas": ["Español"], "modalidad": "Online",
             "cantidad_intercambios": 15, "cantidad_likes": 150, "presentacion_video_curso": None},
            {"id_curso": "102", "titulo": "Curso de Machine Learning", "descripcion": "Introducción al ML",
             "fecha_publicacion": "2024-03-01", "fecha_disponibilidad": "2024-04-01", "fecha_finalizacion": "2024-08-01",
             "nombre_propietario": "Carlos Gómez", "disponible": True, "idiomas": ["Inglés", "Español"], "modalidad": "Presencial",
             "cantidad_intercambios": 10, "cantidad_likes": 200, "presentacion_video_curso": "https://video.ml.com"},
        ]
        self.db["cursos"].insert_many(cursos)

        # Crear colección 'reseñas'
        resenas = [
            {"id_resena": "201", "id_curso": "101", "id_usuario": "2", "comentario": "Excelente curso", "calificacion": 5},
            {"id_resena": "202", "id_curso": "101", "id_usuario": "3", "comentario": "Muy bueno pero complicado", "calificacion": 4},
            {"id_resena": "203", "id_curso": "102", "id_usuario": "1", "comentario": "Interesante contenido", "calificacion": 5},
        ]
        self.db["reseñas"].insert_many(resenas)

        print("Base de datos y colecciones creadas con éxito.")

# Ejecutar la creación de la base de datos
if __name__ == "__main__":
    creador = CrearBaseDatosProyecto()
    creador.crear_colecciones()
