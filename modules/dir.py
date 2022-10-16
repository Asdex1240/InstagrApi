from ast import Str
import os

def createDir(path: str):
    os.mkdir(path)
    os.mkdir(f'{path}/img')
    os.mkdir(f'{path}/img/noupload')
    os.mkdir(f'{path}/img/upload')
    os.mkdir(f'{path}/video/')
    os.mkdir(f'{path}/video/noupload')
    os.mkdir(f'{path}/video/upload')
    os.mkdir(f'{path}/downloads')
    print('Carpetas creadas')

def createCredentials(path: str):
    os.mkdir(path)
    file = open(f'{path}/credentials.txt', 'w')
    file.close()
    print('Archivo credentials.txt creado')
