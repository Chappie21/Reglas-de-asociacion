"""
    Este script se encarga de realizar unca consulta a la base de datos
    para obtener cada una de las transacciones.

    Además de esto, se encarga de trasnformar los datos (trasnacciones),
    dandoles un formato de diccionario, y el itemset que este contiene.

    Los datos son trasformados de nombre clave nombre de producto) o fecha,
    a valores numerios de prioridad, siendo los dias de 0 - 6, y los productos
    de 7 - 22 (22 items en total).

    La obtencion de los dias se hace por medio de la libreria pandas, el cual
    recibe una fecha en formato AA-MM-DD, y retorna el valor correspondiente,
    de 0 a 6, (lunes a domingo respectivamente).
"""
import psycopg2
import pandas as pd
from model.structItems import productos

# OBTENER TRANSACCIONES DE LA BASE DE DATOS
def getItems(connection):

    query = """
                select Factura.id_factura, Factura.Fecha_factura, Producto.nombre_producto 
                from factura, Producto, Venta
                where Factura.id_factura = Venta.id_factura 
                AND Venta.id_producto = Producto.Id_producto
            """

    lista = [] # LISTA DONDE SE ALMACENARÁ EL MUESTREO

    try:

        cursor = connection.cursor()
        cursor.execute(query)
        Rconsulta = cursor.fetchall()  # Obtenemos todos los datos de la consulta

        id = 0

        for i in range(0, len(Rconsulta)):

            if id == Rconsulta[i][0]:
                lista[len(lista)-1]['itemset'].append(productos[Rconsulta[i][2]])
            else:
                lista.append(
                    {
                        "itemset": [pd.Timestamp(Rconsulta[i][1]).dayofweek, productos[Rconsulta[i][2]]]
                    }
                )

            id = Rconsulta[i][0] # obtener id de registro

    except (Exception, psycopg2.DatabaseError) as error:
        print('Error al obtener muestreo...')
        print(error)

    return lista;