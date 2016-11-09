peliculas = {"anabel" : "Rapido y furioso",
			"carli" : "la noche del demonio",
			"joaquin" : "cars"
			}

print (peliculas["anabel"])

for nombre, peli in peliculas.items():
	print("Nombre alumno:  %s" % nombre)
	print("Nombre pelicula:  %s" % peli)


num = 24 * 10
nombre = "anabel"
utiles = ["mochila","libreta","lapiz"]
frutas = ["manazana","pera","uva"]
dia_clases = {"nombre" : nombre, "utiles" : utiles,
				"frutas" : frutas,
				"num" : num}

print (dia_clases["frutas"])