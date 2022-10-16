import getpass
import os
from instagrapi import Client


def credentials():
    try:
        file = open("./credentials/credentials.txt", "w")
    except:
        print("No se encontró el archivo credentials.txt")
    user = input("Usuario: ")
    password = getpass.getpass("Contraseña: ")
    file.writelines(user+"\n"+password)
    file.close()

def info(cl: Client):
    print("Informacion de la cuenta")
    x = cl.account_info().username
    print(x)