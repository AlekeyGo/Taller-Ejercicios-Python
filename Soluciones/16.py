import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Convertir la columna 'salario' a valores numéricos
# errors="coerce" convierte valores inválidos en NaN
# Luego obtener el salario mínimo entre los valores válidos
minimo = pd.to_numeric(df["salario"], errors="coerce").min()

# Mostrar el resultado en pantalla con dos decimales
print(f"El salario mínimo encontrado tras la limpieza del dataset es: {minimo:.2f}.")