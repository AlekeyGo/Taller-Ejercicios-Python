import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Normalizar la columna 'ciudad':
# - Convertir los valores a texto
# - Eliminar espacios en blanco
# - Convertir todo a minúsculas
# Luego contar cuántas ciudades únicas existen en el dataset
cantidad = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .nunique()
)

# Mostrar el resultado en pantalla
print(f"Luego de normalizar los nombres de ciudad, existen {cantidad} ciudades únicas en el dataset.")