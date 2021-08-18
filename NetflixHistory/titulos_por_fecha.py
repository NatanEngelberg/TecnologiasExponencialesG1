import csv
from pprint import pprint

# incluyo la libreria "csv" en mi script
# Tambien el script pprint de la libreria pprint
# nos permite printear cosas por consola de forma mas ordenada

# Instancio una variable como un diccionario vacio
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
titulos_fecha = {}

# Abro el archivo .csv
with open('NetflixViewingHistory.csv') as csv_file:
	# Lo vuelvo legible
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Comienzo a iterar por las filas del csv
    for fila in csv_reader:
    	# Cada fila es una lista del tipo Lista[str, str]
        # En la que la primera posicion es el titulo, y la segunda la fecha

        # Asigno el segundo elemento de la fila a una variable "fecha".
    	fecha = fila[1]

    	# Si ya registre la fecha
    	if fecha in titulos_fecha:
    		# Incremento en 1 el valor bajo la key fecha en mi diccionario
    		titulos_fecha[fecha] += 1
    	else:
    		# Si nunca note la fecha
    		# Instancio la key fecha en mi diccionario con el valor 1
    		titulos_fecha[fecha] = 1

# Muestro cuantos titulos vi por fecha
pprint(titulos_fecha)


# Plus

# El siguiente es un algoritmo para hayar el maximo

# Instancio una variable fecha_max donde voy a ir almacenando la fecha cuyo valor es el maximo
# Y su valor respectivamente

# Inicialmente son nulos
fecha_max = ""
titulos_max = 0


# Itero por todas las fechas en el diccionario titulos por fecha.
# Mas especificamente, itera por todas las keys de mi diccionario.
for fecha in titulos_fecha:

	# Si la cantidad de titulos bajo esta fecha es mayor al maximo almacenado
	if titulos_fecha[fecha] > titulos_max:
		# Remplazo la fecha y el valor maximo
		fecha_max = fecha
		titulos_max = titulos_fecha[fecha]

# Muestro la cantidad maxima de titulos vistos en x fecha.
print(fecha_max)
print(titulos_fecha[fecha_max])