import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Filtrar los registros cuya profesión, normalizada (texto, sin espacios, minúsculas), es "ingeniero"
# Agrupar por ciudad normalizada (texto, sin espacios, minúsculas)
# Contar cuántos ingenieros hay por ciudad
# Obtener la ciudad con mayor cantidad de ingenieros
resultado = (
    df[df["profesion"].astype(str).str.strip().str.lower().eq("ingeniero")]
    .groupby(df["ciudad"].astype(str).str.strip().str.lower())
    .size()
    .idxmax()
)

# Obtener la cantidad de ingenieros en esa ciudad
cantidad = (
    df[df["profesion"].astype(str).str.strip().str.lower().eq("ingeniero")]
    .groupby(df["ciudad"].astype(str).str.strip().str.lower())
    .size()
    .max()
)

# Mostrar la ciudad y la cantidad de ingenieros en pantalla
print(f"La ciudad con mayor cantidad de Ingenieros es '{resultado.title()}', con {cantidad} registros.")