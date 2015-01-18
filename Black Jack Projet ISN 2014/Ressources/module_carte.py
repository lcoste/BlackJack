from random import*

##Module qui s'occupe de la gestion des cartes

def melange():      #Permet de melanger et ainsi avoir une pille de carte
    global pille
    pille=[]        #Notre pille de carte
    while len(pille)!=312:      #On dispose de 6 jeu de carte
        x=randrange(52)
        if pille.count(x)<6:
            pille.append(x)


def tirer():        #Lorsque nous tirons une carte
    global pille
    return pille.pop(0)
