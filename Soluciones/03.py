import pandas as pd

RUTA_ARCHIVO = 'data/personas.csv'

datos = pd.read_csv(RUTA_ARCHIVO)

def decifrar_palabra(palabra_cifrada):
    import codecs
    nueva_palabra = codecs.decode(palabra_cifrada, 'rot_13')
    return nueva_palabra
datos['nombre_decifrado'] = datos['nombre_cifrado'].apply(decifrar_palabra)
condicion = datos['nombre_decifrado'] == 'Juan'
print('Juan aparece: ', datos[condicion].shape[0])