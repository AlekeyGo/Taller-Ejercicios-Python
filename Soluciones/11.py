import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Normalizar la columna 'profesion':
# - Convertir los valores a texto
# - Eliminar espacios en blanco
# - Convertir todo a minúsculas
# Luego contar cuántas profesiones únicas existen en el dataset
cantidad = (
    df["profesion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .nunique()
)

# Mostrar el resultado en pantalla
print(f"Después de normalizar los datos, existen {cantidad} profesiones únicas registradas.")