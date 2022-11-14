import requests
import lxml.html as html
import os
import datetime

#Se crean constantes según las expresiones que se tengan:
HOME_URL = 'https://www.larepublica.co/'
XPATH_LINK_TO_ARTICLE = '//text-fill/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]//span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'

#Se crean las funciones que harán al script ejecutarse:

def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            #Traemos el HTML de la noticia
            notice = response.content.decode('utf-8')
            #Se convierte a un archivo "con superpoderes" para aplicar Xpath
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[1] #El resultado es una lista, puede tener varios elementos, sólo queremos el primero (El titulo)
                title = title.replace('\"','') #Elimina las Comillas dobles del título
                title = title.replace('    ','')
                title = title.replace('\n','')
                title = title.replace('?','')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            
            #Puede ocurrir que hayan noticias que no tengan Summary, así que se hace un catch:
            except IndexError:
                return

            #Manejador contextual: Si mi archivo se cierra de manera inesperada, matenga todo de manera segura
            #Se maneja la ruta [fecha/tituloNoticia.txt], se guarda el archivo con permisos de escritura y un encoding de utf-8
            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')

        else:
            raise ValueError(f'Error: {response.status_code}')
        
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        #200 : Salió bien
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            #Toma el contenido de "home" de texto y transformarlo en un documento para hacer Xpath
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            #print(links_to_notices)

            today = datetime.date.today().strftime('%d-%m-%Y')
            #Si no existe una carpeta llamada "today"
            if not os.path.isdir(today):
                os.mkdir(today)
            
            #Por cada link que haya en la lista, se accede al link y se extrae la info
            for link in links_to_notices:
                parse_notice(link,today)

        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == "__main__":
    run()