import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (df["email"] != df["email"].str.strip()).sum()

print(f"Se identificaron {cantidad} registros cuyo campo email contiene espacios adicionales.")