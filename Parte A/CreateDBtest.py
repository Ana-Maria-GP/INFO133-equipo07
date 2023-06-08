"""
Modelo Relacional:

MedioPrensa (PK_URL_MEDIO, Nom_Medio , COBERTURA, CIUDAD, REGION, PAIS, CONTINENTE, FECHA_Creacion)
Fundadores (PK_Nom_Medio, ID_Fundador, NOMBRE, APELLIDO)
Categoría (PK_URL_Medio, URL_Categoria, NOM_Categoria)

RRSS (Nom_Medio, USUARIO, Fecha_Seguidores, SEGUIDORES, Nom_rrss)

"""
import mysql.connector



#in_host = input("Host: ")
in_user = input("Usuario: ")
in_passwd = input("Contraseña: ")

dataBase = mysql.connector.connect(
  host = "localhost",
  user = in_user,
  passwd = in_passwd,
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS colombia")

cursorObject.execute(dataBase.close())

dataBase = mysql.connector.connect(
  host = "localhost",
  user = in_user,
  passwd = in_passwd,
  database = "Colombia",
)

cursorObject = dataBase.cursor()
# Tablas Simples
MEDIO = """CREATE TABLE IF NOT EXISTS MEDIO(
        
        URL_MEDIO VARCHAR(512) PRIMARY KEY,
        Nom_Medio VARCHAR(50),

        COBERTURA VARCHAR(20),
        CIUDAD VARCHAR(20),
        REGION VARCHAR(20),
        PAIS VARCHAR(20),
        CONTINENTE VARCHAR(20),

        FECHA_Creacion DATE,
        )"""


FUNDADORES = """CREATE TABLE IF NOT EXISTS FUNDADORES(

        Nom_Medio INT PRIMARY KEY,
        ID_Fundador VARCHAR(50),
        NOMBRE VARCHAR(50),
        APELLIDO VARCHAR(50)
        )"""



CATEGORIA = """CREATE TABLE IF NOT EXISTS CATEGORIA(

        URL_Medio VARCHAR(512) PRIMARY KEY,
        URL_CATEGORIA VARCHAR(512),
        NOM_Categoria VARCHAR(50),

        )"""

RRSS (Nom_Medio , Nom_rrss, USUARIO, Fecha_Seguidores, SEGUIDORES)

RRSS = """CREATE TABLE IF NOT EXISTS RRSS(
        Nom_Medio VARCHAR(50) PRIMARY KEY,
        Nom_rrss VARCHAR(50),
        USUARIO VARCHAR(50),
        Fecha_Seguidores VARCHAR(50),
        SEGUIDORES BIGINT
        )"""