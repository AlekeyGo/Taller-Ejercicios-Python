import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Normalizar la columna 'email':
# - Eliminar espacios en blanco al inicio y final
# - Convertir a minúsculas
# Luego verificar cuáles correos terminan con "@gmail.com" y contarlos
# na=False asegura que valores NaN no generen error
cantidad = df["email"].str.strip().str.lower().str.endswith("@gmail.com", na=False).sum()

# Mostrar el resultado en pantalla
print(f"Existen {cantidad} registros cuyo correo electrónico pertenece al dominio 'gmail.com'.")