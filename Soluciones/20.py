import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    pd.to_datetime(df["fecha_nacimiento"], errors="coerce")
    .dt.year
    .between(1990, 2000)
    .sum()
)

print(f"El número de personas nacidas entre 1990 y 2000 (inclusive) es: {cantidad}.")