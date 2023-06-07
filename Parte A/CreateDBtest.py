"""
Modelo Relacional:

MedioPrensa (PK_ID_MEDIO, Nombre, URL_MEDIO, FECHA_CRE, Cobertura, Continente, País, Región, Ciudad)
Fundadores (PK_IDFundador, Nombre, Apellido)
Categoría (Nombre, PK_IDCat)
RRSS (PK_ID, Usuario, ActualizaciónSeg, Seguidores, NombreRED)

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
FUNDADORES = """CREATE TABLE IF NOT EXISTS FUNDADORES(
        ID_Fundadores INT PRIMARY KEY,
        NOMBRE VARCHAR(50),
        Apellido VARCHAR(50)
        )"""

MEDIO = """CREATE TABLE IF NOT EXISTS MEDIO(
        
        ID_MEDIO VARCHAR(50) PRIMARY KEY,
        URL_MEDIO VARCHAR(512),
        NOMBRE VARCHAR(50),

        COBERTURA VARCHAR(20),
        CIUDAD VARCHAR(20),
        REGION VARCHAR(20),
        PAIS VARCHAR(20),
        CONTINENTE VARCHAR(20),
        FECHA_CRE DATE,
        )"""

CATEGORIA = """CREATE TABLE IF NOT EXISTS CATEGORIA(
        ID_Fundadores INT PRIMARY KEY,
        NOMBRE VARCHAR(50),
        TIPO VARCHAR(10)
        URL_CATEGORIA VARCHAR(512),
        )"""

RRSS = """CREATE TABLE IF NOT EXISTS RRSS(
        ID_Fundadores INT PRIMARY KEY,
        Usuario VARCHAR(50),
        ActualizaciónSeg VARCHAR(50),
        NombreRED VARCHAR(50)
        )"""