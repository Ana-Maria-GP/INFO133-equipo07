# PROYECTO UNIDAD 3 - INTEGRACIÓN SGBD EN LA CONSTRUCCIÓN DE SOFTWARE:
# "Bases de datos de medios de prensa e información territorial"
# INFO133-equipo07
## Colombia
# Integrantes:
    - Sebastián Fuentes
    - Andrés Galaz
    - Ana Gerding
## Construcción de una base de datos sobre medios de prensa de países hispanohablantes.
- Construiremos una base de datos con la información de 55 medios de prensa colombianos, para así, facilitar la investigación en ciencias de la comunicación y ciencias políticas.

- Almacenaremos diferente información para los medios de prensa:
    - Nombre medio de prensa.
    - Ubicación geográfica (ciudad, región, país, continente).
        - En el caso de Colombia, la región corresponde al Departamento.
    - Año de fundación.
    - Cobertura (internacional, nacional o local).
    - Nombre de su(s) fundador(es).
    - Cuentas de Facebook, Instagram y Twitter de cada medio de prensa.
        - Nombre de usuario, número de seguidores y fecha de actualización de seguidores.
    - Categorías presentes en cada medio de prensa.

- Haremos crawling y scraping de una noticia para cada medio de prensa.

## A CONTINUACIÓN ESTÁN LOS LINK DE CADA ARCHIVO UTILIZADO EN NUESTRO PROYECTO:

- PAUTA DEL PROYECTO 
- > https://docs.google.com/document/d/1q6gKxkrsuS5gZz6T2vk3V1HJoG9LCMuv7e748dS6ZKY/edit 

- DICCIONARIO DE DATOS 
- > https://docs.google.com/spreadsheets/d/1R7_2ewGCvhqFhOOvM5Dx-3oklUYIEuugg5Z_59endfM/edit?usp=sharing

- RECOPILACIÓN DE DATOS
- > https://docs.google.com/spreadsheets/d/1qsXV4tbcYRVRxK5yD6JJf-3NBGa_3xxxE0P3tIX4iFE/edit#gid=0

- MEDIOS DE PRENSA (FUENTE)
- > https://www.prensaescrita.com/america/colombia.php


## Consultas validadas Mariadb
> SELECT F.NOMBRE_FUNDADOR,F.APELLIDO_FUNDADOR FROM FUNDADORES F JOIN MEDIO_PRENSA M ON F.NOMBRE_MEDIO = M.NOMBRE_MEDIO WHERE M.NOMBRE_MEDIO ="El Meridiano";

> SELECT MEDIO_PRENSA.NOMBRE_MEDIO FROM MEDIO_PRENSA JOIN RRSS ON MEDIO_PRENSA.NOMBRE_MEDIO = RRSS.NOMBRE_MEDIO WHERE NOMBRE_RED="Facebook" ORDER BY SEGUIDORES DESC LIMIT 2;


## DATOS EXTRAS
- En la carpeta Parte-A_TEST están todos los avances que fuimos haciendo hasta lograr lo que nos piden, tales como los modelos relacional y entidad relación, o los script.

- Dentro de esta carpeta se encuentra otra carpeta llamada "test" en donde se encuentran los script que se usaron como base para hacer los que se encuentran en la carpeta final (Parte_A). 