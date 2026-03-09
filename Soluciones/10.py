import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["profesion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("programador")
    .sum()
)

print(f"Se encontraron {cantidad} registros correspondientes a la profesión 'Programador' tras la limpieza.")