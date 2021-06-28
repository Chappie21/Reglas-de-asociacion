"""
    Este script se encarga de la lectura del archivo de configuracion .ini
    leyendo cada una de las propiedades correspondiente a la conexion a
    la base de datos.

    Siendo así más centralizado y modular el programa.
"""
from configparser import ConfigParser

# Obtener archivo de configuracion y leer sus propiedades (retorna un diccionario)
def ReadConfig(archivo = 'config.ini', seccion = 'postgresql'):
    
    # CREAR EL PARSER DEL ARCHIVO Y LEERLO
    parser = ConfigParser()
    parser.read(archivo)

    # Obtener los datos de la seccion de configuracion (postregsql)
    config = {} 

    if parser.has_section(seccion):

        for param in parser.items(seccion):
            config[param[0]] = param[1]
    else:
        raise Exception('Seccion {0} encontrada en el archivo {1}'.format(seccion, archivo))

    return config