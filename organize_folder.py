import os
import shutil

# Directorio a organizar
dir_path = '/Users/josetabango/Downloads'

# Crea un diccionario para almacenar las extensiones y las carpetas correspondientes
extensions = {
    'jpg': 'imagenes',
    'png': 'imagenes',
    'gif': 'imagenes',
    'pdf': 'documentos',
    'docx': 'documentos',
    'xlsx': 'documentos',
    'mp3': 'musica',
    'wav': 'musica',
    'mp4': 'videos',
    'avi': 'videos',
    'mkv': 'videos',
    'zip': 'comprimidos',
    'dmg': 'instaladores'
}

# Itera sobre los archivos del directorio y mueve cada archivo a la carpeta correspondiente
for filename in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, filename)):
        extension = filename.split('.')[-1].lower()
        if extension in extensions:
            folder_name = extensions[extension]
            folder_path = os.path.join(dir_path, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            shutil.move(os.path.join(dir_path, filename), os.path.join(folder_path, filename))