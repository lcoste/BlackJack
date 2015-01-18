import module_carte as carte
from class_joueur import*
from class_jeu import*
                    
def jeu():              #Fonction a appeler pour debuter le jeu
    print("JEU")            ###A Enlever plus tard###
    global list_joueur,Croupier,index,repetition,recursion,fen           #nb=nombre d'adversaire entre 0 et 4
    nb=fen[3]-1
    carte.melange()         
    repetition=1
    recursion=False
    Croupier=Jeu(None)      #Creation du croupier qui est un objet Jeu
    Croupier.points()
    list_joueur=[0,0,0,0]      #Creation des joueurs
    for i in range(nb):         #0=Pas de joueur
        if nb<=2:
            list_joueur[i]=Joueur(fen[1])
        else:
            list_joueur[i]=Joueur(fen[1])
    list_joueur.insert(2,Joueur(fen[1]))          #Le vrai joueur sera toujours au rang 2
    index=0
    etape_parie()                           #On lance les paries




def etape_parie():                          #Fonction a appeler pour recommencer le jeux avec le meme argent et joueurs
    global index,list_joueur,Croupier
    print("PARIE",index)

    
    if index<5:
        if index==2 and list_joueur[index]!=0:      #Ce que nous jouons si nous somme toujours dans le jeu
            #Mettre animation et image pour parier
            print("parie svp")
            interface.message.configure(text="Nouvelle partie  -  Pariez S.V.P")
            interface.miser()
            ##Insere: Apparition bouton "jetons" (tout ce qui sont disponible par rapport a notre argent actuelle)##
            appel_parie(interface.mise)  ##On attend que le joueur rentre une valeur##
        else:
            if list_joueur[index]!=0:               #Ce que l'IA fait
                appel_parie()
            else:
                index+=1
                etape_parie()
                
    else:
        #Verification de blackjack
        for i in range(5):
            if list_joueur[i]!=0:
                if i==2:##Inserer: envoyer carte au joueur i (2 cartes: list_joueur[i].jeu_de_carte[0].cartes[0] etlist_joueur[i].jeu_de_carte[0].cartes[1])##
                    interface.carte(list_joueur[2].jeu_de_carte[0].cartes[0]%4,(list_joueur[2].jeu_de_carte[0].cartes[0]//4)+1)
                    interface.carte(list_joueur[2].jeu_de_carte[0].cartes[1]%4,(list_joueur[2].jeu_de_carte[0].cartes[1]//4)+1)
                    interface.configure_point_joueur(list_joueur[2].jeu_de_carte[0].pts) 
                else:
                    interface.carte_joueur(i,list_joueur[i].jeu_de_carte[0].cartes[0]%4,(list_joueur[i].jeu_de_carte[0].cartes[0]//4)+1)
                    interface.carte_joueur(i,list_joueur[i].jeu_de_carte[0].cartes[1]%4,(list_joueur[i].jeu_de_carte[0].cartes[1]//4)+1)
                    interface.configure_points(i,list_joueur[i].jeu_de_carte[0].pts)
                if list_joueur[i].blackjack:
                    #BlackJack
                    print("BLACKJACK",i)
                    interface.info_blackjack(i)
                    interface.configure_message(i,"BLACKJACK")
                    interface.message.configure(text="Blackjack pour le joueur "+str(i))
                    if i==2:
                        interface.movement_argent("gagnant")##Inserer: Joueur i blackjack##
                    list_joueur[i].argent+=(list_joueur[i].jeu_de_carte[0].bet)*2.5
                    
        temp=Croupier.cartes[0]
        interface.carte_croupier(temp%4,(temp//4)+1) ##Inserer: Envoyer carte au Croupier##
        temp=(temp//4)+1
        if temp>10:
            temp=10
        elif temp==1:
            temp=11
        interface.configure_point_croupier(temp)
        temp=Croupier.cartes[1]
        interface.carte_croupier(temp%4,(temp//4)+1)
        index=0
        print("Croupier",Croupier.cartes)
        if (Croupier.cartes[0])//4==0:              #Si la 1er carte du croupier est un as alors on demande si les joueurs veulent une assurance
            etape_assurance()
        else:
            etape_jeu()

            

def appel_parie(montant=1):                 #Fonction a appeler lorsque nous confirmerons notre mise
    global index,list_joueur,interface               #En argument notre mise
    
    if index==2 and list_joueur[index]!=0:
        list_joueur[index].en_jeu==True
        list_joueur[index].play(montant)
        interface.configure_argent(list_joueur[2].argent)
    else:
        list_joueur[index].IA_parie()
        interface.configure_mises(index,list_joueur[index].jeu_de_carte[0].bet)
        interface.configure_argent_joueurs(index,list_joueur[index].argent)

        
    index+=1
    etape_parie()

    

def etape_assurance():                  #etape du jeu qui verifie qui veut une assurance
    global list_joueur,Croupier,index
    print("ASSURANCE",index)
    
    if index<5:
        if index==2 and list_joueur[index]!=0 and list_joueur[index].en_jeu:
            interface.message.configure(text="As pour le croupier - Voulez vous une assurance?")
            interface.assurance_oui_non()   ##Inserer: apparition bouton "assurance", "pas assurance"##
            print("assurance ou pas")
            #return interface.assurance  #On attend une reponse du joueur s'il veut une assurance
            appel_assurance(interface.assurance)
        else:
            if list_joueur[index]!=0 and list_joueur[index].en_jeu:
                appel_assurance()
            else:
                index+=1
                etape_assurance()
                
    else:
        if Croupier.pts!=21:
            print("perte de l'assurance")
            ##Inserer: Envoyer l'assurance au Croupier(juste l'assurance)##
        index=0
        etape_jeu()

        

def appel_assurance(choix=False):           #A appeler lorsque le joueur aura fait un choix
    global list_joueur,index                #En argument: True=On prend assurance / False=On prend pas
    if index==2 and list_joueur[index]!=0 and choix:
        list_joueur[2].assurance()
        interface.configure_argent(list_joueur[2].argent)
    elif index!=2 and list_joueur[index]!=0:
        list_joueur[index].IA_assurance()
    index+=1
    etape_assurance()

    

def etape_jeu():                #Etape on le jeu se deroule
    global list_joueur,index,repetition,Croupier,fen
    print("ETAPE_JEU",index)

        
    if index < 5:
        
        if index==2 and list_joueur[index]!=0:
            print("cartes",list_joueur[2].jeu_de_carte[0].cartes)
            list_joueur[2].jeu_de_carte[0].points()
            print(list_joueur[2].jeu_de_carte[0].pts)
            print("argent",list_joueur[2].argent)
            print("parie",list_joueur[2].jeu_de_carte[0].bet)
            print(list_joueur[2].en_jeu)
            if list_joueur[2].en_jeu==False:                #On verifie si n a tout jouer
                if len(list_joueur[index].jeu_de_carte)>1:
                    if repetition < len(list_joueur[index].jeu_de_carte):
                        repetition+=1
                        list_joueur[index].jeu_de_carte.append(list_joueur[index].jeu_de_carte.pop(0))
                        if index==2:
                            interface.split_movement(list_joueur[2].jeu_de_carte[1].cartes,list_joueur[2].jeu_de_carte[0].cartes)#split mouvement
                            ##list_joueur[index].jeu_de_carte[1].cartes
                            interface.configure_point_joueur(list_joueur[2].jeu_de_carte[1].pts)
                        list_joueur[index].en_jeu=True
                        etape_jeu()
                    else:
                        repetition=1
                        index+=1
                        etape_jeu()
                else:
                    repetition=1
                    index+=1
                    etape_jeu()
            elif list_joueur[2].en_jeu==True:             #On verifie ce que nous pouvons faire / Rendre les boutons plus ou moins disponibles
                temp=0
                interface.bouton_appa("bouton_aide")
                if fen[3]>3:
                    interface.configure_message(3,"-")
                if fen[3]>4:
                    interface.configure_message(4,"-")
                if ((list_joueur[index].jeu_de_carte[0].cartes[0])//4==(list_joueur[index].jeu_de_carte[0].cartes[1])//4 or ((list_joueur[index].jeu_de_carte[0].cartes[0])//4 >=9 and(list_joueur[index].jeu_de_carte[0].cartes[1])//4>=9)) and (len(list_joueur[index].jeu_de_carte)==1 and len(list_joueur[index].jeu_de_carte[0].cartes)==2):
                    interface.bouton_appa("bouton_split")   ##Inserer: apparition bouton "split"##
                    temp=2
                    print ("On peut spliter")
                if len(list_joueur[index].jeu_de_carte[0].cartes)==2:
                    interface.bouton_appa("bouton_double")  ##Inserer: apparition bouton "double"##
                    temp=temp+1
                    print("On peut doubler")
                if temp==1:
                    interface.message.configure(text="Vous pouver hiter, stayer ou doubler")
                elif temp==2:
                    interface.message.configure(text="Vous pouver hiter, stayer ou spliter")
                elif temp==3:
                    interface.message.configure(text="Vous pouver hiter, stayer, doubler ou spliter")
                else:
                    interface.message.configure(text="Vous pouver hiter ou stayer")
                interface.bouton_appa("bouton_hit") ##Inserer: apparition bouton "hit", "stay"##
                interface.bouton_appa("bouton_stand")
                print("On peut hiter ou stayer")
                interface.action_bouton()
                #return interface.bouton_valeur  ##Tout c'est boutons appel appel_jeu(choix) avec en argument S D H ou R##
                interface.bouton_disp("bouton_hit")
                interface.bouton_disp("bouton_stand")
                interface.bouton_disp("bouton_double")
                interface.bouton_disp("bouton_split")
                interface.bouton_disp("bouton_aide")
                appel_jeu(interface.bouton_valeur)
                

        else:
            if list_joueur[index]!=0 and list_joueur[index].en_jeu:
                print(list_joueur[index].jeu_de_carte[0].cartes)
                appel_jeu()
            else:
                index+=1
                etape_jeu()
                
    else:
        index=0
        etape_croupier()

        

def appel_jeu(option="R"):          #A appeler lorsqon aure fait un choix
    global list_joueur,index        #En argument notre choix
    
    if index==2 and list_joueur[index]!=0:
        if option=="S" and (((list_joueur[index].jeu_de_carte[0].cartes[0])//4==(list_joueur[index].jeu_de_carte[0].cartes[1])//4 or ((list_joueur[index].jeu_de_carte[0].cartes[0])//4 >=9 and(list_joueur[index].jeu_de_carte[0].cartes[1])//4>=9)) and (len(list_joueur[index].jeu_de_carte)==1 and len(list_joueur[index].jeu_de_carte[0].cartes)==2)):             #"S" pour un split
            interface.message.configure(text="SPLIT")
            list_joueur[2].split()
            interface.configure_argent(list_joueur[2].argent)
            temp=len(list_joueur[2].jeu_de_carte[0].cartes)-1
            temp=list_joueur[2].jeu_de_carte[0].cartes[temp]
            interface.split(list_joueur[2].jeu_de_carte[0].cartes[0],list_joueur[2].jeu_de_carte[1].cartes[0],list_joueur[2].jeu_de_carte[0].cartes[1],list_joueur[2].jeu_de_carte[1].cartes[1])
            interface.configure_point_joueur(list_joueur[2].jeu_de_carte[0].pts)
            ##Inserer: Envoyer carte au joueur 2 et separer en 2 jeux de carte##
        elif option=="D":           #"D" pour un double
            interface.message.configure(text="DOUBLE")
            list_joueur[2].double()
            interface.configure_argent(list_joueur[2].argent)
            temp=len(list_joueur[2].jeu_de_carte[0].cartes)-1
            temp=list_joueur[2].jeu_de_carte[0].cartes[temp]
            interface.carte_double(temp%4,(temp//4)+1)##Inserer: Envoyer carte au joueur 2##
            interface.configure_point_joueur(list_joueur[2].jeu_de_carte[0].pts)
        elif option=="H":           #"H" pour tirer une carte
            interface.message.configure(text="HIT")
            list_joueur[2].hit()
            temp=len(list_joueur[2].jeu_de_carte[0].cartes)-1
            temp=list_joueur[2].jeu_de_carte[0].cartes[temp]
            interface.carte(temp%4,(temp//4)+1) ##Inserer: Envoyer carte au joueur 2##
            interface.configure_point_joueur(list_joueur[2].jeu_de_carte[0].pts)
        elif option=="R":           #"R" pour s'arreter
            interface.message.configure(text="STAND")
            list_joueur[2].stay()
        elif option=="A":
            temp=stat()
            interface.info_statistique(temp)
            
        etape_jeu()
        
        
    elif list_joueur[index]!=0:
        i=0
        jeu_carte_split=0
        choix=False
        
        while i < len(list_joueur[index].jeu_de_carte):     #Pour l'IA on verifie tout ce qu'il peut faire
            print("boucle",i)
            if ((list_joueur[index].jeu_de_carte[i].cartes[0])//4==(list_joueur[index].jeu_de_carte[i].cartes[1])//4 or ((list_joueur[index].jeu_de_carte[i].cartes[0])//4 >=9 and(list_joueur[index].jeu_de_carte[i].cartes[1])//4>=9)) and (len(list_joueur[index].jeu_de_carte)==1 and len(list_joueur[index].jeu_de_carte[i].cartes)==2):
                choix=list_joueur[index].IA_split()     #On verifie s'il veut split
                if choix:
                    print("prise de split")
                    interface.configure_message(index,"SPLIT")
                    interface.split_joueur(index,list_joueur[index].jeu_de_carte[0].cartes[0],list_joueur[index].jeu_de_carte[1].cartes[0],list_joueur[index].jeu_de_carte[0].cartes[1],list_joueur[index].jeu_de_carte[1].cartes[1])
                    jeu_carte_split=1
                    ##Inserer: Envoyer cartes au joueur index et separer en index jeux de carte##
            if len(list_joueur[index].jeu_de_carte[i].cartes)==2 and choix==False:
                choix=list_joueur[index].IA_double(i)   #Sinon on verifie s'il veut split
                if choix:
                    print("prise de double")
                    interface.configure_message(index,"DOUBLE")
                    temp=len(list_joueur[index].jeu_de_carte[0].cartes)-1
                    temp=list_joueur[index].jeu_de_carte[0].cartes[temp]
                    interface.carte_double_joueur(index,temp%4,(temp//4)+1)##Inserer: Envoyer carte au joueur index##
            if choix==False:
                choix=list_joueur[index].IA_hit(i)        #Sinon on verifie s'il veut hit et sinon il s'arrete
                if choix:
                    print("prise de hit")
                    interface.configure_message(index,"HIT")
                    temp=len(list_joueur[index].jeu_de_carte[0].cartes)-1
                    temp=list_joueur[index].jeu_de_carte[0].cartes[temp]
                    interface.carte_joueur(index,temp%4,(temp//4)+1)##Inserer: Envoyer carte au joueur index##
            choix=False
            list_joueur[index].jeu_de_carte[i].points()
            if list_joueur[index].jeu_de_carte[i].pts>=21:          ###A Enlever plus tard###
                print("poulet!!!",list_joueur[index].jeu_de_carte[i].pts)
            if list_joueur[index].jeu_de_carte[i].pts>=21 or list_joueur[index].en_jeu==False:
                list_joueur[index].en_jeu=True
                i+=1
                if i==1 and jeu_carte_split:
                    interface.split_movement_joueur(index,list_joueur[index].jeu_de_carte[0].cartes,list_joueur[index].jeu_de_carte[1].cartes)
            interface.configure_points(index,list_joueur[index].jeu_de_carte[0].pts)
        if jeu_carte_split==1:
            interface.fin_split_reconfigure(index)
            print("____________________________________________________________")
        index+=1
        etape_jeu()

        

def etape_croupier():       #Etape ou le croupier joue
    print("CROUPIER")
    global Croupier,list_joueur
    choix=False
    for i in range(5):              #On verifie si sa vaut la peine de jouer
        if list_joueur[i]!=0:       #Si tout les joueurs sont au-dessus de 21 alors il a pas besoin de jouer
            for j in range(len(list_joueur[i].jeu_de_carte)):
                list_joueur[i].jeu_de_carte[j].points()
                if list_joueur[i].jeu_de_carte[j].pts<=21:
                    choix=True
                    
    while Croupier.pts<17 and choix:        #Tant qu'il est en dessous de 17 il continue a tirer une carte
        Croupier.cartes.append(carte.tirer())
        Croupier.points()
        interface.configure_point_croupier(Croupier.pts)
        
    print("Croupier",Croupier.cartes)
    print("Croupier.pts",Croupier.pts)
    interface.configure_point_croupier(Croupier.pts)
    interface.message.configure(text="Le Croupier a : "+str(Croupier.pts)+" points")
    etape_paie()

    

def etape_paie():           #Etape ou la paie se fait et on relance le prochain jeu et les mises
    print("PAIE")
    global list_joueur,Croupier,recursion,fen
    Croupier.points()
    
    for i in range(5):
        if list_joueur[i]!=0 and list_joueur[i].blackjack==False:
            for j in range(len(list_joueur[i].jeu_de_carte)):
                list_joueur[i].jeu_de_carte[j].points()
                if list_joueur[i].jeu_de_carte[j].pts>21:
                    if i==2:
                        interface.movement_argent()##Inserer: Croupier gagne##
                    print("Perdu",i,j)
                    interface.configure_message(i,"PERD")
                elif Croupier.pts>21:
                    list_joueur[i].argent+=list_joueur[i].jeu_de_carte[j].bet*2
                    if i==2:
                        interface.movement_argent("gagnant")##Inserer: Joueur i gagne##
                    interface.configure_message(i,"GAGNE")
                    print("Gagner",i,j)
                elif Croupier.pts<list_joueur[i].jeu_de_carte[j].pts:
                    list_joueur[i].argent+=list_joueur[i].jeu_de_carte[j].bet*2
                    if i==2:
                        interface.movement_argent("gagnant")##Inserer: Joueur i gagne##
                    interface.configure_message(i,"GAGNE")
                    print("Gagner",i,j)
                elif Croupier.pts>list_joueur[i].jeu_de_carte[j].pts:
                    if i==2:
                        interface.movement_argent()##Inserer: Croupier gagne##
                    interface.configure_message(i,"PERD")
                    print("Perdu",i,j)
                elif Croupier.pts == list_joueur[i].jeu_de_carte[j].pts:
                    list_joueur[i].argent+=list_joueur[i].jeu_de_carte[j].bet
                    if i==2:
                        interface.movement_argent("gagnant")##Inserer: Push/Egalité##
                    interface.configure_message(i,"EGALITE")
                    print("Push",i,j)
                    
    if index==2 and list_joueur[index]!=0:      ###A Enlever plus tard
        print (list_joueur[2].argent)
        
    for i in range(5):      #On cherche les joueurs qui n'on plus d'argent ou qui atteint l'objectifs
        if list_joueur[i]!=0:
            if list_joueur[i].argent<=0:        #Plus d'argent
                print("PERDANT",i)
                interface.message.configure(text="Le joueur "+str(i)+" a perdu")
                ##Inserer:faire apparaître "le joueur i à perdu" et faire disparaître le joueur de la table##
                list_joueur[i]=0                #Retirer du jeu
            elif list_joueur[i].argent>=fen[2]:       #Objectif peut changer(2000 c'est beaucoup, peut 1300)
                print("WINNER",i)       #Le jeu entier s'arrete si qqun atteint l'objectif
                interface.message.configure(text="Le joueur "+str(i)+" a gagner !")
                list_joueur=[0,0,0,0,0]
                return
            
    Croupier=Jeu(None)      #Remise a zero du croupier
    Croupier.points()       #On ne veut pas qu'il garde les meme cartes
    if len(carte.pille)<=52:        #S'il ne reste plus que 52 cartes alors on melange a nouveau les cartes
        carte.melange()
    interface.configure_argent(list_joueur[2].argent)
    interface.nettoyage()##Inserer: Nettoyer le tapis de jeu##
    if fen[3]>1:
        interface.configure_points(0,0)
        interface.configure_mises(0,0)
        interface.configure_argent_joueurs(0,list_joueur[0].argent)
    if fen[3]>2:
        interface.configure_points(1,0)
        interface.configure_mises(1,0)
        interface.configure_argent_joueurs(1,list_joueur[1].argent)
    if fen[3]>3:
        interface.configure_points(3,0)
        interface.configure_mises(3,0)
        interface.configure_argent_joueurs(3,list_joueur[3].argent)
    if fen[3]>4:
        interface.configure_points(4,0)
        interface.configure_mises(4,0)
        interface.configure_argent_joueurs(4,list_joueur[4].argent)
        
    while list_joueur[2]==0 and list_joueur.count(0)!=5:
        print("#############################BOUCLE DE LA MORT QUI TUE#############################")
        if recursion==False:
            recursion=True
            etape_parie()
        if recursion==True:
            recursion=False
            return

    if list_joueur[2]!=0:
        etape_parie()           #On recommence avec de nouvelles mises
            
        
def stat():
    list_joueur[2].jeu_de_carte[0].points()
    x=21-list_joueur[2].jeu_de_carte[0].pts
    for i in range(4):
        x+=(list_joueur[2].jeu_de_carte[0].cartes.count(i)*10)
    if x>=10:
        return 100
    else:
        total=0
        pille_total=carte.pille
        pille_total.append(Croupier.cartes[1])
        for i in range(4*x):
            total+=pille_total.count(i)
        pourcentage=round((total*100)/(len(pille_total)))
        return pourcentage

        
