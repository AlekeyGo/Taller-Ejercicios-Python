import pandas as pd
datos = pd.read_csv('data/personas.csv')
solucion = (~datos["id"].astype(str).str.isnumeric()).sum()
print("¿Cuántas filas tienen el campo id con caracteres no numéricos? RESPUESTA:", solucion)