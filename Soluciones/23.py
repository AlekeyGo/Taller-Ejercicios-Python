import pandas as pd
import codecs

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Contar los registros donde:
# - El nombre descifrado de 'nombre_cifrado' con ROT13 es "Carlos"
# - La ciudad, normalizada (texto, sin espacios, minúsculas), es "Cali"
cantidad = (
    df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), "rot_13")).str.strip().str.lower().eq("carlos")
    &
    df["ciudad"].astype(str).str.strip().str.lower().eq("cali")
).sum()

# Mostrar el resultado en pantalla
print(f"Se encontraron {cantidad} registros con nombre 'Carlos' que viven en la ciudad de Cali.")