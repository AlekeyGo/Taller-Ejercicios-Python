import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Normalizar la columna 'activo':
# - Convertir los valores a texto
# - Eliminar espacios en blanco
# - Convertir todo a minúsculas
# Luego verificar cuáles valores representan un estado "verdadero"
# (true, 1, si, yes, y, t) y contarlos
cantidad = (
    df["activo"]
    .astype(str)
    .str.strip()
    .str.lower()
    .isin(["true","1","si","yes","y","t"])
    .sum()
)

# Mostrar el resultado en pantalla
print(f"Después de normalizar el campo 'activo', {cantidad} registros tienen un valor considerado verdadero.")