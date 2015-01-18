import module_carte as carte
from class_joueur import*
from class_jeu import*
from tkinter import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
from class_graphisme import *
                    
def jeu(option_menu):              #Fonction a appeler pour debuter le jeu
    global list_joueur,Croupier,index,repetition,recursion,fen,interface,rang  #nb=nombre d'adversaire entre 0 et 4
    fen=option_menu
    if fen[1]<1:
        fen[1]=1
    if fen[2]<=fen[1]:
        fen[2]=fen[1]+1
    if fen[3]>=5:
        fen[3]=5
    elif fen[3]<1:
        fen[3]=1
    interface = Graphisme(fen[3],fen[0])
    nb=fen[3]-1
    carte.melange()
    repetition=1
    recursion=False
    rang=[]
    Croupier=Jeu(None)      #Creation du croupier qui est un objet Jeu
    Croupier.points()
    list_joueur=[0,0,0,0]      #Creation des joueurs
    for i in range(nb):         #0=Pas de joueur
        if nb<=2:
            list_joueur[i]=Joueur(fen[1])
        else:
            list_joueur[i]=Joueur(fen[1])
    if fen[3]==5:
        interface.configure_argent_joueurs(0,fen[1])
        interface.configure_argent_joueurs(1,fen[1])
        interface.configure_argent_joueurs(3,fen[1])
        interface.configure_argent_joueurs(4,fen[1])
    elif fen[3]==4:
        interface.configure_argent_joueurs(0,fen[1])
        interface.configure_argent_joueurs(1,fen[1])
        interface.configure_argent_joueurs(3,fen[1])
    elif fen[3]==3:
        interface.configure_argent_joueurs(0,fen[1])
        interface.configure_argent_joueurs(1,fen[1])
    elif fen[3]==2:
        interface.configure_argent_joueurs(0,fen[1])
    list_joueur.insert(2,Joueur(fen[1]))          #Le vrai joueur sera toujours au rang 2
    index=0
    etape_parie()                           #On lance les paries



