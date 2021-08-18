from pprint import pprint

# Incluyo el script pprint de la libreria pprint
# nos permite printear cosas por consola de forma mas ordenada

# Creo una lista de titulos sacados a mano del csv y se la asigno a una variable titulos
titulos = ["Rick y Morty: Temporada 3: Descanso y Ricklajación", "Rick y Morty: Temporada 4: Un tren de antologías", "Community: Temporada 2: Accounting for Lawyers", "Community: Temporada 2: Conspiracy Theories and Interior Design", "Community: Temporada 2: Cooperative Calligraphy", "Community: Temporada 2: Celebrity Pharmacology", "Community: Temporada 3: Biología básica", "Community: Temporada 4: Introducción avanzada a la finalidad", "Community: Temporada 4: Orígenes heroicos", "Rick y Morty: Temporada 4: Aprovechando el mortymento: Vive, muere, Rickpeat","Marvel - Daredevil: Temporada 2: La oscuridad al final del túnel", "Marvel - Daredevil: Temporada 2: .380"]

# La muestro por consola
pprint(titulos)

# Instancio una variable contador en 0
cont = 0

# Itero por cada titulo de mi lista titulos
for titulo in titulos:
	# Si la serie "Community" esta contenida en este titulo
	if "Community" in titulo:
		# Incremento mi contador en 1 (El operador ++ no existe en python)
		cont += 1

# Muestro el resultado
print(cont)


