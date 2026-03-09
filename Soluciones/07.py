import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Limpiar la columna 'ciudad':
# - Convertir los valores a texto
# - Eliminar espacios en blanco
# - Convertir todo a minúsculas
# - Reemplazar la tilde en "í" para evitar problemas al comparar
# Luego contar cuántos registros corresponden a "medellin"
cantidad = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("í", "i", regex=False)
    .eq("medellin")
    .sum()
)

# Mostrar el resultado en pantalla
print(f"Después del proceso de limpieza, la ciudad de Medellín tiene {cantidad} registros asociados.")