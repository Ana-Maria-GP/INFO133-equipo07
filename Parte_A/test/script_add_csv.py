
##Script que rellena tablas (Version 1), mantener formato y usar como plantilla para las siguientes tablas
import csv
import mariadb
# mysql -u 'user.here' -p

#in_host = input("Host: ")
in_user = input("Usuario: ")
in_passwd = input("Contraseña: ")

# Ruta del archivo CSV
data_csv = 'MEDIO_PRENSA.csv'

# Nombre de la tabla en la base de datos
nombre_tabla = 'MEDIO_PRENSA'

try:
    # Conexión a la base de datos
    conn = mariadb.connect(
        user        = in_user,
        password    = in_passwd,
        host        = "127.0.0.1",
        port        = 3306,
        database    = 'COLOMBIA'
    )
    cursor = conn.cursor()

    # Leer el archivo CSV y agregar los datos a la tabla
    with open(data_csv, 'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)  # Ignorar la primera fila si contiene encabezados

        for row in csv_data:
            # Generar la consulta de inserción
            insert_query = f"INSERT INTO {nombre_tabla} (NOMBRE_MEDIO, URL_MEDIO, AÑO_FUNDACION, COBERTURA, CONTINENTE, PAIS, REGION, CIUDAD) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_query, tuple(row))

    # Guardar los cambios en la base de datos
    conn.commit()
    print("Los datos se han insertado correctamente en la tabla.")

except mariadb.Error as error:
    print(f'Error al conectar a la base de datos: {error}')


conn.close()
print("La conexión a la base de datos se ha cerrado.")