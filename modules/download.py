from instagrapi import Client

cl = Client()
def downloadMedia(cl: Client, path: str):
    urlvideo = input("Ingresa el url del video: ")
    media_id = cl.media_pk_from_url(urlvideo)
    # Download the media

    folderDownload = f"{path}/downloads/"
    cl.clip_download(media_id, folder=folderDownload)
    print("Descargado")