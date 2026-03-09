import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Convertir la columna 'salario' a valores numéricos
# errors="coerce" convierte los valores inválidos en NaN
# Luego calcular el promedio de los salarios válidos
promedio = pd.to_numeric(df["salario"], errors="coerce").mean()

# Mostrar el resultado en pantalla con dos decimales
print(f"El salario promedio después del proceso de limpieza es: {promedio:.2f}.")