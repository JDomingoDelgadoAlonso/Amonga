from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaDB = cliente["libreria"]
librosColeccion = libreriaDB["libros"]

miquery = { "precio": 19.99 }
libros = librosColeccion.find(miquery) #-> Busca los que tienen precio igual a 19.99
for l in libros:
    print(l) 

print("\n")
miquery2 = { "precio":  { "$gt": 19 } }
libros2 = librosColeccion.find(miquery2) #-> > Busca los que tienen el precio mayor que 19 
for l in libros2:
    print(l)

print("\n")
miquery3 = { "titulo":  { "$regex": "^D" } }
libros3 = librosColeccion.find(miquery3) #-> Busca a toso los que tengan un título que empieza por D
for l in libros3:
    print(l)