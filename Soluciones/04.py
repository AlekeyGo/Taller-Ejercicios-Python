import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["nombre"] = df["nombre_cifrado"].astype(str).apply(
    lambda x: codecs.decode(x, "rot_13")
)

df["nombre"] = df["nombre"].str.strip()
resultado = df["nombre"].value_counts().head(1)

nombre = resultado.index[0]
cantidad = resultado.iloc[0]

print(f"El nombre más frecuente es {nombre} y aparece {cantidad} veces.")