from instagrapi import Client
import random
cl = Client()
def like_hastag(x: Client):
    cl = x
    hashtag = input("Ingresa el hashtag: ")
    elegir = bool(input("Deseas comentar post? (True/False): "))
    amount = int(input("Ingresa la cantidad de likes (Máximo 15): "))
    #Si el amount es mayor a 15, corre riesgo de ban
    while(amount > 15):
        amount = int(input("Ingresa la cantidad de likes (Máximo 15): "))
    
    comments = ["Nice!", "Cool!", "Awesome!"]
    medias = cl.hashtag_medias_recent(hashtag, amount)
    for i, media in enumerate(medias):
        cl.media_like(media.pk)
        print(f"Numero de likes dados: {i+1} para el hashtag {hashtag}")
        if elegir == True:
            if i % 5 == 0:
                cl.user_follow(media.user.pk)
                print(f"Usuario seguido {media.user.username}")
                comment = random.choice(comments)
                cl.media_comment(media.id, comment)
                print(f"Comentamos '{comment}' en el post {i+1}")

def like_automatico(cl: Client, hashtag: str):
    
    comments = ["Nice!", "Cool!", "Awesome!"]
    medias = cl.hashtag_medias_recent(hashtag, 15)
    for i, media in enumerate(medias):
        cl.media_like(media.pk)
        print(f"Numero de likes dados: {i+1} para el hashtag {hashtag}")
        if i % 5 == 0:
            cl.user_follow(media.user.pk)
            print(f"Usuario seguido {media.user.username}")
            comment = random.choice(comments)
            cl.media_comment(media.id, comment)
            print(f"Comentamos '{comment}' en el post {i+1}")