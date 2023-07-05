##Script que rellena tablas (Version 2)
import csv
import os
import mariadb


# mysql -u 'user.here' -p

#Tabla que desea rellenar
in_table = input(str("- Que tabla deseas rellenar ? \n- Opciones: \n\t-MEDIO_PRENSA \n\t-FUNDADORES \n\t-NOTICIA \n\t-RRSS \n\t-CATEGORIA \n: "))

#in_host = input("Host: ")
print("\nLogin MariaDB")
in_user = input("User: ")
in_passwd = input("Password: ")

# Ruta del archivo CSV
data_csv = 'csv_data/'+in_table+'.csv'

nombre_tabla = in_table


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
        #next(csv_data)  # Ignorar la primera fila si contiene encabezados

        if( in_table == "MEDIO_PRENSA"):
            for row in csv_data:
                cursor.execute(f"SELECT COUNT(*) FROM MEDIO_PRENSA WHERE NOMBRE_MEDIO = %s AND URL_MEDIO = %s AND AÑO_FUNDACION = %s AND COBERTURA = %s AND CONTINENTE = %s AND PAIS = %s AND REGION = %s AND CIUDAD = %s", row)
                cantidad = cursor.fetchone()[0]
            
                if cantidad == 0:
                # Insertar la fila en la base de datos si no existe
                    insert_query = f"INSERT INTO {nombre_tabla} (NOMBRE_MEDIO, URL_MEDIO, AÑO_FUNDACION, COBERTURA, CONTINENTE, PAIS, REGION, CIUDAD) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                    cursor.execute(insert_query, tuple(row))
                    print("Los datos se han insertado correctamente en la tabla.")
                else:
                # Mostrar la fila duplicada
                    print(f"La fila {row} ya existe en la base de datos.")
                #
                print("Los datos se han insertado correctamente en la tabla.")
        elif( in_table == "FUNDADORES"):

            #next(csv_data)  # Ignorar la primera fila si contiene encabezados
            #
            for row in csv_data:
                cursor.execute(f"SELECT COUNT(*) FROM FUNDADORES WHERE ID_FUNDADOR = %s AND NOMBRE_FUNDADOR = %s AND APELLIDO_FUNDADOR = %s AND NOMBRE_MEDIO = %s ", row)
                cantidad = cursor.fetchone()[0]
            
                if cantidad == 0:
                # Insertar la fila en la base de datos si no existe
                    insert_query = f"INSERT INTO {nombre_tabla} (ID_FUNDADOR, NOMBRE_FUNDADOR, APELLIDO_FUNDADOR, NOMBRE_MEDIO) VALUES (?, ?, ?, ?)"
                    cursor.execute(insert_query, tuple(row))
                    
                else:
                # Mostrar la fila duplicada
                    print(f"La fila {row} ya existe en la base de datos.")
                #
            print("Los datos se han insertado correctamente en la tabla.")
        elif( in_table == "CATEGORIA"):
            next(csv_data)  # Ignorar la primera fila si contiene encabezados
            #
            for row in csv_data:
                cursor.execute(f"SELECT COUNT(*) FROM CATEGORIA WHERE ID_CATEGORIA = %s AND NOMBRE_CATEGORIA = %s AND URL_CATEGORIA = %s ", row)
                cantidad = cursor.fetchone()[0]
            
                if cantidad == 0:
                # Insertar la fila en la base de datos si no existe
                    insert_query = f"INSERT INTO {nombre_tabla} (ID_CATEGORIA, NOMBRE_CATEGORIA, URL_CATEGORIA) VALUES (?, ?, ?)"
                    cursor.execute(insert_query, tuple(row))
                    
                else:
                # Mostrar la fila duplicada
                    print(f"La fila {row} ya existe en la base de datos.")
                #
                print("Los datos se han insertado correctamente en la tabla.")
        elif (in_table == "RRSS"):
            csv_data = csv.reader(file)
            next(csv_data)  # Ignorar la primera fila si contiene encabezados
            #
            for row in csv_data:
                cursor.execute(f"SELECT COUNT(*) FROM RRSS WHERE ID_RRSS = %s AND USUARIO = %s AND ACTUALIZACION = %s AND SEGUIDORES = %s AND NOMBRE_RED = %s ", row)
                cantidad = cursor.fetchone()[0]
            
                if cantidad == 0:
                # Insertar la fila en la base de datos si no existe
                    insert_query = f"INSERT INTO {nombre_tabla} (ID_RRSS ,USUARIO, ACTUALIZACION ,SEGUIDORES, NOMBRE_RED) VALUES (?, ?, ?, ?, ?)"
                    cursor.execute(insert_query, tuple(row))
                
                else:
                # Mostrar la fila duplicada
                    print(f"La fila {row} ya existe en la base de datos.")
                #
            print("Los datos se han insertado correctamente en la tabla.")
        elif( in_table == "NOTICIA"):
            csv_data = csv.reader(file)
            next(csv_data)  # Ignorar la primera fila si contiene encabezados
            #
            for row in csv_data:
                cursor.execute(f"SELECT COUNT(*) FROM NOTICIA WHERE ID_NOTICIA = %s AND XPATH_TITULO = %s AND XPATH_FECHA = %s AND XPATH_CONTENIDO = %s AND URL_NOTICIA = %s", row)
                cantidad = cursor.fetchone()[0]
            
                if cantidad == 0:
                # Insertar la fila en la base de datos si no existe
                    insert_query = f"INSERT INTO {nombre_tabla} (ID_NOTICIA ,XPATH_TITULO ,XPATH_FECHA ,XPATH_CONTENIDO ,URL_NOTICIA ) VALUES (?, ?, ?, ?, ? )"
                    cursor.execute(insert_query, tuple(row))
                    
                else:
                # Mostrar la fila duplicada
                    print(f"La fila {row} ya existe en la base de datos.")
                #
            print("Los datos se han insertado correctamente en la tabla.")
        else: 
            print("TABLA ESCRITA INVALIDA")

    # Guardar los cambios en la base de datos
    conn.commit()

except mariadb.Error as error:
    print(f'Error al conectar a la base de datos: {error}')


conn.close()
print("La conexión a la base de datos se ha cerrado.")