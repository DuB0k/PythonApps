import re
import mechanize

br = mechanize.Browser()

br.set_handle_robots(False)

respuesta = br.open("http://www.linux-magazine.es/")

br.select_form(nr=1)

br["searchtext"] = "python"

br.submit()

# Estamos en la pagina de resultados

# Primer resultado
urls = [url.absolute_url for url in br.links(url_regex = re.compile(r"pdf$"))]

# Eliminamos duplicados
urls = dict(zip(urls,urls)).keys()

r = re.compile(".*/(\d+)/(.*)$")

for url in urls:
    m = r.match(url)
    nombre = m.group(1) + "-" + m.group(2)
    print nombre

    respuesta = br.open(url)
    datos = respuesta.read()

    fichero = open(nombre, 'w')
    fichero.write(datos)
    fichero.close()

