from instagrapi import Client
def login():
    cl = Client()
    
    with open('./credentials/credentials.txt') as file_object:
        leer = file_object.readlines()
        try:
            cl.login(leer[0],leer[1])
            return cl
        except:
            print("Credenciales incorrectas o vacias")
            return False
    