import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

cantidad = (
    df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), "rot_13")).str.strip().str.lower().eq("carlos")
    &
    df["ciudad"].astype(str).str.strip().str.lower().eq("cali")
).sum()

print(f"Se encontraron {cantidad} registros con nombre 'Carlos' que viven en la ciudad de Cali.")