import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Normalizar la columna 'activo':
# - Convertir los valores a texto
# - Eliminar espacios en blanco
# - Convertir todo a minúsculas
# Luego verificar cuáles valores representan un estado "falso"
# (false, 0, no, f, n) y contarlos
cantidad = (
    df["activo"]
    .astype(str)
    .str.strip()
    .str.lower()
    .isin(["false","0","no","f","n"])
    .sum()
)

# Mostrar el resultado en pantalla
print(f"Luego de la normalización, {cantidad} registros presentan el campo 'activo' como falso.")