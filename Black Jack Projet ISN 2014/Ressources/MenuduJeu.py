from tkinter import*                                                        #Importation de tkinter qui permet de faire du graphisme
from tkinter.messagebox import askyesno
from PIL import Image,ImageTk                                               #Importation de pillow qui permet d'utiliser les image png
import module_jeu_remake as jeu


fen=Tk()                                                                    #Ouverture d'une fenetre dont le nom est "fen"
fen.title("MENU")                                                           #modifie le nom de la fenetre "fen" et met "MENU" comme titre
def regle():
    global fen
    for w in fen.winfo_children():
        w.destroy()
    frame_regle=Frame(fen, width=600, height=450,bg="dark green")
    frame_regle.grid_propagate(0)
    frame_regle.pack()
    barre = Scrollbar(frame_regle, orient=VERTICAL)
    barre.grid(row=0, column=1, sticky=N+S)
    text_regle = Listbox(frame_regle, width=96, height=25,xscrollcommand=barre.set,bg="dark green",disabledforeground="White",highlightcolor="dark green",highlightbackground="dark green",relief=FLAT)
    text_regle.grid(row=0, column=0)
    barre['command'] = text_regle.yview
    text_regle.insert(END,"\n")
    text_regle.insert(END,"                                                                                  Règles du Black Jack")
    text_regle.insert(END,"\n")
    text_regle.insert(END," La distribution des cartes commence après que les joueurs aient misé : la mise se place automatiquement sur")
    text_regle.insert(END," la table de jeu.")
    text_regle.insert(END,"\n")
    text_regle.insert(END," Le Croupier distribue ensuite  deux  cartes à chacun des joueurs,  et deux carte à lui-même dont une face non")
    text_regle.insert(END," visible.")
    text_regle.insert(END," Le Joueur  (après analyse de son jeu et de la carte du Croupier)  peut alors choisir Stand s'il est satisfait de son")
    text_regle.insert(END," jeu, il peut aussi demander une carte de plus en cliquant sur Hit pour atteindre ou se rapprocher de 21 points.")
    text_regle.insert(END," S'il dépasse 21 points il  a perdu et sa mise revient au Croupier.")
    text_regle.insert(END,"\n")
    text_regle.insert(END," Le Joueur  peut continuer à demander des cartes tant  qu'il souhaite  pour améliorer son score.  Une fois tous")
    text_regle.insert(END," les joueurs servis,  le Croupier  se sert à son tour, jusqu'à ce qu'il atteigne ou dépasse  17  points, puis il Stand.")
    text_regle.insert(END,"\n")
    text_regle.insert(END," Le Croupier compare alors son jeu avec les jeux des joueurs, pour déterminer  qui gagne (celui  qui a le  score")
    text_regle.insert(END," le plus élevé gagne).")
    text_regle.insert(END,"\n")
    text_regle.insert(END," Il  y  a une pause au moment de recommencer une partie pour permettre au joueur d'analyser le jeu.  Un  clic")
    text_regle.insert(END," permet de lancer la partie suivante")
    text_regle.insert(END,"      ___________________________________________________________________________________________________________")
    text_regle.insert(END,"\n")
    text_regle.insert(END,"                                                                                    Valeur des cartes")
    text_regle.insert(END,"\n")
    text_regle.insert(END," Les figures (Valets,  Reines, Rois) valent 10,  l’As vaut 1 ou 11 (au choix,  selon ce qui est plus avantageux pour")
    text_regle.insert(END," le Joueur) et les autres cartes prennent leur valeur faciale.")
    text_regle.insert(END,"\n")
    text_regle.insert(END," Black Jack est le meilleur jeu  possible avec  les deux  premières  cartes  totalisant  21,   (un As et un 10 ou une")
    text_regle.insert(END," figure).")
    text_regle.insert(END,"      ___________________________________________________________________________________________________________")
    text_regle.insert(END,"\n")
    text_regle.insert(END,"                                                                                    Scores finaux, gains")
    text_regle.insert(END,"\n")
    text_regle.insert(END," Le joueur fait black jack : il récupère sa mise + gagne 1,5 fois sa mise")
    text_regle.insert(END," Le joueur est plus près de 21 que le croupier : il récupère sa mise + gagne 1 fois sa mise")
    text_regle.insert(END," Le croupier dépasse 21 : le joueur récupère sa mise + gagne 1 fois sa mise")
    text_regle.insert(END," Égalité de points : le Joueur récupère sa mise (même Black Jack)")
    text_regle.insert(END," Le joueur dépasse 21 : le Joueur perd sa mise")
    text_regle.insert(END," Le croupier est plus près de 21 que le joueur : le Joueur perd sa mise")
    text_regle.insert(END,"      ___________________________________________________________________________________________________________")
    text_regle.insert(END,"\n")
    text_regle.insert(END,"                                                                           Actions possibles au Black Jack")
    text_regle.insert(END,"\n")
    text_regle.insert(END," - L'Assurance : lorsque la première carte du Croupier est un As, le Joueur peut prendre une assurance pour se")
    text_regle.insert(END," prémunir d’un Black Jack, c’est à dire déposer sur la ligne assurance de la table, une mise égale à la moitié de")
    text_regle.insert(END," sa mise initiale.")
    text_regle.insert(END," Si  le  Croupier  fait  Black Jack ,  le Joueur  gagne deux fois son assurance,  mais perd sa mise (donc il n'a rien")
    text_regle.insert(END," perdu).")
    text_regle.insert(END," Si le Croupier ne fait pas Black Jack, le Joueur perds l'assurance, puis la partie continue normalement.")
    text_regle.insert(END,"\n")
    text_regle.insert(END," - La Double mise : après la distribution des deux premières cartes, le Joueur peut doubler sa mise (en cliquant")
    text_regle.insert(END," sur Double) mais ne pourra dès lors  ne  recevoir  plus  qu'une  seule  carte.  Cette  dernière  carte  se  place  à")
    text_regle.insert(END," l'horizontal sur son tas de jeu.")
    text_regle.insert(END,"\n")
    text_regle.insert(END," - Faire un split / partager les cartes : si les deux premières cartes du Joueur forment une paire il a la possibilité")
    text_regle.insert(END," de les séparer en deux mains distinctes, en cliquant sur Split.  Ses deux cartes se séparent alors en deux et une")
    text_regle.insert(END," carte arrive sur chacune d'elles pour former deux jeux de cartes.")
    text_regle.insert(END," Le  joueur  mise  la meme chose sur chaque jeux de cartes.  Ainsi le joueur peut gagner ou perdre sa mise sur")
    text_regle.insert(END," chacun des deux jeux de cartes de la même manière que lors d'une partie sans split.")
    text_regle.insert(END," Tout 21 obtenu après un split ne compte pas comme « Black Jack », puisqu’il n’a pas été réalisé avec les deux")
    text_regle.insert(END," cartes d’origine.")
    text_regle.insert(END,"\n")
    text_regle.insert(END," - Stand : stand ou rester signifie ne plus prendre de cartes supplémentaires.")
    text_regle.insert(END,"\n")
    text_regle.insert(END," - Hit : Hit signifie prendre une autre carte.")
    text_regle.configure(state=DISABLED)
    bouton_retour=Button(frame_regle,text="Retour",command=menu,bg="green",fg="white",activebackground="green",activeforeground="white")
    bouton_retour.grid(row=1,column=0,columnspan=2,sticky=N,pady=8)
    fen.mainloop()
