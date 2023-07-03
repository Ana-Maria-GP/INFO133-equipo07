import random
from requests_html import HTMLSession
import w3lib.html
import html
import mariadb
import sys
import time

def format_date(date):
        return(date.split("T")[0])

session = HTMLSession()

## Simular que estamos utilizando un navegador web
USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
headers = {'user-agent':random.choice(USER_AGENT_LIST) }


#Medio de prensa -> El Tiempo
#Link asociado al medio 
# - https://www.eltiempo.com/justicia/investigacion/aviones-de-fuerza-aerea-colisionaron-en-vuelo-de-entrenamiento-en-villavicencio-782649 
xpath_title="/html/body/div[1]/article/div[2]/section/div[2]/div[3]/h1"
xpath_date="/html/body/div[1]/article/div[2]/div[3]/section/div[1]/div[2]/div[2]/div[3]/div/span"
xpath_text="/html/body/div[1]/article/div[2]/div[3]/section/div[1]/div[2]/div[4]/div/p[1]"

# Conectarse a MariaDB
try:
    conn = mariadb.connect(
        user="root",
        password="1234567890",
        host="localhost",
        port=3306,
        database="web_scraping"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

#Listar las URLs que escrapear
# Ejecutar la consulta SQL para obtener las URLs
#cur.execute("SELECT url FROM url")

# Obtener los resultados de la consulta

resultados = 'https://www.eltiempo.com/justicia/investigacion/aviones-de-fuerza-aerea-colisionaron-en-vuelo-de-entrenamiento-en-villavicencio-782649'

# Crear una lista para almacenar las URLs
urls = []

# Iterar sobre los resultados y añadir las URLs a la lista
for resultado in resultados:
    print(resultado[0]) # Se asume que la columna "url" es la primera en la consulta

    response = session.get(resultado[0],headers=headers)

    ## Analizar el contenido
    title = response.html.xpath(xpath_title)[0].text
    date = format_date(response.html.xpath(xpath_date)[0])

    list_p = response.html.xpath(xpath_text)
    text=""
    for p in list_p:
        content = p.text
        content = w3lib.html.remove_tags(content)
        content = w3lib.html.replace_escape_chars(content)
        content = html.unescape(content)
        content = content.strip()
        text=text+" "+content

    #Guardar los datos en MariaDB
    query= f"INSERT INTO news (url,title,date,content) VALUES ('{resultado[0]}', '{title}', '{date}', '{text}')"

    cur.execute(query)
    conn.commit()
    time.sleep(1)

conn.close()