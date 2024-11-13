from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaDB = cliente["libreria"]
librosColeccion = libreriaDB["libros"]


#Obtenermos varios libros
libros = librosColeccion.find()
for l in libros:
    print(l)
print("\n")
#Obtenemos libros pero no el campo id
libros2 = librosColeccion.find({},{ "_id": 0, "titulo": 1, "paginas": 1, "precio":1,"disponible":1 })
for l in libros2:
    print(l)
    libros3 = librosColeccion.find({},{"paginas": 0,"precio":0})
print("\n")
for l in libros3:
    print(l)

#Si mezclamos 1 y 0, sólo podemos poner 0 en un campo
