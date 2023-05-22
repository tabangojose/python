
import pytesseract
from PIL import Image

# Ruta de la imagen que deseas convertir a texto
ruta_imagen = '/Users/josetabango/Documents/1.png'

# Carga la imagen
imagen = Image.open(ruta_imagen)

# Convierte la imagen a texto
texto = pytesseract.image_to_string(imagen, lang='spa')

# Ruta del archivo de texto que deseas crear
ruta_archivo = '/Users/josetabango/Documents/textConvert.txt'

# Escribe el texto en el archivo
with open(ruta_archivo, mode='w', encoding='utf-8') as archivo:
    archivo.write(texto)