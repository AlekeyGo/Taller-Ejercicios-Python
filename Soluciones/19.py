import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = pd.to_datetime(df["fecha_nacimiento"], format="%Y-%m-%d", errors="coerce").isna().sum()

print(f"Se encontraron {cantidad} registros con formato de fecha diferente a AAAA-MM-DD o inválido.")