from instagrapi import Client

cl = Client()
def downloadMedia(cl: Client, so: str):
    urlvideo = input("Ingresa el url del video: ")
    media_id = cl.media_pk_from_url(urlvideo)
    # Download the media
    if so == 'l':
        folderDownload = "/home/asdex/Escritorio/videos/itsjustme/downloads/"
    elif so == 'w':
        folderDownload = "C:/Users/asdex/Videos/itsjustme/downloads/"
    cl.clip_download(media_id, folder=folderDownload)
    print("Descargado")