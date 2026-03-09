import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["activo"]
    .astype(str)
    .str.strip()
    .str.lower()
    .isin(["true","1","si","yes","y","t"])
    .sum()
)

print(f"Después de normalizar el campo 'activo', {cantidad} registros tienen un valor considerado verdadero.")