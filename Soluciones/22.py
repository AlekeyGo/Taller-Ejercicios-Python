import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Calcular la edad de cada persona a la fecha 2026-02-26
# - Convertir 'fecha_nacimiento' a datetime, errores se convierten en NaT
# - Restar la fecha de nacimiento de la fecha objetivo
# - Obtener la diferencia en días y dividir entre 365 para aproximar la edad en años
# - Verificar cuáles personas tienen más de 50 años
# - Contar la cantidad de registros que cumplen la condición
cantidad = (
    (pd.Timestamp("2026-02-26") - pd.to_datetime(df["fecha_nacimiento"], errors="coerce")).dt.days
    .floordiv(365)
    .gt(50)
    .sum()
)

# Mostrar el resultado en pantalla
print(f"A la fecha 2026-02-26, existen {cantidad} personas con más de 50 años.")