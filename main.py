from modules.login import login
from modules.interaction import *
from modules.credentials import *
from modules.download import downloadMedia
from modules.dir import *
from modules.upload import *
from modules.menu import menu
from instagrapi import Client

cl = Client()

def main():
    path = './media'
    if(os.path.exists(path) == False):
        createDir(path)
    
    if(os.path.exists('./credentials/') == False):
        path = './credentials'
        createCredentials(path)

    cl = login()
    while cl == False:
        credentials()
        cl = login()

    opcion = menu()

    if opcion == 0:
        print("Saliendo...")
        exit()
    elif opcion == 1:
        like_hastag(cl)
    elif opcion == 2:
        upload(cl, path)
    elif opcion == 3:
        info(cl)
    elif opcion == 4:
        hashtag = input("Ingresa el hashtag: ")
        like_automatico(cl, hashtag)
    elif opcion == 5:
        downloadMedia(cl, path)
    else:
        print("Opcion invalida")
        main()
    



main()