def etape_parie():                          #Fonction a appeler pour recommencer le jeux avec le meme argent et joueurs
    global index,list_joueur,Croupier
    interface.message.configure(fg="blue")
    if fen[3]>1:
        interface.configure_message(0,"-")
    if fen[3]>2:
        interface.configure_message(1,"-")
    if fen[3]>3:
        interface.configure_message(3,"-")
    if fen[3]>4:
        interface.configure_message(4,"-")
    if index<5:
        if index==2 and list_joueur[index]!=0:      #Ce que nous jouons si nous somme toujours dans le jeu
            interface.message.configure(text="Pariez S.V.P",font=('arial','11','bold'))
            interface.configure_argent(list_joueur[2].argent)
            interface.miser(list_joueur[2].argent)
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
                if i==2:
                    interface.carte(list_joueur[2].jeu_de_carte[0].cartes[0]%4,(list_joueur[2].jeu_de_carte[0].cartes[0]//4)+1)
                    interface.carte(list_joueur[2].jeu_de_carte[0].cartes[1]%4,(list_joueur[2].jeu_de_carte[0].cartes[1]//4)+1)
                    interface.configure_point_joueur(list_joueur[2].jeu_de_carte[0].pts) 
                else:
                    if list_joueur[2]!=0:
                        interface.carte_joueur(i,list_joueur[i].jeu_de_carte[0].cartes[0]%4,(list_joueur[i].jeu_de_carte[0].cartes[0]//4)+1)
                        interface.carte_joueur(i,list_joueur[i].jeu_de_carte[0].cartes[1]%4,(list_joueur[i].jeu_de_carte[0].cartes[1]//4)+1)
                        interface.configure_points(i,list_joueur[i].jeu_de_carte[0].pts)
                if list_joueur[i].blackjack:
                    if list_joueur[2]!=0:
                        interface.info_blackjack(i)
                        interface.message.configure(text="Joueur "+str(i+1)+": Blackjack!!!")
                        interface.configure_message(i,"BLACKJACK")                        
                    if i==2:
                        interface.movement_argent("gagnant")
                        interface.afficher_gagne("joueur")
                    list_joueur[i].argent+=(list_joueur[i].jeu_de_carte[0].bet)*2.5

        if list_joueur[2]!=0:
            temp=Croupier.cartes[0]
            interface.carte_croupier(temp%4,(temp//4)+1)
            temp=(temp//4)+1
            if temp>10:
                temp=10
            elif temp==1:
                temp=11
            interface.configure_point_croupier(temp)
            temp=Croupier.cartes[1]
            interface.carte_croupier(temp%4,(temp//4)+1)
        index=0
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
        if list_joueur[2]!=0:
            interface.configure_mises(index,list_joueur[index].jeu_de_carte[0].bet)
            interface.configure_argent_joueurs(index,list_joueur[index].argent)

        
    index+=1
    etape_parie()


def etape_assurance():                  #etape du jeu qui verifie qui veut une assurance
    global list_joueur,Croupier,index,recursion,rang
    
    if index<5:
        if index==2 and list_joueur[index]!=0 and list_joueur[index].en_jeu:
            if list_joueur[index].argent>=(list_joueur[index].jeu_de_carte[0].bet*0.5):
                interface.message.configure(text="Voulez vous une assurance?")
                interface.assurance_oui_non()#On attend une reponse du joueur s'il veut une assurance
                appel_assurance(interface.assurance)
            else:
                interface.message.configure(text="Vous n'avez pas assez d'argent pour prendre une assurance")
                appel_assurance(False)
        else:
            if list_joueur[index]!=0 and list_joueur[index].en_jeu and (list_joueur[index].argent>=(list_joueur[index].jeu_de_carte[0].bet*0.5)):
                appel_assurance()
            else:
                index+=1
                etape_assurance()
                
    else:
        index=0
        if Croupier.pts!=21:
            if list_joueur[2]!=0 and list_joueur[2].assurance_prise:
                interface.movement_argent_assurance("perdant")
        if Croupier.pts==21:
            if list_joueur[2]!=0:
                temp=Croupier.cartes[1]
                interface.appa_carte_croupier(temp%4,(temp//4)+1)
            for i in range (5):
                if list_joueur[i]!=0:
                    if list_joueur[i].assurance_prise:
                        list_joueur[i].argent+=list_joueur[i].jeu_de_carte[0].bet*1.5
                        if i==2:                        
                            interface.movement_argent("gagnant")
                            interface.movement_argent_assurance("gagnant")
                            interface.afficher_gagne("joueur")
                    elif i==2 and list_joueur[i].assurance_prise==False:
                        interface.movement_argent("perdant")
                        interface.afficher_gagne("croupier")
            for i in range(5):      #On cherche les joueurs qui n'on plus d'argent ou qui atteint l'objectifs
                if list_joueur[i]!=0:
                    if list_joueur[i].argent<=0:        #Plus d'argent
                        interface.gagnant_perdant(i,"PERDANT")
                        rang.append(i)
                        if i==2:
                            interface.nettoyage()
                            interface.caneva.delete(interface.text_nouvelle_partie)
                            if fen[3]!=1:
                                interface.pause_nouvelle_partie()
                        interface.message.configure(text="Le joueur "+str(i+1)+" a perdu",fg="blue")
                        list_joueur[i]=0                
                    elif list_joueur[i].argent>=fen[2]:       #Objectif (fen[2] correspond a la somme a atteindre)
                        #Le jeu entier s'arrete si qqun atteint l'objectif
                        rang=[i]
                        list_joueur=[0,0,0,0,0]
                        interface.nettoyage()
                        interface.caneva.delete(interface.text_nouvelle_partie)
                        interface.gagnant_perdant(i,"GAGNANT")
                        if i==2:
                            showinfo("VICTOIRE", "FELICITATION\nVOUS AVEZ GAGNE !")
                        else:
                            showinfo("VICTOIRE", "LE JOUEUR "+str(i+1)+" A GAGNE !")
                        interface.fenetre.destroy()
                        print("destruction1")
                        return

            if list_joueur.count(0)==5 and fen[3]!=1:
                compteur=fen[3]-1
                temp=""
                classement=1
                while compteur>=0:
                    if rang[compteur]==2:
                        if classement==1:
                            temp=temp+"       "+str(classement)+"er       Vous\n"
                        else:
                            temp=temp+"       "+str(classement)+"eme   Vous\n"
                    else:
                        if classement==1:
                            temp=temp+"       "+str(classement)+"er       Joueur "+str(rang[compteur]+1)+"\n"
                        else:
                            temp=temp+"       "+str(classement)+"ème   Joueur "+str(rang[compteur]+1)+"\n"
                    compteur=compteur-1
                    classement=classement+1
                showinfo("RESULTATS", temp)
                interface.fenetre.destroy()
                print("destruction2")
                return
            elif list_joueur[2]==0 and fen[3]==1:
                showinfo("PERDU", "VOUS AVEZ PERDU !")
                interface.fenetre.destroy()
                print("destruction3")
                return
            Croupier=Jeu(None)      #Remise a zero du croupier
            Croupier.points()       #On ne veut pas qu'il garde les meme cartes
            if len(carte.pille)<52:        #S'il ne reste plus que 52 cartes alors on melange a nouveau les cartes
                carte.melange()
            if list_joueur[2]!=0:
                interface.pause_nouvelle_partie()
                interface.nettoyage()
            if list_joueur[2]!=0:
                interface.configure_argent(list_joueur[2].argent)
            if fen[3]>1:
                if list_joueur[2]!=0:
                    if list_joueur[0]!=0:
                        interface.configure_points(0,0)
                        interface.configure_mises(0,0)
                        interface.configure_argent_joueurs(0,list_joueur[0].argent)
            if fen[3]>2:
                if list_joueur[2]!=0:
                    if list_joueur[1]!=0:
                        interface.configure_points(1,0)
                        interface.configure_mises(1,0)
                        interface.configure_argent_joueurs(1,list_joueur[1].argent)
            if fen[3]>3:
                if list_joueur[2]!=0:
                    if list_joueur[3]!=0:
                        interface.configure_points(3,0)
                        interface.configure_mises(3,0)
                        interface.configure_argent_joueurs(3,list_joueur[3].argent)
            if fen[3]>4:
                if list_joueur[2]!=0:
                    if list_joueur[4]!=0:
                        interface.configure_points(4,0)
                        interface.configure_mises(4,0)
                        interface.configure_argent_joueurs(4,list_joueur[4].argent)
                
            while list_joueur.count(0)!=5:
                if recursion==False:
                    recursion=True
                    etape_parie()
                if recursion==True:
                    recursion=False
                    return

             
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
        
    if index < 5:
        
        if index==2 and list_joueur[index]!=0:
            list_joueur[2].jeu_de_carte[0].points()
            if list_joueur[2].en_jeu==False:                #On verifie si on a tout jouer
                if len(list_joueur[index].jeu_de_carte)>1:
                    if repetition < len(list_joueur[index].jeu_de_carte):
                        repetition+=1
                        list_joueur[index].jeu_de_carte.append(list_joueur[index].jeu_de_carte.pop(0))
                        if index==2:
                            interface.split_movement(list_joueur[2].jeu_de_carte[1].cartes,list_joueur[2].jeu_de_carte[0].cartes)
                            list_joueur[2].jeu_de_carte[0].points()
                            interface.configure_point_joueur(list_joueur[2].jeu_de_carte[0].pts)
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
                interface.bouton_appa("bouton_aide")
                if ((list_joueur[index].jeu_de_carte[0].cartes[0])//4==(list_joueur[index].jeu_de_carte[0].cartes[1])//4 or ((list_joueur[index].jeu_de_carte[0].cartes[0])//4 >=9 and(list_joueur[index].jeu_de_carte[0].cartes[1])//4>=9)) and (len(list_joueur[index].jeu_de_carte)==1 and len(list_joueur[index].jeu_de_carte[0].cartes)==2) and list_joueur[index].argent >= list_joueur[index].jeu_de_carte[0].bet:
                    interface.bouton_appa("bouton_split")
                if len(list_joueur[index].jeu_de_carte[0].cartes)==2 and list_joueur[index].argent >= list_joueur[index].jeu_de_carte[0].bet:
                    interface.bouton_appa("bouton_double")
                interface.message.configure(text="A vous de jouer")
                interface.bouton_appa("bouton_hit")
                interface.bouton_appa("bouton_stand")
                interface.action_bouton()
                ##Tout c'est boutons appel appel_jeu(choix) avec en argument S D H ou R##
                interface.bouton_disp("bouton_hit")
                interface.bouton_disp("bouton_stand")
                interface.bouton_disp("bouton_double")
                interface.bouton_disp("bouton_split")
                interface.bouton_disp("bouton_aide")
                appel_jeu(interface.bouton_valeur)

        else:
            if list_joueur[index]!=0 and list_joueur[index].en_jeu:
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
            list_joueur[2].jeu_de_carte[0].points()
            interface.configure_point_joueur(list_joueur[2].jeu_de_carte[0].pts)
        elif option=="D":           #"D" pour un double
            interface.message.configure(text="DOUBLE")
            list_joueur[2].double()
            interface.configure_argent(list_joueur[2].argent)
            temp=len(list_joueur[2].jeu_de_carte[0].cartes)-1
            temp=list_joueur[2].jeu_de_carte[0].cartes[temp]
            interface.carte_double(temp%4,(temp//4)+1)
            list_joueur[2].jeu_de_carte[0].points()
            interface.configure_point_joueur(list_joueur[2].jeu_de_carte[0].pts)
        elif option=="H":           #"H" pour tirer une carte
            interface.message.configure(text="HIT")
            list_joueur[2].hit()
            temp=len(list_joueur[2].jeu_de_carte[0].cartes)-1
            temp=list_joueur[2].jeu_de_carte[0].cartes[temp]
            interface.carte(temp%4,(temp//4)+1)
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
        selection_jeu_carte=0
        choix=False
        
        while i < len(list_joueur[index].jeu_de_carte):     #Pour l'IA on verifie tout ce qu'il peut faire
            #print("boucle",i)
            if ((list_joueur[index].jeu_de_carte[i].cartes[0])//4==(list_joueur[index].jeu_de_carte[i].cartes[1])//4 or ((list_joueur[index].jeu_de_carte[i].cartes[0])//4 >=9 and(list_joueur[index].jeu_de_carte[i].cartes[1])//4>=9)) and (len(list_joueur[index].jeu_de_carte)==1 and len(list_joueur[index].jeu_de_carte[i].cartes)==2) and list_joueur[index].argent >= list_joueur[index].jeu_de_carte[0].bet:
                choix=list_joueur[index].IA_split()     #On verifie s'il veut split
                if choix:
                    if list_joueur[2]!=0:
                        interface.configure_message(index,"SPLIT")
                        interface.split_joueur(index,list_joueur[index].jeu_de_carte[0].cartes[0],list_joueur[index].jeu_de_carte[1].cartes[0],list_joueur[index].jeu_de_carte[0].cartes[1],list_joueur[index].jeu_de_carte[1].cartes[1])
                    jeu_carte_split=1
            if len(list_joueur[index].jeu_de_carte[i].cartes)==2 and list_joueur[index].argent >= list_joueur[index].jeu_de_carte[0].bet and choix==False:
                choix=list_joueur[index].IA_double(i)   #Sinon on verifie s'il veut double
                if choix:
                    if list_joueur[2]!=0:
                        interface.configure_message(index,"DOUBLE")
                        temp=len(list_joueur[index].jeu_de_carte[selection_jeu_carte].cartes)-1
                        temp=list_joueur[index].jeu_de_carte[selection_jeu_carte].cartes[temp]
                        interface.carte_double_joueur(index,temp%4,(temp//4)+1)
            if choix==False:
                choix=list_joueur[index].IA_hit(i)        #Sinon on verifie s'il veut hit et sinon il s'arrete
                if choix:
                    if list_joueur[2]!=0:
                        interface.configure_message(index,"HIT")
                        temp=len(list_joueur[index].jeu_de_carte[selection_jeu_carte].cartes)-1
                        temp=list_joueur[index].jeu_de_carte[selection_jeu_carte].cartes[temp]
                        interface.carte_joueur(index,temp%4,(temp//4)+1)
            choix=False
            list_joueur[index].jeu_de_carte[i].points()
            if list_joueur[index].jeu_de_carte[i].pts>=21 or list_joueur[index].en_jeu==False:
                list_joueur[index].en_jeu=True
                i+=1
                if i==1 and jeu_carte_split and list_joueur[2]!=0:
                    interface.split_movement_joueur(index,list_joueur[index].jeu_de_carte[0].cartes,list_joueur[index].jeu_de_carte[1].cartes)
                    selection_jeu_carte=1
            if list_joueur[2]!=0:
                interface.configure_points(index,list_joueur[index].jeu_de_carte[selection_jeu_carte].pts)
        if jeu_carte_split==1 and list_joueur[2]!=0:
                interface.fin_split_reconfigure(index)
        index+=1
        etape_jeu()


def etape_croupier():       #Etape ou le croupier joue
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
        if list_joueur[2]!=0 and len(Croupier.cartes)>2:
            temp=len(Croupier.cartes)-1
            temp=Croupier.cartes[temp]
            interface.carte_croupier(temp%4,(temp//4)+1)
            interface.configure_point_croupier(Croupier.pts)
    if list_joueur[2]!=0:
        if len(Croupier.cartes)==2:
            temp=Croupier.cartes[1]
            interface.appa_carte_croupier(temp%4,(temp//4)+1)

    if list_joueur[2]!=0:
        interface.configure_point_croupier(Croupier.pts)
        interface.message.configure(text="Croupier: "+str(Croupier.pts)+" points")
    etape_paie()


def etape_paie():           #Etape ou la paie se fait et on relance le prochain jeu et les mises
    global list_joueur,Croupier,recursion,fen,rang
    Croupier.points()
    
    for i in range(5):
        if list_joueur[i]!=0 and list_joueur[i].blackjack==False:
            for j in range(len(list_joueur[i].jeu_de_carte)):
                list_joueur[i].jeu_de_carte[j].points()
                if list_joueur[i].jeu_de_carte[j].pts>21:
                    if i==2 and list_joueur[2]!=0:
                        interface.movement_argent()
                        if j==0:
                            interface.afficher_gagne("croupier")
                        elif j==1:
                            interface.afficher_gagne_split("croupier")
                    if list_joueur[2]!=0:
                        interface.configure_message(i,"PERDU")
                elif Croupier.pts>21:
                    list_joueur[i].argent+=list_joueur[i].jeu_de_carte[j].bet*2
                    if i==2 and list_joueur[2]!=0:
                        interface.movement_argent("gagnant")
                        if j==0:
                            interface.afficher_gagne("joueur")
                        elif j==1:
                            interface.afficher_gagne_split("joueur")
                    if list_joueur[2]!=0:
                        interface.configure_message(i,"GAGNE!!")
                elif Croupier.pts<list_joueur[i].jeu_de_carte[j].pts:
                    list_joueur[i].argent+=list_joueur[i].jeu_de_carte[j].bet*2
                    if i==2 and list_joueur[2]!=0:
                        interface.movement_argent("gagnant")
                        if j==0:
                            interface.afficher_gagne("joueur")
                        elif j==1:
                            interface.afficher_gagne_split("joueur")
                    if list_joueur[2]!=0:
                        interface.configure_message(i,"GAGNE!!")
                elif Croupier.pts>list_joueur[i].jeu_de_carte[j].pts:
                    if i==2 and list_joueur[2]!=0:
                        interface.movement_argent()
                        if j==0:
                            interface.afficher_gagne("croupier")
                        elif j==1:
                            interface.afficher_gagne_split("croupier")
                    if list_joueur[2]!=0:
                        interface.configure_message(i,"PERDU")
                elif Croupier.pts == list_joueur[i].jeu_de_carte[j].pts:
                    list_joueur[i].argent+=list_joueur[i].jeu_de_carte[j].bet
                    if i==2 and list_joueur[2]!=0:
                        interface.movement_argent("gagnant")
                        if j==0:
                            interface.afficher_gagne("egalite")
                        elif j==1:
                            interface.afficher_gagne_split("egalite")
                    if list_joueur[2]!=0:
                        interface.configure_message(i,"EGALITE")
    for i in range(5):      #On cherche les joueurs qui n'on plus d'argent ou qui atteint l'objectifs
        if list_joueur[i]!=0:
            if list_joueur[i].argent<=0:        #Plus d'argent
                interface.gagnant_perdant(i,"PERDANT")
                rang.append(i)
                if i==2:
                    interface.nettoyage()
                    interface.caneva.delete(interface.text_nouvelle_partie)
                    if fen[3]!=1:
                        interface.pause_nouvelle_partie()
                interface.message.configure(text="Le joueur "+str(i+1)+" a perdu",fg="blue")
                list_joueur[i]=0                
            elif list_joueur[i].argent>=fen[2]:       #Objectif (fen[2] correspond a la somme a atteindre)
                #Le jeu entier s'arrete si qqun atteint l'objectif
                rang=[i]
                list_joueur=[0,0,0,0,0]
                interface.nettoyage()
                interface.caneva.delete(interface.text_nouvelle_partie)
                interface.gagnant_perdant(i,"GAGNANT")
                if i==2:
                    showinfo("VICTOIRE", "FELICITATION\nVOUS AVEZ GAGNE !")
                else:
                    showinfo("VICTOIRE", "LE JOUEUR "+str(i+1)+" A GAGNE !")
                interface.fenetre.destroy()
                print("destruction1")
                return

    if list_joueur.count(0)==5 and fen[3]!=1:
        compteur=fen[3]-1
        temp=""
        classement=1
        while compteur>=0:
            if rang[compteur]==2:
                if classement==1:
                    temp=temp+"       "+str(classement)+"er       Vous\n"
                else:
                    temp=temp+"       "+str(classement)+"eme   Vous\n"
            else:
                if classement==1:
                    temp=temp+"       "+str(classement)+"er       Joueur "+str(rang[compteur]+1)+"\n"
                else:
                    temp=temp+"       "+str(classement)+"ème   Joueur "+str(rang[compteur]+1)+"\n"
            compteur=compteur-1
            classement=classement+1
        showinfo("RESULTATS", temp)
        interface.fenetre.destroy()
        print("destruction2")
        return
    elif list_joueur[2]==0 and fen[3]==1:
        showinfo("PERDU", "VOUS AVEZ PERDU !")
        interface.fenetre.destroy()
        print("destruction3")
        return
            
    Croupier=Jeu(None)      #Remise a zero du croupier
    Croupier.points()       #On ne veut pas qu'il garde les meme cartes
    if len(carte.pille)<52:        #S'il ne reste plus que 52 cartes alors on melange a nouveau les cartes
        carte.melange()
    if list_joueur[2]!=0:
        interface.pause_nouvelle_partie()
        interface.nettoyage()
    if list_joueur[2]!=0:
        interface.configure_argent(list_joueur[2].argent)
    if fen[3]>1:
        if list_joueur[2]!=0:
            if list_joueur[0]!=0:
                interface.configure_points(0,0)
                interface.configure_mises(0,0)
                interface.configure_argent_joueurs(0,list_joueur[0].argent)
    if fen[3]>2:
        if list_joueur[2]!=0:
            if list_joueur[1]!=0:
                interface.configure_points(1,0)
                interface.configure_mises(1,0)
                interface.configure_argent_joueurs(1,list_joueur[1].argent)
    if fen[3]>3:
        if list_joueur[2]!=0:
            if list_joueur[3]!=0:
                interface.configure_points(3,0)
                interface.configure_mises(3,0)
                interface.configure_argent_joueurs(3,list_joueur[3].argent)
    if fen[3]>4:
        if list_joueur[2]!=0:
            if list_joueur[4]!=0:
                interface.configure_points(4,0)
                interface.configure_mises(4,0)
                interface.configure_argent_joueurs(4,list_joueur[4].argent)
        
    while list_joueur.count(0)!=5:
        if recursion==False:
            recursion=True
            etape_parie()
        if recursion==True:
            recursion=False
            return


            
        
def stat():         #fonction statistique pour le joueur Humain
    pille_total=[]
    list_joueur[2].jeu_de_carte[0].points()
    x=21-list_joueur[2].jeu_de_carte[0].pts_min

    if x>=10:
        return 100
    else:
        total=0
        for i in range (len(carte.pille)):
            pille_total.append(carte.pille[i])
        pille_total.append(Croupier.cartes[1])
        for i in range(4*x):
            total+=pille_total.count(i)
        pourcentage=round((total*100)/(len(pille_total)))
        return pourcentage

        
