import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Normalizar la columna 'profesion' y convertir 'salario' a numérico
# Luego agrupar por profesión y calcular el salario promedio
promedios = (
    df.assign(
        profesion=df["profesion"].astype(str).str.strip().str.lower(),
        salario=pd.to_numeric(df["salario"], errors="coerce")
    )
    .groupby("profesion")["salario"]
    .mean()
)

# Obtener la profesión con el salario promedio más alto y su valor
profesion = promedios.idxmax()
promedio = promedios.max()

# Mostrar el resultado en pantalla con dos decimales
print(f"La profesión con el salario promedio más alto es '{profesion.title()}', con un promedio de {promedio:.2f}.")