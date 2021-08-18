import csv
# incluyo la libreria "csv" en mi script

# Tomo el titulo a contabilizar 
serie = input("Ingrese la serie que quiere contar: ")

# Abro el archivo .csv
with open('NetflixViewingHistory.csv') as csv_file:
    # Lo vuelvo legible
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Instancio un contador en 0
    cont = 0

    # Comienzo a iterar por las filas del csv
    for fila in csv_reader:
    	# Cada fila es una lista del tipo Lista[str, str]
        # En la que la primera posicion es el titulo, y la segunda la fecha

        # Asigno el primer elemento de la fila a una variable "titulo".
        titulo = fila[0]
        
        # Si el titulo de la serie ingresado esta contenido en este titulo
    	if serie in titulo:
    		cont += 1
            # Sumo 1 a mi contador (El operador ++ no existe en python)

    print("Viste " + str(cont) + " capitulos de " + serie)