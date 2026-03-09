import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (
    (pd.Timestamp("2026-02-26") - pd.to_datetime(df["fecha_nacimiento"], errors="coerce")).dt.days
    .floordiv(365)
    .gt(50)
    .sum()
)

print(f"A la fecha 2026-02-26, existen {cantidad} personas con más de 50 años.")