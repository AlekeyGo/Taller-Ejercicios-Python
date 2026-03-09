import pandas as pd

# Cargar los datos desde el archivo CSV
datos = pd.read_csv('data/personas.csv')

# Verificar qué registros tienen el campo 'id' con caracteres no numéricos
# astype(str) asegura que todos los valores sean tratados como texto
# isnumeric() identifica si el contenido es completamente numérico
# ~ invierte el resultado para detectar los que NO son numéricos
solucion = (~datos["id"].astype(str).str.isnumeric()).sum()

# Mostrar la respuesta en pantalla
print("¿Cuántas filas tienen el campo id con caracteres no numéricos? RESPUESTA:", solucion)