import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Verificar qué registros tienen valores no numéricos en la columna 'salario'
# - astype(str) asegura que todos los valores se traten como texto
# - str.fullmatch(r"\d+") valida que el contenido tenga solo dígitos
# - ~ invierte la condición para identificar los que NO son numéricos
# Luego se cuentan esos registros
cantidad = (~df["salario"].astype(str).str.fullmatch(r"\d+")).sum()

# Mostrar el resultado en pantalla
print(f"Existen {cantidad} registros donde el campo salario contiene caracteres no numéricos.")