def nouvelle_partie():
    global fen
    for w in fen.winfo_children():
        w.destroy()
    frame_nouvelle_partie=Frame(fen,width=604,height=454,bg="dark green")
    frame_nouvelle_partie.grid_propagate(0)
    frame_nouvelle_partie.pack_propagate(0)
    frame_nouvelle_partie.pack()
    text=Label(frame_nouvelle_partie,text="OPTIONS DE JEU",bg="dark green",fg="blue",font="Arial 10 bold italic")
    text.grid(row=0,column=0,columnspan=3,sticky=N,padx=10,pady=20)
    cadre1=Canvas(frame_nouvelle_partie,width=112,height=157,bg="dark green",highlightbackground="dark green")
    cadre1.grid(row=1,column=0,padx=40)
    cadre2=Canvas(frame_nouvelle_partie,width=112,height=157,bg="dark green",highlightbackground="dark green")
    cadre2.grid(row=1,column=1,padx=40)
    cadre3=Canvas(frame_nouvelle_partie,width=112,height=157,bg="dark green",highlightbackground="dark green")
    cadre3.grid(row=1,column=2,padx=40)
    image_carte1=Image.open("Carte blackjack Bleu.png").resize((112,157), Image.ANTIALIAS)
    image_carte1=ImageTk.PhotoImage(image_carte1)
    cadre1.create_image(57,78,image=image_carte1)
    image_carte2=Image.open("Carte blackjack Rouge.png").resize((112,157), Image.ANTIALIAS)
    image_carte2=ImageTk.PhotoImage(image_carte2)
    cadre2.create_image(57,78,image=image_carte2)
    image_carte3=Image.open("Carte blackjack Mandoline.png").resize((112,157), Image.ANTIALIAS)
    image_carte3=ImageTk.PhotoImage(image_carte3)
    cadre3.create_image(57,78,image=image_carte3)
    valeur_bouton=StringVar()
    valeur_bouton.set("1")
    bouton_radio1=Radiobutton(frame_nouvelle_partie,variable=valeur_bouton,value="1",command=None,bg="dark green")
    bouton_radio1.grid(row=2,column=0)
    bouton_radio1.select()
    bouton_radio2=Radiobutton(frame_nouvelle_partie,variable=valeur_bouton,value="2",command=None,bg="dark green")
    bouton_radio2.grid(row=2,column=1)
    bouton_radio2.deselect()
    bouton_radio3=Radiobutton(frame_nouvelle_partie,variable=valeur_bouton,value="3",command=None,bg="dark green")
    bouton_radio3.grid(row=2,column=2)
    bouton_radio3.deselect()
    text_argentdep=Label(frame_nouvelle_partie,text="Argent de Départ : ",bg="dark green")
    text_argentdep.grid(row=3,column=0,sticky=E,pady=20)
    selection_argentdep=Spinbox(frame_nouvelle_partie,from_=100 ,to=10000,increment=10,width=6)
    selection_argentdep.delete(0,END)
    selection_argentdep.insert(0,"1000")
    selection_argentdep.grid(row=3,column=1,sticky=W)
    text_argentfin=Label(frame_nouvelle_partie,text="Somme à atteindre pour gagner : ",bg="dark green")
    text_argentfin.grid(row=4,column=0,sticky=E)
    selection_argentfin=Spinbox(frame_nouvelle_partie,from_=200 ,to=50000,increment=10,width=6)
    selection_argentfin.delete(0,END)
    selection_argentfin.insert(0,"2000")
    selection_argentfin.grid(row=4,column=1,sticky=W)
    text_joueur=Label(frame_nouvelle_partie,text="Nombre de joueur : ",bg="dark green")
    text_joueur.grid(row=5,column=0,sticky=E,pady=20)
    selection_joueur=Spinbox(frame_nouvelle_partie,from_=1 ,to=5,increment=1,width=2)
    selection_joueur.delete(0,END)
    selection_joueur.insert(0,"1")
    selection_joueur.grid(row=5,column=1,sticky=W)
    bouton_retour=Button(frame_nouvelle_partie,text="Retour",command=menu,bg="green",fg="white",activebackground="green",activeforeground="white")
    bouton_retour.grid(row=6,column=0,sticky=N)
    bouton_jouer=Button(frame_nouvelle_partie,text="  JOUER  ",command=fen.quit,bg="green",fg="white",activebackground="green",activeforeground="white")
    bouton_jouer.grid(row=6,column=2,sticky=N)
    fen.mainloop()
    temp=0
    try:
        temp=[int(valeur_bouton.get()),int(selection_argentdep.get()),int(selection_argentfin.get()),int(selection_joueur.get())]
    except TclError:
        print("TclError: invalid command name")
        print("_______________CORRECTION ERREUR_______________")
        return
    fen.destroy()
    fen=temp
