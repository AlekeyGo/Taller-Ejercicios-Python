import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Convertir la columna 'fecha_nacimiento' a tipo datetime usando el formato AAAA-MM-DD
# errors="coerce" convierte fechas inválidas en NaT
# Luego contar cuántos registros no pudieron convertirse (NaT)
cantidad = pd.to_datetime(df["fecha_nacimiento"], format="%Y-%m-%d", errors="coerce").isna().sum()

# Mostrar el resultado en pantalla
print(f"Se encontraron {cantidad} registros con formato de fecha diferente a AAAA-MM-DD o inválido.")