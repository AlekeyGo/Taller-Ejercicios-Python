import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Comparar el campo 'email' original con su versión sin espacios
# str.strip() elimina espacios al inicio y al final del texto
# Si son diferentes, significa que el correo tenía espacios adicionales
# Luego se cuentan esos registros
cantidad = (df["email"] != df["email"].str.strip()).sum()

# Mostrar el resultado en pantalla
print(f"Se identificaron {cantidad} registros cuyo campo email contiene espacios adicionales.")