def quitter():
    global fen
    if askyesno("QUITTER", "Etes vous sur de vouloir quitter?"):
        fen.destroy()
def menu():
    global fen
    fen.quit()
    for w in fen.winfo_children():
        w.destroy()
    fen.configure(bg="dark green")                                                    #modifie la couleur de la fenetre en couleur:"dark green"
    cadre=Canvas(fen,width=600,height=400,bg="dark green",highlightbackground="dark green") #cré un canevas(cadre dans la fentre) nommé "cadre", de hauteur400, de longueur 600, de couleur "dark green"
    image_blackjack=Image.open("Image BlackJack menu.png")                                #ouvre un image apelée "blackjack3.png" et l'enregistre dans la variable image_blackjack
    image_blackjack=ImageTk.PhotoImage(image_blackjack)                         #converti l'image contenu dans la variable image_blackjack en une image lisible par tkinter
    cadre.create_image(300,200,image=image_blackjack)                           #place l'image contenu dans la variable image_blakjack dans le cadre a la position x=300 et y=200
    cadre.pack()                                                                #affiche le cadre dans la fenetre
    frame=Frame(fen,width=485,height=50,bg="dark green")                              #cré un Frame(cadre dans lequel on peut mettre des objet Tkinter) de longueur485 et de hauteur50 et de couleur"dark green"
    frame.grid_propagate(0)                                                     #empeche le redimentionnement du cadre Frame quand on met un objet dedans
    frame.pack()                                                                #place le Frame dans la fenetre
    bouton_regles=Button(frame,text="Règles",command=regle,bg="green",fg="white",activebackground="green",activeforeground="white")
    bouton_regles.grid(row=1,column=1)
    bouton_nouvelle=Button(frame,text="Nouvelle Partie",command=nouvelle_partie,bg="green",fg="white",activebackground="green",activeforeground="white")
    bouton_nouvelle.grid(row=1,column=2,padx=150)
    bouton_quitter=Button(frame,text="Quitter",command=quitter,bg="green",fg="white",activebackground="green",activeforeground="white")
    bouton_quitter.grid(row=1,column=3)
    fen.mainloop()



while True:
    menu()
    try:
        jeu.jeu(fen)
    except TclError:
        pass
    fen=Tk()                                                                    #Ouverture d'une fenetre dont le nom est "fen"
    fen.title("MENU")
