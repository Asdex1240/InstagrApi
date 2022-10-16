import getpass
import os
from instagrapi import Client


def credentials():
    
    file = open("./credentials/credentials.txt", "w")
    user = input("Usuario: ")
    password = getpass.getpass("Contraseña: ")
    file.writelines(user+"\n"+password)
    file.close()

def info(cl: Client):
    print("Informacion de la cuenta")
    x = cl.account_info().username
    print(x)