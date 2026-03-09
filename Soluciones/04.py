import pandas as pd
import codecs

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Descifrar los nombres que están en la columna 'nombre_cifrado'
# Primero se convierten a texto y luego se aplica el algoritmo ROT13
df["nombre"] = df["nombre_cifrado"].astype(str).apply(
    lambda x: codecs.decode(x, "rot_13")
)

# Eliminar posibles espacios en blanco al inicio o final del nombre
df["nombre"] = df["nombre"].str.strip()

# Contar cuántas veces aparece cada nombre y seleccionar el más frecuente
resultado = df["nombre"].value_counts().head(1)

# Obtener el nombre y la cantidad de repeticiones
nombre = resultado.index[0]
cantidad = resultado.iloc[0]

# Mostrar el resultado en pantalla
print(f"El nombre más frecuente es {nombre} y aparece {cantidad} veces.")