from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaDB = cliente["libreria"]
librosColeccion = libreriaDB["libros"]

miquery = { "titulo": "El Principito" }
nuevosValores = { "$set": { "precio": 99.99 } }

resultado = librosColeccion.update_one(miquery, nuevosValores)
 
#miquery = { "titulo": "1984" }
#nuevosValores = { "$set": { "titulo": "Reina Roja" } }
#
#resultado = librosColeccion.update_many(miquery, nuevosValores)