import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Limpiar la columna 'profesion':
# - Convertir los valores a texto
# - Eliminar espacios en blanco
# - Convertir todo a minúsculas
# Luego contar cuántos registros corresponden a la profesión "programador"
cantidad = (
    df["profesion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("programador")
    .sum()
)

# Mostrar el resultado en pantalla
print(f"Se encontraron {cantidad} registros correspondientes a la profesión 'Programador' tras la limpieza.")