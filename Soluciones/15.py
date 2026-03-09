import pandas as pd

df = pd.read_csv("data/personas.csv")

maximo = pd.to_numeric(df["salario"], errors="coerce").max()

print(f"El salario máximo registrado después de limpiar los datos es: {maximo:.2f}.")