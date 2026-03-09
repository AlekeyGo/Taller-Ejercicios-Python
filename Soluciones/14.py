import pandas as pd

df = pd.read_csv("data/personas.csv")

promedio = pd.to_numeric(df["salario"], errors="coerce").mean()

print(f"El salario promedio después del proceso de limpieza es: {promedio:.2f}.")