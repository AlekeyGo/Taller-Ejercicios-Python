import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Convertir la columna 'salario' a valores numéricos
# errors="coerce" transforma valores inválidos en NaN
# Luego obtener el salario máximo entre los valores válidos
maximo = pd.to_numeric(df["salario"], errors="coerce").max()

# Mostrar el resultado en pantalla con dos decimales
print(f"El salario máximo registrado después de limpiar los datos es: {maximo:.2f}.")