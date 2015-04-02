#!/usr/bin/python

# El fichero pasado como parametro debe contener una url por linea con fotos

class ListaURLs:
    # Recibe un fichero y carga sus cadenas en una lista
    def __init__(self,nombre):
        self.lista = []
        self.contador = 0

        self.archivo = file(nombre)
        self.cadena = self.archivo.readline()

        while(self.cadena != '\n'):
            self.lista.append(self.cadena)
            self.cadena = self.archivo.readline()
        self.archivo.close()

    # Hace que se empiece por el principio de la lista
    def rebobina(self):
        self.contador = 0

    # Devuelve el siguiente elemento de la lista o '' si llega al final
    def siguiente(self):
        if (self.contador >= len(self.lista)):
            return ''
        else:
            self.valor = self.lista[self.contador]
            self.contador = self.contador + 1
            return self.valor

    # Comprueba si hemos llegado al final de la lista
    def fin(self):
        return(self.contador == len(self.lista))

    # Comprueba si existe el directorio, sino lo crea y cambia a ese directorio
    def crea_directorio(self):
        componentes = cadena.split('.')
        if(os.path.exists(componentes[0])):
            print "Error, el directorio ya existe"
            sys.exit()
        else:
            os.makedirs(componentes[0])
            print "Creando directorio " + componentes[0]

    # Recorre la lista de URLs, las descarga y las guarda en un fichero
    def descarga_urls(lista):
        lista.rebobina()
        while(not lista.fin()):
            url = lista.siguiente()
            # Dividimos la url en dos partes, fichero y direccion
            componentes = url.split('/')
            servidor = componentes[2]

            # Construimos la ruta de la imagen eliminando el servidor y el http://
            ruta_imagen = '/'
            for i in range(3, len(componentes)):
                ruta_imagen = ruta_imagen + '/' + componentes[i]

            # Descarga el fichero y lo guarda
            # url[:-1] es la cadena menos el ultimo caracter
            print "Descargando image: " + url[:-1]
            conexion = httplib.HTTPConnection(servidor)
            conexion.request("GET", ruta_imagen)
            respuesta = conexion.getresponse()
            datos = respuesta.read()
            conexion.close()

            # El nombre del fichero es el ultimo elemento de la lista de componentes
            nom_fichero = componentes[len(componentes) - 1]
            # Eliminamos el salto de linea final
            nom_fichero = nom_fichero[:-1]

            # Abrimos el fichero, lo escribimos y lo cerramos
            archivo = file(nom_fichero, 'w')
            archivo.write(datos)
            archivo.close()

    # Crea el fichero HTTP
    def genera_index(lista):
        print "Generando indice index.html"
        archivo = file('index.html', 'w')
        archivo.write('<html>\n')
        archivo.write('<head>\n')
        archivo.write('<title>Imagenes</title>\n')
        archivo.write('</head>\n')
        archivo.write('<body>\n')
        archivo.write('<h1>Imagenes</h1>\n')
        archivo.write('<ul>\n')

        lista.rebobina()
        url = lista.siguiente()

        # Dividimos la URL
        componentes = url.split('/')
        imagen = componentes[len(componentes) - 1]

        # Recorremos la url
        while(url != ''):
            archivo.write('<li><img src=\"' + imagen  +'\"></img></li>\n')
            url = lista.siguiente()
            componentes = url.split('/')
            imagen = componentes[len(componentes) -1]

        archivo.write('</ul>\n')
        archivo.write('</body>\n')
        archivo.write('</html>\n')

        archivo.close()


#-------------------------------------------------------------------------------------

if __name__ == '__main__':

    import httplib
    import os
    import os.path
    import sys

    # Comprobamos los argumentos
    if len(sys.argv) == 2:
        # Pasamos el fichero al constructor
        lista = ListaURLs(sys.argv[1])
        crea_directorio(sys.argv[1])
        descarga_urls(lista)

    elif len(sys.argv) == 0:
        print 'La sintaxis del programa es:\n'
        print sys.argv[0] + ' archivo\n'
        print 'El archivo debe contener una URL por linea'

    else:
        print 'ERROR: la sintaxis es ' + sys.argv[0] + ' <fichero>'

