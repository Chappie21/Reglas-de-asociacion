"""
    UNIVERSIDAD RAFAEL URDANETA; PERIODO: 2021; CATEDRA: MINERIA DE DATOS;
    ALUMNOS: 
        - Andrés Chaparro CI: 27552207
        - Carlos Dubuc CI: 28451238

    FECHA DE ENTREGA: 28-6-21
"""
from db.Connection import DBGestor
from db.readConf import ReadConfig
from functions.getItemsets import getItems
from functions.apriori import *

# Entrada de datos
soportemin = float(input("-> Ingrese soporte minimo: "))
confianzamin = float(input("-> Ingrese confianza minima: "))

# Mensaje de espera
print("-> Por favor espere mientras se realiza el analisis, este proceso podria tardar unos instantes...")

# Lista de iteraciones
iteraciones = [] 

# Leer configuracion e inicializar conexion
conexion = DBGestor(ReadConfig())

# Obtener muestreo de itemsets
muestreo = getItems(conexion.getConexion())

# Generar itemsets i = 1
itemsetI1 = generarItemset1(muestreo)

# Clacular frecuencias y soportes de i = 1
for obj in itemsetI1:
    calculos(obj, muestreo)

# Eliminar itemsets menos frecuentes para i = 1
itemsetI1 = eleminarInfrecuencia(itemsetI1, soportemin)
iteraciones.append(itemsetI1) # Guardar iteracion i = 1 en la lista

# Realizar combinaciones, calcular su frecuencia y eliminar infrecuentes para i + 1
nuevoConjunto = itemsetI1

while(nuevoConjunto):

    # Generar combinacion i + 1
    nuevoConjunto = newItemsets(nuevoConjunto)

    # Clacular frecuencia y soporte
    for obj in nuevoConjunto:
        calculos(obj, muestreo)

    # Eliminar itemsets infrecuentes 
    nuevoConjunto = eleminarInfrecuencia(nuevoConjunto, soportemin)
    
    # En caso de no ser vacio el nuevo conjunto (de tener cojuntos frecuentes) lo almacena en las iteraciones
    if nuevoConjunto:
        iteraciones.append(nuevoConjunto)

# Generar reglas de asociacion
reglas = generarReglas(iteraciones[len(iteraciones)-1], iteraciones)

# Verificar que existan reglas, de no existir, no se superó el soporte minimo
if reglas:

    # Eliminar confianzas que no superen o iguales el valor establecido
    reglas = eleminarConfianzabaja(reglas, confianzamin)

    # Verificar que existan reglas, de no existir, no se superó la confianza minima
    if reglas:
        # Mostrar en pantalla reglas generadas en base a el soporte y confianz dado por el usuario
        for obj in reglas:
            print(obj['regla'] + " confianza: " + str(round((obj['confianza'] * 100), 2)) + "%")
    else:
        print("los itemsets no superaron el ", confianzamin ," de confinaza...")
else:
    print("los itemsets no superaron el ", soportemin ," de soporte...")

input("Presione enter para salir...")
