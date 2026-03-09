import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["profesion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .nunique()
)

print(f"Después de normalizar los datos, existen {cantidad} profesiones únicas registradas.")