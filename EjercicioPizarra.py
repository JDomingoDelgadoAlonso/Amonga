from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaDB = cliente["libreria"]
librosColeccion = libreriaDB["libros"]

#Libros en el que el número de páginas sea 1072
miquery = { "paginas": 1072 }
libros = librosColeccion.find(miquery,{ "_id": 0})
print("Libros en el que el número de páginas sea 1072")
for l in libros:
    print(l) 


#Libros con precio mayor o igual a 5 y el título empiece por 1
miquery2 = ({ "$and" : [
                                                     { "titulo" : { "$regex": "^1" }},
                                                     { "precio" : { "$gte":5} }
                                                   ]
                                           }
                                           )

libros2 = librosColeccion.find(miquery2,{ "_id": 0})
print("\n")
print("Libros con precio mayor o igual a 5 y el título empiece por 1")
for l in libros2:
    print(l) 


#Libros que no tengan más de 600 páginas y cuestan más e 30 euros
#miquery = { "paginas" > 600 and "precio"> 30 }
miquery3 = ({ "$and" : [
                                                     { "paginas" : {"$lt": 600 }},
                                                     { "precio" : { "$lt":30} }
                                                   ]
                                           }
                                           )

libros3= librosColeccion.find(miquery3,{ "_id": 0}).sort("titulo", -1)
print("\n")
print("Libros que no tengan más de 600 páginas y cuestan más e 30 euros")
for l in libros3:
    print(l)