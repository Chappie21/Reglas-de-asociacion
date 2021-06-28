"""
    Clase DBGestor, se encarga de realizar una conexion a la base de datos, y resguardar
    esta conexion.

    Su iniciador recibe como parametro un diccionario que debe contener los siguientes
    atributos:
        - host: direccion ip del host contenedor de la base de datos
        - port: puerto a donde realizar la peticion a el host contenedor de la base de datos
        - user: usuario de la base de datos
        - password: contraseña o clave del usuario de la base de datos
        - database: nombre de la base de datos a conectar

"""
from os import error
import psycopg2

# Conexion con base de datos
class DBGestor:
    
    def __init__(self, data):
        self.__host = data['host']
        self.__port = data['port']
        self.__user = data['user']
        self.__password = data['password']
        self.__database = data['database']

        # REALIZAR LA CONEXION
        self.__conexion = self.__connection()

    # realizar o ejeuctar la conexion
    def __connection(self):

        conexion = None

        try:
            # SE ESTABLECE CONEXION
            conexion = psycopg2.connect(host = self.__host, port = self.__port, database = self.__database, user = self.__user, 
                                    password = self.__password)

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

        return conexion # Retornar conexion establecida
    
    # Obtener conexion
    def getConexion(self):
        return self.__conexion
