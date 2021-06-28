"""
    FUNCIONES DE TAREAS GENERALES AL MOMENTO DE LLEVAR ACABO EL ALGORITMO
    APRIORI
"""
from model.structItems import objetos

# OBTENER ITEMSETS I = 1
def generarItemset1(muestra):
    
    itemsets = [] # conjunto de intemsets i = 1

    # COMPROBAR EXISTENCIA DEL ITEM
    def itemExist(item):
        for obj in itemsets:
            if item == obj['itemset'][0]:
                return True

        return False

    # Generar items
    for conjunto in muestra:
        for item in conjunto['itemset']:
            if not itemExist(item):
                itemsets.append(
                    {
                        "itemset": [item],
                        "frecuencia": 0,
                        "soporte": 0
                    }
                )
    
    return itemsets

# CALCULAR FRECUENCIA Y SOPORTE
def calculos(conjunto, muestreo):

    principal = muestreo

    for transa in principal:

        coincidencia = 0 # contador de coincidencias 

        for items in conjunto['itemset']:
            for dato in transa['itemset']:
                if str(items) == str(dato):
                    coincidencia += 1
            
            # Si se cumplienron todas la coincidencias, la frecuencia aumentan
            if coincidencia == len(conjunto['itemset']):
                conjunto['frecuencia'] += 1
    
    # calcular soporte
    conjunto['soporte'] = conjunto['frecuencia']/len(principal)


# Eliminar itemsets infrecuentes
def eleminarInfrecuencia(itemsets, sopmin):

    newItemset = []

    for obj in itemsets:
        if obj['soporte'] >= sopmin:
            newItemset.append(obj)

    return newItemset

# Crear nuevos itemsets para i = i + 1
def newItemsets(itemsets):
    
    # Obtener itemsets o litsas neta de los conjuntos
    join1 = obtener_itemsets(itemsets)

    nuevos = [] # nuevos itemsets de i + 1
    
    for i in range(len(join1)):
        for j in range(i+1, len(join1)):
            for y in range(len(join1[i])):
                if join1[i][y] == join1[j][y]:
                    pass
                elif y < len(join1[i])-1:
                    break
                else:
                    nuevoitemset = join1[i].copy()
                    nuevoitemset.append(join1[j][len(join1[j])-1])
                    nuevoitemset.sort()
                    nuevos.append({
                         "itemset": nuevoitemset,
                         "frecuencia": 0,
                         "soporte": 0
                     })
                    
    return nuevos

# Obtener itemsets o datos neta
def obtener_itemsets(itemsets):

    lista = []
    for conjunto in itemsets:
        lista.append(conjunto['itemset'])

    return lista

# Generador de reglas
def generarReglas(itemsets, iteraciones):
    
    reglas = [] # lista de reglas

    for conjunto in itemsets:

        soporteUnion = conjunto['soporte']

        for i in range(len(conjunto['itemset'])):

            parte1 = [conjunto['itemset'][i]]
            soporte1 = buscarSoporte(parte1, iteraciones)

            parte2 = []
            parte2num = []

            for j in range(len(conjunto['itemset'])):
                if i != j:
                    parte2.append(objetos[conjunto['itemset'][j]])
                    parte2num.append(conjunto['itemset'][j])

            # calcular confianza
            confianza1 = soporteUnion/soporte1

            # añadir regla
            reglas.append({
                "regla": str([objetos[parte1[0]]]) + " => " + str(parte2),
                "confianza": confianza1
            })

            # Calcular la regla inversa para itemset de i > 2, debido a que si es i = 2 en la siguiente itercion caulcula el inverso
            if(len(conjunto['itemset']) > 2):
                soporte2 =  buscarSoporte(parte2num, iteraciones)

                # calcular confianza
                confianza2 = soporteUnion/soporte2

                # añadir regla
                reglas.append({
                    "regla": str(parte2) + " => " + str([objetos[parte1[0]]]),
                    "confianza": confianza2
                })
            
    return reglas       

# buscar soporte
def buscarSoporte(dato, iteraciones):

    for conjunto in iteraciones:
        for itemset in conjunto:
            if(set(itemset['itemset']) == set(dato)):
                return itemset['soporte']

    return None

# busca dentro del itemset si se contiene algún dia, y devulve un string con formato
def contieneDia(arr):

    po = None
    productos = []
    regla = ""

    for i in len(arr):
        if arr[i] in range(0, 6):
            po = i
        else:
            productos.append(arr)

    if len(productos) != 0:
        regla = arr[po] + " ^ " + productos 
    else:
        regla = str([arr[po]])

    return regla

# Eliminar reglas que no superen la confianza minima
def eleminarConfianzabaja(itemsets, confianzamin):

    newItemset = []

    for obj in itemsets:
        if obj['confianza'] >= confianzamin:
            newItemset.append(obj)

    return newItemset
