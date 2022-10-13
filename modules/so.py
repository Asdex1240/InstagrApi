def worl():
    bucle = True
    while bucle:
        so = input('Windows o Linux? (w/l): ')
        if(so == 'w' or so == 'l'):
            bucle = False
        else:
            print("Opcion no valida")
            bucle = True
    return so