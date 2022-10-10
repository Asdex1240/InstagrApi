from modules.login import login
from modules.interaction import *
from modules.credentials import *
from modules.so import worl
from modules.download import downloadMedia
from modules.upload import *
from modules.menu import menu
from instagrapi import Client

cl = Client()

def main():

    cl = login()
    while cl == False:
        credentials()
        cl = login()
    so = worl()

    opcion = menu()

    if opcion == 0:
        print("Saliendo...")
        exit()
    elif opcion == 1:
        like_hastag(cl)
    elif opcion == 2:
        upload(cl)
    elif opcion == 3:
        info(cl)
    elif opcion == 4:
        hashtag = input("Ingresa el hashtag: ")
        like_automatico(cl, hashtag)
    elif opcion == 5:
        downloadMedia(cl, so)
    else:
        print("Opcion invalida")
        main()
    



main()