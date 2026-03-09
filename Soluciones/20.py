import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Convertir la columna 'fecha_nacimiento' a tipo datetime
# errors="coerce" transforma fechas inválidas en NaT
# Luego extraer el año y verificar cuáles registros están entre 1990 y 2000 (inclusive)
# Finalmente contar la cantidad de registros que cumplen la condición
cantidad = (
    pd.to_datetime(df["fecha_nacimiento"], errors="coerce")
    .dt.year
    .between(1990, 2000)
    .sum()
)

# Mostrar el resultado en pantalla
print(f"El número de personas nacidas entre 1990 y 2000 (inclusive) es: {cantidad}.")