import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Contar los registros donde se cumplen todas las condiciones:
# - La ciudad, normalizada (texto, sin espacios, minúsculas), es "barranquilla"
# - El estado 'activo' representa verdadero (true, 1, si, yes, y, t)
# - El año de nacimiento es mayor a 1980
cantidad = (
    df["ciudad"].astype(str).str.strip().str.lower().eq("barranquilla")
    &
    df["activo"].astype(str).str.strip().str.lower().isin(["true","1","si","yes","y","t"])
    &
    pd.to_datetime(df["fecha_nacimiento"], errors="coerce").dt.year.gt(1980)
).sum()

# Mostrar el resultado en pantalla
print(f"Se encontraron {cantidad} personas activas que viven en Barranquilla y nacieron después de 1980.")