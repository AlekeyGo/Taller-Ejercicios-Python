import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["activo"]
    .astype(str)
    .str.strip()
    .str.lower()
    .isin(["false","0","no","f","n"])
    .sum()
)

print(f"Luego de la normalización, {cantidad} registros presentan el campo 'activo' como falso.")