import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Convertir la columna 'fecha_nacimiento' a tipo datetime
# errors="coerce" convierte fechas inválidas en NaT
# Luego extraer el año y verificar cuáles registros corresponden a personas nacidas antes de 1960
# Finalmente contar la cantidad de registros que cumplen la condición
cantidad = (
    pd.to_datetime(df["fecha_nacimiento"], errors="coerce")
    .dt.year
    .lt(1960)
    .sum()
)

# Mostrar el resultado en pantalla
print(f"La cantidad de personas nacidas antes del año 1960 es: {cantidad}.")