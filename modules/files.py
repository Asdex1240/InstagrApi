import pathlib
import shutil
import os
from os import remove

# Funciones para Reels
def deletePics(files, path):
    for file in files:
        extension = pathlib.Path(path+'/'+file)
        if(extension.suffix == '.jpg'):
            remove(extension)

def moveReeltoUpload(path):
    try:
        shutil.move(f'{path}', f'{path}/video/upload')

    except Exception as e:
        print("Error al mover el archivo ->", e)

def videoArray(path):
    files = os.listdir(path)
    return files
