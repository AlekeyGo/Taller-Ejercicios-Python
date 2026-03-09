import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Contar los registros donde:
# - La profesión, normalizada (texto, sin espacios, minúsculas), es "abogado"
# - El salario, convertido a numérico, es mayor a 10,000,000
cantidad = (
    df["profesion"].astype(str).str.strip().str.lower().eq("abogado")
    &
    pd.to_numeric(df["salario"], errors="coerce").gt(10_000_000)
).sum()

# Mostrar el resultado en pantalla
print(f"Hay {cantidad} registros cuya profesión es 'Abogado' y poseen un salario superior a 10,000,000.")