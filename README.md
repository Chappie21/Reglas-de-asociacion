# Reglas-de-asociasion
 Proyecto de mineria de datos, aplicando regla de asociasion para determinar la venta de productos tomando tambien en cuenta loas días de la semana
 
# Configuracion
Dentro de la carpeta del proyecto se enceuntra un backup de la base de datos elaborada en postgresql,
es necesario crear una nueva base de datos, y restaurarla colocando la ruta de este backup.

Posterior a esto en el archivo de configuracion .ini, deben colocarse las credenciales del
servidor base de datos, y el nombre de la base de datos que contiene el backup.

Una vez realizado esto, el programa estará listo para su uso.

# Ejecucion
Para ejecutar el programa, abra un terminal, entre a la ruta o carpeta del proyecto
y ejecute el index.py con el comando "python3 index.py" o "python index.py", una vez hecho
esto se ejecutará el programa.

# En ejecucion
Debido a el numero de registros en la base de datos, el analisis y calculo de reglas de asociasion de este puede tardar unos instantes, dependiendo del numero de soporte y confianza
ingresado por el usuario.
