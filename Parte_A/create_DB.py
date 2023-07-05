#Codigo que genera la DB
"""
MEDIO_PRENSA (PK_NOMBRE_MEDIO, URL_MEDIO, AÑO_FUNDACION, COBERTURA, CONTINENTE, PAIS, REGION, CIUDAD)
FUNDADORES (PK_ID_FUNDADOR, NOMBRE_FUNDADOR, APELLIDO_FUNDADOR , FK_NOMBRE_MEDIO)
CATEGORIA (PK_ID_CATEGORIA, NOMBRE_CATEGORIA, FK_NOMBRE_MEDIO, URL_CATEGORIA)
RRSS (PK_ID_RRSS, USUARIO, ACTUALIZACION, SEGUIDORES, NOMBRE_RED, FK_NOMBRE_MEDIO)
NOTICIA (PK_ID_NOTICIA, XPATH_TITULO, XPATH_FECHA, XPATH_CONTENIDO, URL_NOTICIA, FK_NOMBRE_MEDIO)
FUNDADO_POR (FK_NOMBRE_MEDIO, FK_ID_FUNDADOR)
"""

import mariadb
import sys

#in_host = input("Host: ")
in_user = input("Usuario: ")
in_passwd = input("Contraseña: ")
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user        = in_user,
        password    = in_passwd,
        host        = "127.0.0.1",
        port        = 3306
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

DB_NAME = "COLOMBIA"

# Comprobar si la base de datos ya existe
cur.execute(f"SHOW DATABASES LIKE '{DB_NAME}'")
resultado = cur.fetchone()

if resultado:
    print(f"La base de datos '{DB_NAME}' ya existe.")
else:
    # Crear la base de datos si no existe
    cur.execute(f"CREATE DATABASE {DB_NAME}")
    print(f"Se creó la base de datos '{DB_NAME}'.")

cur.execute("USE COLOMBIA")

# Tablas Simples


cur.execute("""
    CREATE TABLE IF NOT EXISTS MEDIO_PRENSA (
        NOMBRE_MEDIO VARCHAR(100) PRIMARY KEY,
        URL_MEDIO VARCHAR(100),
        AÑO_FUNDACION INT,
        COBERTURA VARCHAR(100),
        CONTINENTE VARCHAR(100),
        PAIS VARCHAR(100),
        REGION VARCHAR(100),
        CIUDAD VARCHAR(100)        
    )
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS FUNDADORES (
        ID_FUNDADOR INT PRIMARY KEY,
        NOMBRE_FUNDADOR VARCHAR(100),
        APELLIDO_FUNDADOR VARCHAR(100),
        NOMBRE_MEDIO VARCHAR(100),
        FOREIGN KEY (NOMBRE_MEDIO) REFERENCES MEDIO_PRENSA(NOMBRE_MEDIO)
    )
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS CATEGORIA (
        ID_CATEGORIA INT PRIMARY KEY,
        NOMBRE_CATEGORIA VARCHAR(100),
        NOMBRE_MEDIO VARCHAR(100),
        URL_CATEGORIA VARCHAR(500),
        FOREIGN KEY (NOMBRE_MEDIO) REFERENCES MEDIO_PRENSA(NOMBRE_MEDIO)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS RRSS (
        ID_RRSS INT PRIMARY KEY,
        USUARIO VARCHAR(100),
        ACTUALIZACION DATE,
        SEGUIDORES BIGINT,
        NOMBRE_RED VARCHAR(100),
        NOMBRE_MEDIO VARCHAR(100),
        FOREIGN KEY (NOMBRE_MEDIO) REFERENCES MEDIO_PRENSA(NOMBRE_MEDIO)
    )
""")

# Tablas Dependientes
cur.execute("""
    CREATE TABLE IF NOT EXISTS NOTICIA (
        ID_NOTICIA INT PRIMARY KEY,
        XPATH_TITULO VARCHAR(500),
        XPATH_FECHA VARCHAR(500),
        XPATH_CONTENIDO VARCHAR(500),
        URL_NOTICIA VARCHAR(500),
        NOMBRE_MEDIO VARCHAR(100),
        FOREIGN KEY (NOMBRE_MEDIO) REFERENCES MEDIO_PRENSA(NOMBRE_MEDIO)
    )
""")

# Tablas Intermedias
cur.execute("""
    CREATE TABLE IF NOT EXISTS FUNDADO_POR (
        NOMBRE_MEDIO VARCHAR(100),
        FOREIGN KEY (NOMBRE_MEDIO) REFERENCES MEDIO_PRENSA(NOMBRE_MEDIO),
        ID_FUNDADOR INT,
        FOREIGN KEY (ID_FUNDADOR) REFERENCES FUNDADORES (ID_FUNDADOR)
    )
""")

print("DB created successfully")
conn.commit() 
conn.close()