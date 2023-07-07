#
#
# 
"""

"""

import mysql.connector

# Conexión a la base de datos
connection = mysql.connector.connect(
    host='localhost', 
    user='usuario', 
    password='  ', 
    database=' ')
cursor = connection.cursor()

# Carga de datos de prueba en la tabla MEDIO_PRENSA
cursor.execute("""
    INSERT INTO MEDIO_PRENSA (PK_NOMBRE_MEDIO, URL_MEDIO, AÑO_FUNDACION, COBERTURA, CONTINENTE, PAIS, REGION, CIUDAD, FK_URL_CATEGORIA, FK_NOMBRE_CATEGORIA)
    VALUES
    ('Medio1', 'http://medio1.com', 2000, 'Local', 'América', 'Estados Unidos', 'California', 'Los Angeles', 'http://categoria1.com', 'Categoría1'),
    ('Medio2', 'http://medio2.com', 1995, 'Internacional', 'Europa', 'España', 'Madrid', 'Madrid', 'http://categoria2.com', 'Categoría2')
""")

# Carga de datos de prueba en la tabla FUNDADORES
cursor.execute("""
    INSERT INTO FUNDADORES (PK_ID_FUNDADOR, NOMBRE_FUNDADOR, APELLIDO_FUNDADOR)
    VALUES
    (1, 'John', 'Doe'),
    (2, 'Jane', 'Smith')
""")

# Carga de datos de prueba en la tabla CATEGORIA
cursor.execute("""
    INSERT INTO CATEGORIA (PK_NOMBRE_CATEGORIA, FK_NOMBRE_MEDIO, URL_CATEGORIA)
    VALUES
    ('Categoría1', 'Medio1', 'http://categoria1.com'),
    ('Categoría2', 'Medio2', 'http://categoria2.com')
""")

# Carga de datos de prueba en la tabla RRSS
cursor.execute("""
    INSERT INTO RRSS (PK_ID_RRSS, , USUARIO, ACTUALIZACION, SEGUIDORES, NOMBRE_RED)
    VALUES
    (1, 'portafolio', '2022-10-13', 1000, 'Twitter'),
    (1, 'portafolio', '2022-10-13', 3121, 'Facebook'),
    (1, 'portafolio', '2023-03-22', 6700, 'Instagram'),

    (2, 'usuario1', '2023-03-22', 6700, 'Instagram'),
    (3, 'usuario2', '2023-02-12', 2000, 'Facebook')
""")

# Carga de datos de prueba en la tabla FUNDADO_POR
cursor.execute("""
    INSERT INTO FUNDADO_POR (FK_NOMBRE_MEDIO, FK_ID_FUNDADOR, FK_NOMBRE_FUNDADOR, FK_APELLIDO_FUNDADOR)
    VALUES
    ('Medio1', 1, 'John', 'Doe'),
    ('Medio2', 2, 'Jane', 'Smith')
""")

# Carga de datos de prueba en la tabla TENER
cursor.execute("""
    INSERT INTO TENER (FK_NOMBRE_MEDIO, FK_ID_RRSS)
    VALUES
    ('Medio1', 1),
    ('Medio2', 2)
""")

# Carga de datos de prueba en la tabla NOTICIAS
cursor.execute("""
    INSERT INTO NOTICIAS (PK_ID_NOTICIA, FK_NOMBRE_MEDIO, TITULO, CONTENIDO, FECHA)
    VALUES
    (1, 'Medio1', 'Noticia 1', 'Contenido de la noticia 1', '2023-01-01'),
    (2, 'Medio2', 'Noticia 2', 'Contenido de la noticia 2', '2023-02-01')
""")

# Confirmar los cambios en la base de datos
connection.commit()