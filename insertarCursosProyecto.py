    def insertar_datos(self):
            # Datos para la colección de Cursos
            cursos = [
                {
                    "id_curso": "101",
                    "titulo": "Curso de Python",
                    "descripcion": "Aprende Python desde cero",
                    "fecha_publicacion": "2024-01-01",
                    "fecha_disponibilidad": "2024-02-01",
                    "fecha_finalizacion": "2024-06-01",
                    "disponible": True,
                    "idiomas": ["Español"],
                    "modalidad": "Online",
                    "cantidad_intercambios": 15,
                    "cantidad_likes": 150,
                    "presentacion_video_curso": None,
                    "email": "domi@gmail.com"
                },
                {
                    "id_curso": "102",
                    "titulo": "Curso de Machine Learning",
                    "descripcion": "Introducción al ML",
                    "fecha_publicacion": "2024-03-01",
                    "fecha_disponibilidad": "2024-04-01",
                    "fecha_finalizacion": "2024-08-01",
                    "disponible": True,
                    "idiomas": ["Español", "Inglés"],
                    "modalidad": "Presencial",
                    "cantidad_intercambios": 10,
                    "cantidad_likes": 200,
                    "presentacion_video_curso": "https://video.ml.com",
                    "email": "domi@gmail.com"
                },
                {
                    "id_curso": "103",
                    "titulo": "Curso de Desarrollo Web",
                    "descripcion": "Fundamentos de HTML, CSS y JavaScript",
                    "fecha_publicacion": "2024-02-01",
                    "fecha_disponibilidad": "2024-03-01",
                    "fecha_finalizacion": "2024-07-01",
                    "disponible": True,
                    "idiomas": ["Español", "Inglés"],
                    "modalidad": "Online",
                    "cantidad_intercambios": 30,
                    "cantidad_likes": 300,
                    "presentacion_video_curso": None,
                    "email": "paco@gmail.com"
                },
                {
                    "id_curso": "104",
                    "titulo": "Curso de React",
                    "descripcion": "Aprende a desarrollar interfaces con React",
                    "fecha_publicacion": "2024-03-15",
                    "fecha_disponibilidad": "2024-04-01",
                    "fecha_finalizacion": "2024-09-01",
                    "disponible": True,
                    "idiomas": ["Inglés"],
                    "modalidad": "Online",
                    "cantidad_intercambios": 25,
                    "cantidad_likes": 250,
                    "presentacion_video_curso": "https://video.react.com",
                    "email": "fran@gmail.com"
                }
            ]

            # Datos para la colección de Reseñas
            reseñas = [
                {
                    "id_resena": "201",
                    "id_curso": "101",
                    "comentario": "Excelente curso, aprendí mucho y los ejemplos fueron muy útiles.",
                    "calificacion": 5,
                    "email": "domi@gmail.com"
                },
                {
                    "id_resena": "202",
                    "id_curso": "101",
                    "comentario": "Muy bueno pero complicado para principiantes.",
                    "calificacion": 4,
                    "email": "paco@gmail.com"
                },
                {
                    "id_resena": "203",
                    "id_curso": "102",
                    "comentario": "Interesante contenido, aunque creo que podría profundizar más en algunos temas.",
                    "calificacion": 5,
                    "email": "fran@gmail.com"
                },
                {
                    "id_resena": "204",
                    "id_curso": "103",
                    "comentario": "Gran curso, los temas se explican de manera clara y sencilla.",
                    "calificacion": 5,
                    "email": "paco@gmail.com"
                },
                {
                    "id_resena": "205",
                    "id_curso": "104",
                    "comentario": "Excelente curso para aprender React desde cero. El material es muy completo.",
                    "calificacion": 5,
                    "email": "fran@gmail.com"
                }
            ]

            # Insertar los nuevos documentos
            self.cursos.insert_many(cursos)
            self.reseñas.insert_many(reseñas)

            print("Cursos y reseñas insertados correctamente.")
