import pandas as pd

# Definir la ruta del archivo de datos
RUTA_ARCHIVO = 'data/personas.csv'

# Cargar los datos desde el archivo CSV
datos = pd.read_csv(RUTA_ARCHIVO)

# Función para descifrar una palabra utilizando el algoritmo ROT13
def decifrar_palabra(palabra_cifrada):
    import codecs
    nueva_palabra = codecs.decode(palabra_cifrada, 'rot_13')
    return nueva_palabra

# Aplicar la función de descifrado a la columna 'nombre_cifrado'
# y guardar el resultado en una nueva columna
datos['nombre_decifrado'] = datos['nombre_cifrado'].apply(decifrar_palabra)

# Crear una condición para filtrar los registros cuyo nombre descifrado sea "Juan"
condicion = datos['nombre_decifrado'] == 'Juan'

# Contar cuántas veces aparece el nombre "Juan"
print('Juan aparece: ', datos[condicion].shape[0])