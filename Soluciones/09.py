import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["profesion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("ingeniero")
    .sum()
)

print(f"El número de registros cuya profesión es 'Ingeniero' después de limpiar los datos es: {cantidad}.")