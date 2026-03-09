import pandas as pd
import codecs

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Contar los registros donde:
# - El nombre descifrado de 'nombre_cifrado' con ROT13 es "Ana"
# - La profesión, normalizada (texto, sin espacios, minúsculas), es "Medico"
cantidad = (
    df["nombre_cifrado"]
    .apply(lambda x: codecs.decode(str(x), "rot_13"))
    .str.strip()
    .str.lower()
    .eq("ana")
    &
    df["profesion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("medico")
).sum()

# Mostrar el resultado en pantalla
print(f"Existen {cantidad} registros donde el nombre es 'Ana' y la profesión corresponde a 'Medico'.")