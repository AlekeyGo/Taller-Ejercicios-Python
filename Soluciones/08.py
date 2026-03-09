import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .nunique()
)

print(f"Luego de normalizar los nombres de ciudad, existen {cantidad} ciudades únicas en el dataset.")