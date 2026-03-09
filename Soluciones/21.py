import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    pd.to_datetime(df["fecha_nacimiento"], errors="coerce")
    .dt.year
    .lt(1960)
    .sum()
)

print(f"La cantidad de personas nacidas antes del año 1960 es: {cantidad}.")