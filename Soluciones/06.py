import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Limpiar la columna 'ciudad':
# - Convertir los valores a texto
# - Eliminar espacios en blanco
# - Convertir todo a minúsculas
# - Reemplazar la tilde en "á" para evitar problemas al comparar
# Luego contar cuántos registros corresponden a "bogota"
cantidad = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("á", "a", regex=False)
    .eq("bogota")
    .sum()
)

# Mostrar el resultado en pantalla
print(f"Después de limpiar los datos, existen {cantidad} registros correspondientes a la ciudad de Bogotá.")