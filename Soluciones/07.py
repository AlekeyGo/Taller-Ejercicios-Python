import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("í", "i", regex=False)
    .eq("medellin")
    .sum()
)

print(f"Después del proceso de limpieza, la ciudad de Medellín tiene {cantidad} registros asociados.")