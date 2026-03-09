import pandas as pd
import codecs

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Contar los registros donde:
# - El nombre descifrado de 'nombre_cifrado' usando ROT13 es "jose"
# - El apellido descifrado de 'apellido_cifrado' usando ROT13 es "garcia"
# En ambos casos se normaliza el texto eliminando espacios y convirtiendo a minúsculas
cantidad = (
    df["nombre_cifrado"]
    .apply(lambda x: codecs.decode(str(x), "rot_13"))
    .str.strip()
    .str.lower()
    .eq("jose")
    &
    df["apellido_cifrado"]
    .apply(lambda x: codecs.decode(str(x), "rot_13"))
    .str.strip()
    .str.lower()
    .eq("garcia")
).sum()

# Mostrar el resultado en pantalla
print(f"Se encontraron {cantidad} registros correspondientes a personas llamadas 'Jose Garcia'.")