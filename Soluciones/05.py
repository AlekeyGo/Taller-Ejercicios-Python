import pandas as pd
import codecs

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Descifrar los apellidos que están en la columna 'apellido_cifrado'
# Se convierten a texto y se aplica el algoritmo ROT13
df["apellido"] = df["apellido_cifrado"].apply(
    lambda x: codecs.decode(str(x), "rot_13")
).str.strip()

# Contar cuántas veces aparece cada apellido y seleccionar el más frecuente
resultado = df["apellido"].value_counts().head(1)

# Mostrar el apellido más frecuente y su número de repeticiones
print(f"El apellido más frecuente es {resultado.index[0]} y aparece {resultado.iloc[0]} veces.")