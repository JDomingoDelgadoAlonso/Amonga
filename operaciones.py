from conector import ConectorMongoDB

class OperacionesDB:
    def __init__(self):
        self.cliente = ConectorMongoDB().conectarse()
        self.db = self.cliente["app_cursos_online"]
        self.usuarios = self.db["usuarios"]
        self.cursos = self.db["cursos"]
        self.reseñas= self.db["reseñas"]

    def insertar_un_registro(self):
        #inputdatos
        print("Inserción de un nuevo registro")
        nombre = input("Introduce el nombre: ")
        email = input("Introduce el email: ")
        estado = input("Introduce el estado: ")
        video = input("¿Tiene video de presentación? (si/no): ")

        #diccionario con los ibputs
        nuevo_registro = {
            "nombre": nombre,
            "email": email,
            "estado": estado,
            "presentacion_video": True if video.lower() == "si" else False
        }

        # insertamos los nuevos datos en la coleccion usuarios
        resultado = self.usuarios.insert_one(nuevo_registro)

        print(f"Registro insertado con ID: {resultado.inserted_id}")

    def insertar_varios_registros(self):
        # List para almacenar los registros a insertar
        registros = []
        
        print("Inserción de varios registros")
        
        # Continuamos pidiendo registros hasta que el usuario decida detenerse
        while True:
            print("\nIntroduce los datos del nuevo registro:")

            nombre = input("Introduce el nombre: ")
            email = input("Introduce el email: ")
            estado = input("Introduce el estado: ")
            video = input("¿Tiene video de presentación? (si/no): ")

            # Creamos el diccionario con los datos introducidos
            nuevo_registro = {
                "nombre": nombre,
                "email": email,
                "estado": estado,
                "presentacion_video": True if video.lower() == "si" else False
            }

            # Añadimos el registro a la lista de registros
            registros.append(nuevo_registro)

            # Preguntamos si el usuario quiere añadir otro registro
            continuar = input("¿Quieres añadir otro registro? (si/no): ")
            if continuar.lower() != 'si':
                break
        
        # Insertamos todos los registros a la vez en la base de datos
        if registros:
            resultado = self.usuarios.insert_many(registros)
            print(f"Se han insertado {len(resultado.inserted_ids)} registros con los siguientes IDs:")
            for id in resultado.inserted_ids:
                print(f" - {id}")
        else:
            print("No se ha insertado ningún registro.")

    def actualizar_un_registro(self):
        print("Actualización de un registro existente")

        #email que pedimos al usuario para actualizar
        email = input("Introduce el email del registro que quieres actualizar: ")

        # comprobacion
        usuario_a_actualizar = self.usuarios.find_one({"email": email})
        
        if usuario_a_actualizar:
            # muestra de datos a actualizar
            print(f"Datos actuales del usuario con email {email}:")
            print(f"Nombre: {usuario_a_actualizar['nombre']}")
            print(f"Estado: {usuario_a_actualizar['estado']}")
            print(f"Video de presentación: {'Sí' if usuario_a_actualizar['presentacion_video'] else 'No'}")

            # Pedimos los nuevos datos que se van a actualizar
            estado_nuevo = input(f"Introduce el nuevo estado (actual: {usuario_a_actualizar['estado']}): ")
            video_nuevo = input(f"¿Tiene video de presentación? (actual: {'Sí' if usuario_a_actualizar['presentacion_video'] else 'No'}) (si/no): ")

            # almacenamos los cambios
            actualizacion = {
                "estado": estado_nuevo if estado_nuevo else usuario_a_actualizar['estado'],
                "presentacion_video": True if video_nuevo.lower() == "si" else False if video_nuevo else usuario_a_actualizar['presentacion_video']
            }

            # Ejecutamos la actualización en la base de datos
            resultado = self.usuarios.update_one({"email": email}, {"$set": actualizacion})

            # Comprobamos si se actualizó el registro
            if resultado.modified_count > 0:
                print(f"El registro con email {email} ha sido actualizado.")
            else:
                print(f"No se realizaron cambios en el registro con email {email}.")
        else:
            print(f"No se encontró un registro con el email {email}.")

    def actualizar_varios_registros(self):
        print("Actualización de varios registros por email")

        # Pedimos los correos electrónicos de los usuarios que queremos actualizar
        emails = input("Introduce los correos electrónicos de los usuarios a actualizar (separados por coma): ")
        emails_lista = [email.strip() for email in emails.split(",")]

        # Filtramos los usuarios por los correos electrónicos proporcionados
        registros_a_actualizar = self.usuarios.find({"email": {"$in": emails_lista}})
        
        # Usamos len() para contar el número de registros
        registros_a_actualizar_lista = list(registros_a_actualizar)  # Convertimos el cursor en una lista
        if len(registros_a_actualizar_lista) > 0:
            print(f"Se encontraron {len(registros_a_actualizar_lista)} registros con los emails proporcionados.")

            # Pedimos los nuevos valores para actualizar
            estado_nuevo = input("Introduce el nuevo estado para los usuarios: ")
            video_nuevo = input("¿Deseas cambiar si tienen video de presentación? (si/no): ")

            # Creamos el diccionario con las actualizaciones
            actualizacion = {
                "estado": estado_nuevo if estado_nuevo else None,
                "presentacion_video": True if video_nuevo.lower() == "si" else False
            }

            # Ejecutamos la actualización en la base de datos
            resultado = self.usuarios.update_many(
                {"email": {"$in": emails_lista}}, 
                {"$set": actualizacion}
            )

            # Comprobamos si se actualizaron registros
            if resultado.modified_count > 0:
                print(f"{resultado.modified_count} registros han sido actualizados.")
            else:
                print("No se realizaron cambios en los registros.")
        else:
            print(f"No se encontraron registros con los emails proporcionados.")

    def obtener_registros_por_estado(self):
        print("Obteniendo registros por estado")

        # Pedimos el estado para filtrar
        estado = input("Introduce el estado para filtrar (por ejemplo, activo, inactivo): ")

        # Creamos el filtro por estado
        filtro = {"estado": estado}

        # Obtenemos los registros que coinciden con el filtro
        registros = self.usuarios.find(filtro)

        # Mostramos los registros encontrados
        registros_encontrados = list(registros)  # Convertimos el cursor en una lista
        if registros_encontrados:
            print(f"Se encontraron {len(registros_encontrados)} registros con el estado '{estado}':")
            for registro in registros_encontrados:
                print(registro)
        else:
            print(f"No se encontraron registros con el estado '{estado}'.")

    def obtener_por_filtro_estado_y_no_video(self):
        print("Obteniendo registros con estado 'disponible' y sin video de presentación")

        # Filtro para usuarios con estado "disponible" y sin video de presentación
        filtro = {
            "estado": "disponible",
            "presentacion_video": False
        }

        # Obtenemos los registros que coinciden con el filtro
        registros = self.usuarios.find(filtro)

        # Mostramos los registros encontrados
        registros_encontrados = list(registros)  # Convertimos el cursor en una lista
        if registros_encontrados:
            print(f"Se encontraron {len(registros_encontrados)} registros con estado 'disponible' y sin video:")
            for registro in registros_encontrados:
                print(registro)
        else:
            print("No se encontraron registros que cumplan con el filtro especificado.")

    def obtener_registros_sin_null_en_video(self):
        print("Obteniendo registros donde 'presentacion_video' no es null")

        # Filtro para obtener registros donde 'presentacion_video' no es null
        filtro = {
            "presentacion_video": {"$ne": None}  # Filtramos registros donde 'presentacion_video' no sea null
        }

        # Obtenemos los registros que cumplen con el filtro
        registros = self.usuarios.find(filtro)

        # Mostramos los registros encontrados
        registros_encontrados = list(registros)  # Convertimos el cursor en una lista
        if registros_encontrados:
            print(f"Se encontraron {len(registros_encontrados)} registros donde 'presentacion_video' no es null:")
            for registro in registros_encontrados:
                print(registro)
        else:
            print("No se encontraron registros donde 'presentacion_video' no sea null.")

    def obtener_registros_sin_atributo(self):
        print("Obteniendo registros que no tienen el atributo 'id_usuario'")

        # Filtro para obtener registros donde 'id_usuario' no existe
        filtro = {
            "id_usuario": {"$exists": False}
        }

        # Obtenemos los registros que cumplen con el filtro
        registros = self.usuarios.find(filtro)

        # Mostramos los registros encontrados
        registros_encontrados = list(registros)  # Convertimos el cursor en una lista
        if registros_encontrados:
            print(f"Se encontraron {len(registros_encontrados)} registros que no tienen el atributo 'id_usuario':")
            for registro in registros_encontrados:
                print(registro)
        else:
            print("No se encontraron registros que no tengan el atributo 'id_usuario'.")

    def obtener_por_lista_de_valores(self):
        print("Obteniendo registros que tienen el valor 'estado' en una lista de valores específicos")

        # Pedimos al usuario los estados que quiere filtrar
        estados_input = input("Introduce los estados que quieres filtrar, separados por comas (por ejemplo: 'disponible,en proceso'): ")

        # Convertimos la entrada del usuario en una lista
        estados_posibles = [estado.strip() for estado in estados_input.split(",")]

        # Filtro para obtener registros donde el campo 'estado' coincida con los valores en la lista
        filtro = {
            "estado": {"$in": estados_posibles}
        }

        # Obtenemos los registros que cumplen con el filtro
        registros = self.usuarios.find(filtro)

        # Mostramos los registros encontrados
        registros_encontrados = list(registros)  # Convertimos el cursor en una lista
        if registros_encontrados:
            print(f"Se encontraron {len(registros_encontrados)} registros con 'estado' en la lista {estados_posibles}:")
            for registro in registros_encontrados:
                print(registro)
        else:
            print("No se encontraron registros con los estados especificados.")

    def obtener_usuarios_con_mas_de_x_cursos(self):
        #input num de cursos para mostrar
        cantidad_minima = int(input("Introduce el número mínimo de cursos: "))
        
        # Buscar los usuarios que tienen más de esa cantidad de cursos
        pipeline = [
            # Agrupamos los cursos por el email del propietario (email del usuario)
            {"$group": {
                "_id": "$email",  # Agrupamos por el email del usuario
                "cantidad_cursos": {"$sum": 1}  # Sumamos la cantidad de cursos de cada usuario
            }},
            # Filtramos aquellos que tienen más que la cantidad mínima de cursos
            {"$match": {
                "cantidad_cursos": {"$gt": cantidad_minima}
            }}
        ]
        
        usuarios_con_mas_cursos = list(self.cursos.aggregate(pipeline))
        
        if usuarios_con_mas_cursos:
            for usuario in usuarios_con_mas_cursos:
                print(f"\nUsuario: {usuario['_id']} tiene {usuario['cantidad_cursos']} cursos.")
                print("Cursos que puede ofrecer:")
                
                #buscamos los cursos con elemail como filtro, está en ambas colecciones
                cursos_usuario = self.cursos.find({"email": usuario["_id"]})
                
                for curso in cursos_usuario:
                    print(f"- {curso['titulo']}")
        else:
            print("No se encontraron usuarios con más de esa cantidad de cursos.")


    def obtener_usuarios_cursando_o_con_cursos(self):
        # Condición 1: usuarios con estado "disponible"
        condicion_1 = {"estado": "cursando"}
        
        # Condición 2: usuarios que tienen al menos un curso asociado (su email debe estar presente en la colección cursos)
        # Buscamos usuarios cuyo email esté presente en la colección de cursos
        emails_con_cursos = self.cursos.distinct("email")
        condicion_2 = {"email": {"$in": emails_con_cursos}}

        # Usamos $or para combinar ambas condiciones
        usuarios_con_condicion = list(self.usuarios.find({"$or": [condicion_1, condicion_2]}))

        # Mostrar los resultados
        if usuarios_con_condicion:
            for usuario in usuarios_con_condicion:
                print(f"\nUsuario: {usuario['nombre']}, Estado: {usuario['estado']}")
                print(f"Email: {usuario['email']}")
                print(f"Video de presentación: {'Sí' if usuario['presentacion_video'] else 'No'}")

                # Si tiene cursos asociados, mostrar los cursos
                cursos_usuario = list(self.cursos.find({"email": usuario["email"]}))
                if cursos_usuario:
                    print("Cursos asignados:")
                    for curso in cursos_usuario:
                        print(f"- {curso['titulo']}")
        else:
            print("No se encontraron usuarios que cumplan con las condiciones(estado cursando o con cursos en la plataforma).")

    def obtener_usuarios_no_disponibles(self):
        # Buscar usuarios cuyo estado NO sea "disponible"
        usuarios_no_disponibles = list(self.usuarios.find({"estado": {"$ne": "disponible"}}))

        # Mostrar los resultados
        if usuarios_no_disponibles:
            for usuario in usuarios_no_disponibles:
                print(f"\nUsuario: {usuario['nombre']}, Estado: {usuario['estado']}")
                print(f"Email: {usuario['email']}")
                print(f"Video de presentación: {'Sí' if usuario['presentacion_video'] else 'No'}")
        else:
            print("No se encontraron usuarios que no estén disponibles.")

    def eliminar_resenia(self):
        # Pedimos el email del usuario
        email_usuario = input("Introduce el email del usuario cuyas reseñas quieres eliminar: ").strip()

        # Verificar que el correo no está vacío
        if not email_usuario:
            print("El email no puede estar vacío.")
            return

        # Buscar las reseñas del usuario con el email proporcionado
        print(f"Buscando reseñas para el usuario con email: '{email_usuario}'")  # Depuración
        resenias_usuario = list(self.reseñas.find({"email": email_usuario}))

        print(f"Se encontraron {len(resenias_usuario)} reseñas para el email '{email_usuario}'")  # Depuración

        if resenias_usuario:
            print(f"\nReseñas encontradas para el usuario {email_usuario}:")
            # Mostrar las reseñas numeradas
            for index, resenia in enumerate(resenias_usuario, 1):
                print(f"{index}. Curso ID: {resenia['id_curso']} | Comentario: {resenia['comentario']} | Calificación: {resenia['calificacion']}")

            # Pedir al usuario que elija la reseña a eliminar
            try:
                opcion = int(input("\nIntroduce el número de la reseña que quieres eliminar: "))
                if 1 <= opcion <= len(resenias_usuario):
                    resenia_a_eliminar = resenias_usuario[opcion - 1]
                    id_resenia = resenia_a_eliminar['_id']

                    # Eliminar la reseña seleccionada
                    self.reseñas.delete_one({"_id": id_resenia})

                    print(f"Reseña eliminada: {resenia_a_eliminar['comentario']} del curso {resenia_a_eliminar['id_curso']}")
                else:
                    print("Opción no válida. Por favor, elige un número de la lista.")
            except ValueError:
                print("Por favor, introduce un número válido.")
        else:
            print(f"No se encontraron reseñas para el usuario con email '{email_usuario}'. Revise el email y asegúrese de que tiene reseñas.")

    def eliminar_todas_resenas(self):
        # Solicitar el email del usuario
        email_usuario = input("Introduce el email del usuario cuyas reseñas quieres eliminar: ").strip()

        # Verificar que el email no esté vacío
        if not email_usuario:
            print("El email no puede estar vacío.")
            return

        # Buscar las reseñas asociadas a ese email
        reseñas_usuario = list(self.reseñas.find({"email": email_usuario}))

        if reseñas_usuario:
            # Mostrar las reseñas asociadas a ese email
            print(f"\nReseñas encontradas para el usuario {email_usuario}:")
            for index, resenia in enumerate(reseñas_usuario, 1):
                print(f"{index}. Curso ID: {resenia['id_curso']} | Comentario: {resenia['comentario']} | Calificación: {resenia['calificacion']}")

            # Preguntar al usuario si desea eliminar todas las reseñas
            confirmacion = input("\n¿Seguro que quieres eliminar todas las reseñas para este email? (sí/no): ").strip().lower()

            if confirmacion == 'sí' or confirmacion == 'si':
                # Eliminar todas las reseñas para ese email
                self.reseñas.delete_many({"email": email_usuario})
                print(f"\nTodas las reseñas asociadas al email '{email_usuario}' han sido eliminadas.")
            else:
                print("Operación cancelada. No se eliminaron reseñas.")
        else:
            print(f"No se encontraron reseñas para el usuario con email '{email_usuario}'.")
