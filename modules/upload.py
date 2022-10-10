from instagrapi import Client


def upload(cl: Client):
    client = Client()
    client = cl

    print("1. Subir foto")
    print("2. Subir Reel")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        upload_photo(client)
    elif opcion == 2:
        upload_reel(client)


def upload_photo(cl: Client):
    photo = input("Ingresa nombre de la foto: ")
    caption = input("Ingresa la descripción: ")
    try:
        cl.photo_upload(f"media/{photo}.jpg", caption)
        print("Foto subida con exito!")
    except:
        print("Error al subir la foto")

def upload_reel(cl: Client):
    video = input("Ingresa nombre del video: ")
    caption = input("Ingresa la descripción: ")
    try:
        cl.clip_upload(f"media/{video}.mp4", caption)
        print("Video subido con exito!")
    except:
        print("Error al subir el video")