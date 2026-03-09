import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["apellido"] = df["apellido_cifrado"].apply(
    lambda x: codecs.decode(str(x), "rot_13")
).str.strip()

resultado = df["apellido"].value_counts().head(1)

print(f"El apellido más frecuente es {resultado.index[0]} y aparece {resultado.iloc[0]} veces.")