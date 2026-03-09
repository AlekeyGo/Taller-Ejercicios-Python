import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["nombre_cifrado"]
    .apply(lambda x: codecs.decode(str(x), "rot_13"))
    .str.strip()
    .str.lower()
    .eq("ana")
    &
    df["profesion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("medico")
).sum()

print(f"Existen {cantidad} registros donde el nombre es 'Ana' y la profesión corresponde a 'Medico'.")