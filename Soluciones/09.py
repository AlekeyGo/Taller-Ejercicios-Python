import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Limpiar la columna 'profesion':
# - Convertir los valores a texto
# - Eliminar espacios en blanco
# - Convertir todo a minúsculas
# Luego contar cuántos registros tienen la profesión "ingeniero"
cantidad = (
    df["profesion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("ingeniero")
    .sum()
)

# Mostrar el resultado en pantalla
print(f"El número de registros cuya profesión es 'Ingeniero' después de limpiar los datos es: {cantidad}.")