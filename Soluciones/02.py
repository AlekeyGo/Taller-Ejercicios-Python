import pandas as pd
import codecs 

# Cargar los datos desde el archivo CSV
datos = pd.read_csv('data/personas.csv')

# Definir el texto original que queremos buscar
texto_original = 'Maria'

# Cifrar el texto usando el algoritmo ROT13
texto_cifrado = codecs.encode(texto_original, 'rot_13')
print(f'Cifrado: {texto_cifrado}')

# Crear una condición para filtrar los registros cuyo nombre cifrado sea 'Znevn' (Maria en ROT13)
condicion = datos['nombre_cifrado'] == 'Znevn'

# Filtrar el DataFrame usando la condición
datos_nuevos = datos[condicion]

# Contar cuántas veces aparece "Maria" en el dataset
print(('El numero de repeticiones de Maria es: ', datos_nuevos.shape[0]))