import pandas as pd

df = pd.read_csv("data/personas.csv")

minimo = pd.to_numeric(df["salario"], errors="coerce").min()

print(f"El salario mínimo encontrado tras la limpieza del dataset es: {minimo:.2f}.")