#Script que realiza scraping a tablas html
#Bibliografia   ->
#               https://es.wikipedia.org/wiki/Regiones_de_Chile
#               https://mrenrique.medium.com/web-scraping-de-tablas-html-de-wikipedia-usando-pandas-9045994b6b34
#               https://bobbyhadz.com/blog/python-no-module-named-pandas

# Hacer peticion HTTP
import requests
# Manipular código y guardar datos tabulares en archivo CSV
# si no lo tienes ejecutar $pip install pandas
import pandas as pd


# url de la página web a «escrapear»
url = 'https://es.wikipedia.org/wiki/Regiones_de_Chile'

# pasar "User-agent" para simular interacción con la página usando Navegador web
headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

respuesta = requests.get(url, headers=headers)

# El código de respuesta <200> indicará que todo salió bien
print(respuesta)

all_tables = pd.read_html(respuesta.content, encoding = 'utf8')

print(f'Total de tablas encontradas: {len(all_tables)}')

matched_table = pd.read_html(respuesta.text, match='Imagen de la región')
#matched_table = pd.read_html(respuesta.text, match='Regiones de Chile')

# imprime numero de tablas que coinciden con parametro match
print(f'Total de tablas encontradas: {len(matched_table)}')

# Guardar tabla en variable con nombre semántico
Regiones = matched_table[0]

# Verificamos si es la tabla que buscamos
print(Regiones)
print(matched_table)
"""
for (i in Regiones)
{
    print("Esta es la informacion:", i)
}
"""