from tkinter import *
from PIL import Image,ImageTk

class Cadre_joueur:
    """Class qui s'occupe de creer et de gerer les cadres d'information des
    joueurs de l'Intelligence Artificielle"""
    def __init__(self,index,fenetre):
        self.frame=Frame(fenetre,width=115,height=140,bg="black",relief=RIDGE)
        self.frame.grid_propagate(0)
        self.text1=Label(self.frame, text="JOUEUR "+str(index+1),fg="dark green",bg="black")
        self.text1.grid(row=1,column=1,pady=5,columnspan=2,sticky=N)
        self.text2=Label(self.frame, text="Argent :",fg="white",bg="black")
        self.text2.grid(row=2,column=1,sticky=E)
        self.case_argent=Entry(self.frame,bg="black",fg="white",justify=CENTER,width=10,disabledbackground="black",disabledforeground="white")
        self.case_argent.insert(0,"1000.0€")
        self.case_argent.config(state=DISABLED)
        self.case_argent.grid(row=2,column=2,sticky=W)
        self.text3=Label(self.frame, text="Mise :",fg="white",bg="black")
        self.text3.grid(row=3,column=1,sticky=E)
        self.case_mise=Entry(self.frame,bg="black",fg="white",justify=CENTER,width=10,disabledbackground="black",disabledforeground="white")
        self.case_mise.insert(0,"00.0€")
        self.case_mise.config(state=DISABLED)
        self.case_mise.grid(row=3,column=2,sticky=W)
        self.text4=Label(self.frame, text="Points :",fg="white",bg="black")
        self.text4.grid(row=4,column=1,sticky=E)
        self.case_points=Entry(self.frame,bg="black",fg="white",justify=CENTER,width=10,disabledbackground="black",disabledforeground="white")
        self.case_points.insert(0,"00 pts")
        self.case_points.config(state=DISABLED)
        self.case_points.grid(row=4,column=2,sticky=W)
        self.text_message="-"
        self.message=Label(self.frame,text=self.text_message,fg="green",bg="black")
        self.message.grid(row=5,column=1,sticky=N,columnspan=2)
        self.message2=Label(self.frame,text=self.text_message,fg="green",bg="black")
        self.message2.grid(row=6,column=1,sticky=N,columnspan=2)
    def __repr__(self):
        return "Objet de type Cadre regroupant les information (argent, points...) des joueurs de l'IA"
    def configure_argent_joueur(self,argent):
        self.case_argent.configure(state=NORMAL)
        self.case_argent.delete(0,END)
        self.case_argent.insert(0,str(float(argent))+"€")
        self.case_argent.configure(state=DISABLED)
    def configure_point(self,points):
        self.case_points.configure(state=NORMAL)
        self.case_points.delete(0,END)
        self.case_points.insert(0,str(int(points))+" pts")
        self.case_points.configure(state=DISABLED)
    def configure_mise(self,mise):
        self.case_mise.configure(state=NORMAL)
        self.case_mise.delete(0,END)
        self.case_mise.insert(0,str(float(mise))+"€")
        self.case_mise.configure(state=DISABLED)

class Graphisme:
    def __init__(self,nombrejoueur=1,tapis=1):
        self.dictionnaire={1: "carte",2: "carte"}
        self.dictcroupier={1: "carte",2: "carte"}
        self.dictjetons={1: "jeton",2: "jeton"}
        self.dictjetons_assurance={1: "jeton",2: "jeton"}
        self.dictjoueur={1: "carte",2: "carte"}
        self.dict_valeur_carte={1: "carte_valeur",2: "carte_valeur"}
        self.dict_valeur_carte_croupier={1: "carte_valeur",2: "carte_valeur"}
        self.dict_valeur_carte_joueur={1: "carte_valeur",2: "carte_valeur"}
        self.fenetre =Tk()
        self.fenetre.title("- - - - - - - B L A C K J A C K - - - - - - -")
        self.caneva=Canvas(self.fenetre, width=1108, height=773, bg="Black",highlightbackground="Black")
        self.caneva.grid(row=1,column=2,columnspan=3)
        if tapis==1:
            self.tapis_blackjack=Image.open("Tapis blackjack - Carte Bleu.png")
            self.revers_carte=Image.open("Carte blackjack Bleu.png")
        elif tapis==2:
            self.tapis_blackjack=Image.open("Tapis blackjack - Carte Rouge.png")
            self.revers_carte=Image.open("Carte blackjack Rouge.png")
        elif tapis==3:
            self.tapis_blackjack=Image.open("Tapis blackjack - Carte Mandoline.png")
            self.revers_carte=Image.open("Carte blackjack Mandoline.png")
        self.tapis_blackjack=self.tapis_blackjack.resize((1108,773), Image.ANTIALIAS)
        self.tapis_blackjack=ImageTk.PhotoImage(self.tapis_blackjack)
        self.caneva.create_image(554,386,image=self.tapis_blackjack)

        #CREATION BARRE DU BAS
        self.frame=Frame(self.fenetre,width=323,height=27)
        self.frame.grid_propagate(0)
        self.frame.grid(row=2,column=2)
        self.frame2=Frame(self.fenetre,width=651,height=27)
        self.frame2.grid_propagate(0)
        self.frame2.pack_propagate(0)
        self.frame2.grid(row=2,column=3)
        self.frame3=Frame(self.fenetre,width=134,height=27)
        self.frame3.grid_propagate(0)
        self.frame3.grid(row=2,column=4)
        self.text1=Label(self.frame, text="Votre argent : ",font=('arial','8','bold'))
        self.text1.grid(row=1,column=1,sticky=W)
        self.entree1=Entry(self.frame,bg="black",fg="white",justify=CENTER,width=10,disabledbackground="black",disabledforeground="white")
        self.entree1.insert(0,"1000.0€")
        self.entree1.config(state=DISABLED)
        self.entree1.grid(row=1,column=2,sticky=W)
        self.text2=Label(self.frame, text="\ Mise en cours : ",font=('arial','8','bold'))
        self.text2.grid(row=1,column=3,sticky=W)
        self.entree2=Entry(self.frame,bg="black",fg="white",justify=CENTER,width=10,disabledbackground="black",disabledforeground="white")
        self.entree2.insert(0,"00.0€")
        self.entree2.config(state=DISABLED)
        self.entree2.grid(row=1,column=4,sticky=W)
        self.text3=Label(self.frame, text=" \ ")
        self.text3.grid(row=1,column=5,sticky=W)
        self.text4=Label(self.frame3, text="\ Nombre de joueur : "+str(nombrejoueur))
        self.text4.grid(row=1,column=1,sticky=E)
        self.text_message=None
        self.message=Label(self.frame2,textvariable=self.text_message,fg="blue")
        self.message.pack()
        #CADRES JOUEUR
        if nombrejoueur>1:
            self.frame5=Frame(self.fenetre,width=115,height=800,bg="black")
            self.frame5.grid_propagate(0)
            self.frame5.pack_propagate(0)
            self.frame5.grid(row=1,column=5,rowspan=2)
            self.frame_separation1=Frame(self.frame5,width=115,height=280,bg="black")
            self.frame_separation1.grid()
            self.cadre_joueur0=Cadre_joueur(0,self.frame5)
            self.cadre_joueur0.frame.grid()
            if nombrejoueur>2:
                self.cadre_joueur1=Cadre_joueur(1,self.frame5)
                self.cadre_joueur1.frame.grid()
        if nombrejoueur==5:
            self.frame4=Frame(self.fenetre,width=115,height=800,bg="black")
            self.frame4.grid_propagate(0)
            self.frame4.pack_propagate(0)
            self.frame4.grid(row=1,column=1,rowspan=2)
            self.frame_separation2=Frame(self.frame4,width=115,height=280,bg="black")
            self.frame_separation2.grid()
            self.cadre_joueur4=Cadre_joueur(4,self.frame4)
            self.cadre_joueur4.frame.grid()
            self.cadre_joueur3=Cadre_joueur(3,self.frame4)
            self.cadre_joueur3.frame.grid()
        elif nombrejoueur==4:
            self.frame4=Frame(self.fenetre,width=115,height=800,bg="black")
            self.frame4.grid_propagate(0)
            self.frame4.pack_propagate(0)
            self.frame4.grid(row=1,column=1,rowspan=2)
            self.frame_separation2=Frame(self.frame4,width=115,height=420,bg="black")
            self.frame_separation2.grid()
            self.cadre_joueur3=Cadre_joueur(3,self.frame4)
            self.cadre_joueur3.frame.grid()
        self.revers_carte=self.revers_carte.resize((112,157), Image.ANTIALIAS)
        self.revers_carte_convertTk=ImageTk.PhotoImage(self.revers_carte)
        self.nombre_carte=0
        self.nombre_carte_croupier=0
        self.nombre_carte_joueur=0
        self.image_carte_double=0
        self.nombre_carte_joueur0=0
        self.nombre_carte_joueur1=0
        self.nombre_carte_joueur3=0
        self.nombre_carte_joueur4=0
        self.split_ok=1
        self.split_ok_joueur=1
        self.text=None
        self.text_blackjack_joueur0=None
        self.text_blackjack_joueur1=None
        self.text_blackjack_joueur2=None
        self.text_blackjack_joueur3=None
        self.text_blackjack_joueur4=None
        self.text_pourcentage=None
        self.text_points_joueur=None
        self.text_points_croupier=None
        self.text_nouvelle_partie=None
        self.assurance=False
        self.nombre_jetons_assurance=0
        self.affichage_gagnant_split=None
        
        #IMAGES BOUTONS
        self.image_bouton_hit=Image.open("bouton hit.png")
        self.image_bouton_hit=ImageTk.PhotoImage(self.image_bouton_hit)
        self.image_bouton_stand=Image.open("bouton stand.png")
        self.image_bouton_stand=ImageTk.PhotoImage(self.image_bouton_stand)
        self.image_bouton_double=Image.open("bouton double.png")
        self.image_bouton_double=ImageTk.PhotoImage(self.image_bouton_double)
        self.image_bouton_split=Image.open("bouton split.png")
        self.image_bouton_split=ImageTk.PhotoImage(self.image_bouton_split)
        self.image_bouton_aide=Image.open("bouton aide.png")
        self.image_bouton_aide=ImageTk.PhotoImage(self.image_bouton_aide)
        self.image_bouton_assurance=Image.open("bouton assurance.png")
        self.image_bouton_assurance=ImageTk.PhotoImage(self.image_bouton_assurance)
        self.image_bouton_valider=Image.open("bouton valider.png")
        self.image_bouton_valider=ImageTk.PhotoImage(self.image_bouton_valider)
        self.image_bouton_annuler=Image.open("bouton annuler.png")
        self.image_bouton_annuler=ImageTk.PhotoImage(self.image_bouton_annuler)
        self.bouton_hit=None
        self.bouton_stand=None
        self.bouton_double=None
        self.bouton_split=None
        self.bouton_aide=None
        self.bouton_assurance=None
        #IMAGES JETONS
        self.image_jeton05=Image.open("jeton 0,5.png")
        self.image_jeton05=ImageTk.PhotoImage(self.image_jeton05)
        self.image_jeton1=Image.open("jeton 1.png")
        self.image_jeton1=ImageTk.PhotoImage(self.image_jeton1)
        self.image_jeton5=Image.open("jeton 5.png")
        self.image_jeton5=ImageTk.PhotoImage(self.image_jeton5)
        self.image_jeton10=Image.open("jeton 10.png")
        self.image_jeton10=ImageTk.PhotoImage(self.image_jeton10)
        self.image_jeton50=Image.open("jeton 50.png")
        self.image_jeton50=ImageTk.PhotoImage(self.image_jeton50)
        self.image_jeton100=Image.open("jeton 100.png")
        self.image_jeton100=ImageTk.PhotoImage(self.image_jeton100)
        #AUTRE
        self.fond_pour_point=Image.open("fond points.png")
        self.fond_pour_point=ImageTk.PhotoImage(self.fond_pour_point)
        self.image_croupier_gagne=Image.open("croupier gagne.png")
        self.image_croupier_gagne=ImageTk.PhotoImage(self.image_croupier_gagne)
        self.image_joueur_gagne=Image.open("joueur gagne.png")
        self.image_joueur_gagne=ImageTk.PhotoImage(self.image_joueur_gagne)
        self.image_egalite=Image.open("egalite.png")
        self.image_egalite=ImageTk.PhotoImage(self.image_egalite)

    def __repr__(self):
        return "Objet issu de la class Graphisme(), correspondant a l'Interface Graphique d'un jeu de BlackJack"

    def configure_argent(self,argent):
        self.entree1.configure(state=NORMAL)
        self.entree1.delete(0,END)
        self.entree1.insert(0,str(float(argent))+"€")
        self.entree1.configure(state=DISABLED)

    def configure_points(self,numerojoueur,points):
        if numerojoueur==0:
            self.cadre_joueur0.configure_point(points)
        elif numerojoueur==1:
            self.cadre_joueur1.configure_point(points)
        elif numerojoueur==3:
            self.cadre_joueur3.configure_point(points)
        elif numerojoueur==4:
            self.cadre_joueur4.configure_point(points)

    def configure_mises(self,numerojoueur,mises):
        if numerojoueur==0:
            self.cadre_joueur0.configure_mise(mises)
        elif numerojoueur==1:
            self.cadre_joueur1.configure_mise(mises)
        elif numerojoueur==3:
            self.cadre_joueur3.configure_mise(mises)
        elif numerojoueur==4:
            self.cadre_joueur4.configure_mise(mises)

    def configure_argent_joueurs(self,numerojoueur,argent):
        if numerojoueur==0:
            self.cadre_joueur0.configure_argent_joueur(argent)
        elif numerojoueur==1:
            self.cadre_joueur1.configure_argent_joueur(argent)
        elif numerojoueur==3:
            self.cadre_joueur3.configure_argent_joueur(argent)
        elif numerojoueur==4:
            self.cadre_joueur4.configure_argent_joueur(argent)

    def configure_message(self,numerojoueur,message,numeroligne=1):
        if numerojoueur==0:
            if message=="PERDU":
                self.cadre_joueur0.message.configure(text=message,fg="red")
            else:
                self.cadre_joueur0.message.configure(text=message,fg="green")
        elif numerojoueur==1:
            if message=="PERDU":
                self.cadre_joueur1.message.configure(text=message,fg="red")
            else:
                self.cadre_joueur1.message.configure(text=message,fg="green")
        elif numerojoueur==2:
            if message=="PERDU":
                self.message.configure(text=message,fg="red")
            else:
                self.message.configure(text=message,fg="blue")
        elif numerojoueur==3:
            if message=="PERDU":
                self.cadre_joueur3.message.configure(text=message,fg="red")
            else:
                self.cadre_joueur3.message.configure(text=message,fg="green")
        elif numerojoueur==4:
            if message=="PERDU":
                self.cadre_joueur4.message.configure(text=message,fg="red")
            else:
                self.cadre_joueur4.message.configure(text=message,fg="green")

    def info_blackjack(self,numerojoueur=2):
        """Permet d'indiquer par un texte sur l'interface quel joueur a fait Blackjack"""
        if numerojoueur==0:
            self.text_blackjack_joueur0=self.caneva.create_text(963,230,text="B l a c k J a c k !",fill="black")
        elif numerojoueur==1:
            self.text_blackjack_joueur1=self.caneva.create_text(850,415,text="B l a c k J a c k !",fill="black")
        elif numerojoueur==2:
            self.text_blackjack_joueur2=self.caneva.create_text(550,447,text="B l a c k J a c k !",fill="black")
        elif numerojoueur==3:
            self.text_blackjack_joueur3=self.caneva.create_text(240,415,text="B l a c k J a c k !",fill="black")
        elif numerojoueur==4:
            self.text_blackjack_joueur4=self.caneva.create_text(105,233,text="B l a c k J a c k !",fill="black")

    def info_statistique(self,pourcentage):
        """Affiche la statistique de ne pas depasser 21 pour le joueur "humain" """
        self.text_pourcentage=self.caneva.create_text(560,643,text="Vous avez "+str(pourcentage)+"% de chance de ne pas dépasser 21",font=('arial','10','bold'))

    def configure_point_joueur(self,points):
        if self.text_points_joueur!=None:
            self.caneva.delete(self.text_points_joueur)
            self.caneva.delete(self.image_fond_point)
            self.text_points_joueur=None
        self.image_fond_point=self.caneva.create_image(550,623,image=self.fond_pour_point)
        self.text_points_joueur=self.caneva.create_text(550,623,text=str(points)+" pts")

    def configure_point_croupier(self,points):
        if self.text_points_croupier!=None:
            self.caneva.delete(self.text_points_croupier)
            self.text_points_croupier=None
            self.caneva.delete(self.image_fond_point_croupier)
        self.image_fond_point_croupier=self.caneva.create_image(543,273,image=self.fond_pour_point)
        self.text_points_croupier=self.caneva.create_text(543,273,text=str(points)+" pts")

    def gagnant_perdant(self,numerojoueur=0,info="PERDANT"):
        """Informe l'utilisateur qu'un des joueurs a perdu"""
        if info=="PERDANT":
            temp="Red"
            self.configure_argent_joueurs(numerojoueur,0)
            self.configure_points(numerojoueur,0)
            self.configure_mises(numerojoueur,0)
        else:
            temp="Green"
        if numerojoueur==0:
            if info=="PERDANT":
                self.caneva.create_text(1010,350,text="            PERDU \n Le Joueur a tout misé",fill="Red")
            else:
                self.caneva.create_text(1000,350,text=" GAGNANT ",fill="Blue")
            self.cadre_joueur0.text1.configure(fg=temp)
            self.cadre_joueur0.text2.configure(fg=temp)
            self.cadre_joueur0.text3.configure(fg=temp)
            self.cadre_joueur0.text4.configure(fg=temp)
            self.cadre_joueur0.message.configure(text="")
            self.cadre_joueur0.message2.configure(text="")
            self.cadre_joueur0.case_mise.configure(disabledforeground=temp)
            self.cadre_joueur0.case_argent.configure(disabledforeground=temp)
            self.cadre_joueur0.case_points.configure(disabledforeground=temp)
        elif numerojoueur==1:
            if info=="PERDANT":
                self.caneva.create_text(880,500,text="            PERDU \n Le Joueur a tout misé",fill="Red")
            else:
                self.caneva.create_text(870,500,text=" GAGNANT ",fill="Blue")
            self.cadre_joueur1.text1.configure(fg=temp)
            self.cadre_joueur1.text2.configure(fg=temp)
            self.cadre_joueur1.text3.configure(fg=temp)
            self.cadre_joueur1.text4.configure(fg=temp)
            self.cadre_joueur1.message.configure(text="")
            self.cadre_joueur1.message2.configure(text="")
            self.cadre_joueur1.case_mise.configure(disabledforeground=temp)
            self.cadre_joueur1.case_argent.configure(disabledforeground=temp)
            self.cadre_joueur1.case_points.configure(disabledforeground=temp)
        elif numerojoueur==2:
            if info=="PERDANT":
                self.caneva.create_text(555,550,text="            PERDU \n Vous avez tout misé",fill="Red")
            else:
                self.caneva.create_text(555,550,text=" GAGNANT ",fill="Blue")
        elif numerojoueur==3:
            if info=="PERDANT":
                self.caneva.create_text(235,495,text="            PERDU \n Le Joueur a tout misé",fill="Red")
            else:
                self.caneva.create_text(225,495,text=" GAGNANT ",fill="Blue")
            self.cadre_joueur3.text1.configure(fg=temp)
            self.cadre_joueur3.text2.configure(fg=temp)
            self.cadre_joueur3.text3.configure(fg=temp)
            self.cadre_joueur3.text4.configure(fg=temp)
            self.cadre_joueur3.message.configure(text="")
            self.cadre_joueur3.message2.configure(text="")
            self.cadre_joueur3.case_mise.configure(disabledforeground=temp)
            self.cadre_joueur3.case_argent.configure(disabledforeground=temp)
            self.cadre_joueur3.case_points.configure(disabledforeground=temp)
        elif numerojoueur==4:
            if info=="PERDANT":
                self.caneva.create_text(90,360,text="            PERDU \n Le Joueur a tout misé",fill="Red")
            else:
                self.caneva.create_text(80,360,text=" GAGNANT ",fill="Blue")
            self.cadre_joueur4.text1.configure(fg=temp)
            self.cadre_joueur4.text2.configure(fg=temp)
            self.cadre_joueur4.text3.configure(fg=temp)
            self.cadre_joueur4.text4.configure(fg=temp)
            self.cadre_joueur4.message.configure(text="")
            self.cadre_joueur4.message2.configure(text="")
            self.cadre_joueur4.case_mise.configure(disabledforeground=temp)
            self.cadre_joueur4.case_argent.configure(disabledforeground=temp)
            self.cadre_joueur4.case_points.configure(disabledforeground=temp)

    def afficher_gagne(self, gagnant):
        """Affiche qui gagne du joueur ou du croupier"""
        if gagnant=="croupier":
            self.affichage_gagnant=self.caneva.create_image(480,432,image=self.image_croupier_gagne)
        elif gagnant=="joueur":
            self.affichage_gagnant=self.caneva.create_image(480,432,image=self.image_joueur_gagne)
        elif gagnant=="egalite":
            self.affichage_gagnant=self.caneva.create_image(480,432,image=self.image_egalite)

    def afficher_gagne_split(self, gagnant):
        """Affiche qui gagne du joueur ou du coupier sur le second jeu de cartes, lors d'un split"""
        if gagnant=="croupier":
            self.affichage_gagnant_split=self.caneva.create_text(620,395,text="Croupier gagne",fill="white")
        elif gagnant=="joueur":
            self.affichage_gagnant_split=self.caneva.create_text(620,395,text="Joueur gagne",fill="white")
        elif gagnant=="egalite":
            self.affichage_gagnant_split=self.caneva.create_text(620,395,text="Egalité",fill="white")


    def carte(self,couleur=0,numero=1):
        """Distribue une carte au joueur "humain" """
        self.nombre_carte=self.nombre_carte+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte[self.nombre_carte]=Image.open(chaine_temporaire)
        self.dict_valeur_carte[self.nombre_carte]=self.dict_valeur_carte[self.nombre_carte].resize((368,521), Image.ANTIALIAS)
        self.dict_valeur_carte[self.nombre_carte]=ImageTk.PhotoImage(self.dict_valeur_carte[self.nombre_carte])
        self.dictionnaire[self.nombre_carte] = self.caneva.create_image(938,181 ,image=self.revers_carte_convertTk)
        compteur_movement=0
        while compteur_movement<35:
            compteur_movement = compteur_movement+1                 #!!//Carte arrive en 518,531(centre)//!!
            self.caneva.move(self.dictionnaire[self.nombre_carte], -12,10)
            self.fenetre.after(5,None)
            self.fenetre.update()
        self.caneva.delete(self.dictionnaire[self.nombre_carte])
        self.dictionnaire[self.nombre_carte] = self.caneva.create_image(518,531 ,image=self.dict_valeur_carte[self.nombre_carte])
        if self.nombre_carte>1:
            compteur_movement=0
            while compteur_movement<3*(self.nombre_carte-self.split_ok):
                compteur_movement = compteur_movement+1                 #!!//Carte arrive 50px plus loin(centre)//!!
                self.caneva.move(self.dictionnaire[self.nombre_carte], 10,0)
                self.fenetre.after(5,None)
                self.fenetre.update()

    def carte_joueur(self,numero_joueur=0,couleur=0,numero=1):
        """Distribue une carte a l'un des joueur de l'IA"""
        if numero_joueur==0:
            compteur_max=9
            move_x=0
            move_y=15
            arriver_posx=938
            arriver_posy=316
            self.nombre_carte_joueur0=self.nombre_carte_joueur0+1
            compteur_movement_carte=self.nombre_carte_joueur0
        if numero_joueur==1:
            compteur_max=30
            move_x=-3.6
            move_y=10.6
            arriver_posx=830
            arriver_posy=500
            self.nombre_carte_joueur1=self.nombre_carte_joueur1+1
            compteur_movement_carte=self.nombre_carte_joueur1
        if numero_joueur==3:
            compteur_max=58
            move_x=-12.37
            move_y=5.5
            arriver_posx=220
            arriver_posy=500
            self.nombre_carte_joueur3=self.nombre_carte_joueur3+1
            compteur_movement_carte=self.nombre_carte_joueur3
        if numero_joueur==4:
            compteur_max=61
            move_x=-14
            move_y=2.25
            arriver_posx=84
            arriver_posy=318
            self.nombre_carte_joueur4=self.nombre_carte_joueur4+1
            compteur_movement_carte=self.nombre_carte_joueur4
        self.nombre_carte_joueur=self.nombre_carte_joueur+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_joueur[self.nombre_carte_joueur]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_joueur[self.nombre_carte_joueur]=self.dict_valeur_carte_joueur[self.nombre_carte_joueur].resize((368,521), Image.ANTIALIAS)
        self.dict_valeur_carte_joueur[self.nombre_carte_joueur]=ImageTk.PhotoImage(self.dict_valeur_carte_joueur[self.nombre_carte_joueur])
        self.dictjoueur[self.nombre_carte_joueur] = self.caneva.create_image(938,181 ,image=self.revers_carte_convertTk)
        compteur_movement=0
        while compteur_movement<compteur_max:
            compteur_movement = compteur_movement+1
            self.caneva.move(self.dictjoueur[self.nombre_carte_joueur], move_x,move_y)
            self.fenetre.after(5,None)
            self.fenetre.update()
        if compteur_movement_carte>6:
            self.caneva.move(self.dictjoueur[self.nombre_carte_joueur], 0,13)
            self.fenetre.after(5,None)
            self.fenetre.update()
            self.caneva.move(self.dictjoueur[self.nombre_carte_joueur], 0,13)
            self.fenetre.after(5,None)
            self.fenetre.update()
            self.caneva.delete(self.dictjoueur[self.nombre_carte_joueur])
            self.dictjoueur[self.nombre_carte_joueur] = self.caneva.create_image(arriver_posx,arriver_posy+26,image=self.dict_valeur_carte_joueur[self.nombre_carte_joueur])
            compteur_movement_carte=compteur_movement_carte-6
        else:
            self.caneva.delete(self.dictjoueur[self.nombre_carte_joueur])
            self.dictjoueur[self.nombre_carte_joueur] = self.caneva.create_image(arriver_posx,arriver_posy,image=self.dict_valeur_carte_joueur[self.nombre_carte_joueur])
        if compteur_movement_carte>1:
            compteur_movement=0
            while compteur_movement<2*(compteur_movement_carte-self.split_ok_joueur):
                compteur_movement = compteur_movement+1
                self.caneva.move(self.dictjoueur[self.nombre_carte_joueur], 10,0)
                self.fenetre.after(5,None)
                self.fenetre.update()

    def carte_double(self,couleur=0,numero=1):
        """Envoie une carte au joueur "humain" qui se place a l'horizontale sur le tapis de jeu"""
        self.entree2.configure(state=NORMAL)
        self.entree2.delete(0,END)
        self.entree2.insert(0,str(float(self.mise*2))+"€")
        self.entree2.configure(state=DISABLED)
        self.text_double=self.caneva.create_text(455,410,text="2 X ",fill="Blue")
        self.carte(couleur,numero)
        save_nombre_carte=self.nombre_carte
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        temporaire_carte=Image.open(chaine_temporaire).resize((368,521), Image.ANTIALIAS)
        compteur=0
        while compteur<3:
            self.caneva.move(self.dictionnaire[self.nombre_carte], 10,-10)
            self.fenetre.after(5,None)
            self.fenetre.update()
            compteur=compteur+1
        compteur=0
        self.image_carte_double=ImageTk.PhotoImage(temporaire_carte)
        self.caneva.delete(self.dictionnaire[self.nombre_carte])
        self.cartedouble=self.caneva.create_image(30*(self.nombre_carte)+518,501 ,image=self.image_carte_double)#608
        if self.split_ok!=1:
            self.nombre_carte=2.5
        while compteur<10:
            self.image_carte_double=ImageTk.PhotoImage(temporaire_carte.rotate(compteur*10, expand=1))
            self.caneva.delete(self.cartedouble)
            self.cartedouble = self.caneva.create_image(30*(self.nombre_carte)+518,501 ,image=self.image_carte_double)
            self.fenetre.after(10,None)
            self.fenetre.update()
            compteur=compteur+1
        self.nombre_carte=save_nombre_carte

    def carte_double_joueur(self,numerojoueur,couleur=0,numero=1):
        """Envoie une carte a un des joueurs IA qui se place a l'horizontale sur le tapis de jeu"""
        self.carte_joueur(numerojoueur,couleur,numero)
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        temporaire_carte=Image.open(chaine_temporaire).resize((368,521), Image.ANTIALIAS)
        compteur=0
        while compteur<2:
            self.caneva.move(self.dictjoueur[self.nombre_carte_joueur], 10,-10)
            self.fenetre.after(5,None)
            self.fenetre.update()
            compteur=compteur+1
        compteur=0            
        self.image_carte_double_joueur=ImageTk.PhotoImage(temporaire_carte)
        self.caneva.delete(self.dictjoueur[self.nombre_carte_joueur])
        if numerojoueur==0:
            arriver_posx=938
            arriver_posy=316
            self.cartedouble_joueur=self.caneva.create_image(20*(self.nombre_carte_joueur0)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur)
            nombrecarte=self.nombre_carte_joueur0
        elif numerojoueur==1:
            arriver_posx=830
            arriver_posy=500
            self.cartedouble_joueur=self.caneva.create_image(20*(self.nombre_carte_joueur1)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur)
            nombrecarte=self.nombre_carte_joueur1
        elif numerojoueur==3:
            arriver_posx=220
            arriver_posy=500
            self.cartedouble_joueur=self.caneva.create_image(20*(self.nombre_carte_joueur3)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur)
            nombrecarte=self.nombre_carte_joueur3
        elif numerojoueur==4:
            arriver_posx=84
            arriver_posy=318
            self.cartedouble_joueur=self.caneva.create_image(20*(self.nombre_carte_joueur4)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur)
            nombrecarte=self.nombre_carte_joueur4
        while compteur<10:
            self.image_carte_double_joueur=ImageTk.PhotoImage(temporaire_carte.rotate(compteur*10, expand=1))
            self.caneva.delete(self.cartedouble_joueur)
            self.cartedouble_joueur = self.caneva.create_image(20*(nombrecarte)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur)
            self.fenetre.after(10,None)
            self.fenetre.update()
            compteur=compteur+1
        self.image_carte_double_joueur=ImageTk.PhotoImage(temporaire_carte.rotate(90, expand=1))
        if numerojoueur==0:
            self.image_carte_double_joueur0=self.image_carte_double_joueur
            self.caneva.delete(self.cartedouble_joueur)
            self.dictjoueur[self.nombre_carte_joueur] = self.caneva.create_image(20*(nombrecarte)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur0)
        elif numerojoueur==1:
            self.image_carte_double_joueur1=self.image_carte_double_joueur
            self.caneva.delete(self.cartedouble_joueur)
            self.dictjoueur[self.nombre_carte_joueur] = self.caneva.create_image(20*(nombrecarte)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur1)
        elif numerojoueur==3:
            self.image_carte_double_joueur3=self.image_carte_double_joueur
            self.caneva.delete(self.cartedouble_joueur)
            self.dictjoueur[self.nombre_carte_joueur] = self.caneva.create_image(20*(nombrecarte)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur3)
        elif numerojoueur==4:
            self.image_carte_double_joueur4=self.image_carte_double_joueur
            self.caneva.delete(self.cartedouble_joueur)
            self.dictjoueur[self.nombre_carte_joueur] = self.caneva.create_image(20*(nombrecarte)+arriver_posx,arriver_posy-20 ,image=self.image_carte_double_joueur4)

    def carte_croupier(self,couleur=0,numero=1):
        """Envoie une carte au croupier, si c'est la seconde elle est face cachée"""
        self.nombre_carte_croupier=self.nombre_carte_croupier+1
        if self.nombre_carte_croupier==3:
            self.caneva.delete(self.dictcroupier[2])
            self.dictcroupier[2] = self.caneva.create_image(518,181 ,image=self.dict_valeur_carte_croupier[2])
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_croupier[self.nombre_carte_croupier]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_croupier[self.nombre_carte_croupier]=self.dict_valeur_carte_croupier[self.nombre_carte_croupier].resize((368,521), Image.ANTIALIAS)
        self.dict_valeur_carte_croupier[self.nombre_carte_croupier]=ImageTk.PhotoImage(self.dict_valeur_carte_croupier[self.nombre_carte_croupier])
        self.dictcroupier[self.nombre_carte_croupier] = self.caneva.create_image(938,181 ,image=self.revers_carte_convertTk)
        compteur_movement=0
        while compteur_movement<40:
            compteur_movement = compteur_movement+1
            self.caneva.move(self.dictcroupier[self.nombre_carte_croupier], -12,0)
            self.fenetre.after(5,None)
            self.fenetre.update()
        if self.nombre_carte_croupier!=2:
            self.caneva.delete(self.dictcroupier[self.nombre_carte_croupier])
            self.dictcroupier[self.nombre_carte_croupier] = self.caneva.create_image(458,181 ,image=self.dict_valeur_carte_croupier[self.nombre_carte_croupier])
        if self.nombre_carte_croupier>1:
            compteur_movement=0
            while compteur_movement<6*(self.nombre_carte_croupier-1):
                compteur_movement = compteur_movement+1
                self.caneva.move(self.dictcroupier[self.nombre_carte_croupier], 10,0)
                self.fenetre.after(5,None)
                self.fenetre.update()

    def appa_carte_croupier(self,couleur,numero):
        """Fait apparaitre la deuxieme carte du croupier dans le cas ou elle est face cachée"""
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_croupier[2]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_croupier[2]=self.dict_valeur_carte_croupier[2].resize((368,521), Image.ANTIALIAS)
        self.dict_valeur_carte_croupier[2]=ImageTk.PhotoImage(self.dict_valeur_carte_croupier[2])
        self.caneva.delete(self.dictcroupier[2])
        self.dictcroupier[2] = self.caneva.create_image(518,181 ,image=self.dict_valeur_carte_croupier[2])

    def split(self,carte1=0,carte2=0,carte3=0,carte4=0):
        """Sépare les cartes du joueur "humain" en deux jeux de cartes. (Le joueur doit avoir deux cartes)"""
        compteur_movement=0
        while compteur_movement<12:
            compteur_movement = compteur_movement+1
            self.caneva.move(self.dictionnaire[2], 10,0)
            self.fenetre.after(5,None)
            self.fenetre.update()
        self.split_ok=2
        couleur=carte3%4
        numero=(carte3//4)+1
        self.carte(couleur,numero)
        self.split_ok=-2
        couleur=carte4%4
        numero=(carte4//4)+1
        self.carte(couleur,numero)
        compteur_movement=0
        while compteur_movement<9:
            compteur_movement = compteur_movement+1
            self.caneva.move(self.dictionnaire[2], 0,-10)
            self.caneva.move(self.dictionnaire[4], 0,-10)
            self.fenetre.after(5,None)
            self.fenetre.update()
        couleur=carte2%4
        numero=(carte2//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte[2]=Image.open(chaine_temporaire)
        self.dict_valeur_carte[2]=self.dict_valeur_carte[2].resize((184,260), Image.ANTIALIAS)
        self.dict_valeur_carte[2]=ImageTk.PhotoImage(self.dict_valeur_carte[2])
        self.caneva.delete(self.dictionnaire[2])
        self.dictionnaire[2] = self.caneva.create_image(611,441 ,image=self.dict_valeur_carte[2])
        couleur=carte4%4
        numero=(carte4//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte[4]=Image.open(chaine_temporaire)
        self.dict_valeur_carte[4]=self.dict_valeur_carte[4].resize((184,260), Image.ANTIALIAS)
        self.dict_valeur_carte[4]=ImageTk.PhotoImage(self.dict_valeur_carte[4])
        self.caneva.delete(self.dictionnaire[4])
        self.dictionnaire[4] = self.caneva.create_image(631,441 ,image=self.dict_valeur_carte[4])
        self.split_ok=3
        self.nombre_carte=4
        
    def split_movement(self, chaine_carte1=[0,0], chaine_carte2=[0,0]):
        """Lors d'un split, echange le jeu de carte devant avec celui de derriere"""
        save_nombre_carte=self.nombre_carte
        compteur_movement=0
        while compteur_movement<12:
            if self.image_carte_double!=0:
                self.caneva.move(self.cartedouble,10,0)
            while self.nombre_carte>0:
                if self.nombre_carte!=2 and self.nombre_carte!=4:
                    self.caneva.move(self.dictionnaire[self.nombre_carte], 10,0)
                else:
                    self.caneva.move(self.dictionnaire[self.nombre_carte], -10,0)
                self.nombre_carte=self.nombre_carte-1
            self.fenetre.after(5,None)
            self.fenetre.update()
            compteur_movement=compteur_movement+1
            self.nombre_carte=save_nombre_carte
        couleur=chaine_carte2[0]%4
        numero=(chaine_carte2[0]//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte[2]=Image.open(chaine_temporaire)
        self.dict_valeur_carte[2]=self.dict_valeur_carte[2].resize((368,521), Image.ANTIALIAS)
        self.dict_valeur_carte[2]=ImageTk.PhotoImage(self.dict_valeur_carte[2])
        self.caneva.delete(self.dictionnaire[2])
        self.dictionnaire[2] = self.caneva.create_image(518,441 ,image=self.dict_valeur_carte[2])
        couleur=chaine_carte2[1]%4
        numero=(chaine_carte2[1]//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte[4]=Image.open(chaine_temporaire)
        self.dict_valeur_carte[4]=self.dict_valeur_carte[4].resize((368,521), Image.ANTIALIAS)
        self.dict_valeur_carte[4]=ImageTk.PhotoImage(self.dict_valeur_carte[4])
        self.caneva.delete(self.dictionnaire[4])
        self.dictionnaire[4] = self.caneva.create_image(548,441 ,image=self.dict_valeur_carte[4])
        compteur_movement=0
        self.nombre_carte=save_nombre_carte
        while compteur_movement<9:
            if self.image_carte_double!=0:
                self.caneva.move(self.cartedouble,0,-10)
            while self.nombre_carte>0:
                if self.nombre_carte!=2 and self.nombre_carte!=4:
                    self.caneva.move(self.dictionnaire[self.nombre_carte], 0,-10)
                else:
                    self.caneva.move(self.dictionnaire[self.nombre_carte], 0,10)
                self.nombre_carte=self.nombre_carte-1
            self.fenetre.after(5,None)
            self.fenetre.update()
            compteur_movement=compteur_movement+1
            self.nombre_carte=save_nombre_carte
        compteur=len(chaine_carte1)-1
        self.nombre_carte=save_nombre_carte
        if self.image_carte_double!=0:
            couleur=chaine_carte1[compteur]%4
            numero=(chaine_carte1[compteur]//4)+1
            if couleur==0:
                chaine_temporaire=str(numero)+"C.png"
            elif couleur==1:
                chaine_temporaire=str(numero)+"T.png"
            elif couleur==2:
                chaine_temporaire=str(numero)+"P.png"
            elif couleur==3:
                chaine_temporaire=str(numero)+"CO.png"
            self.dict_valeur_carte[self.nombre_carte]=Image.open(chaine_temporaire)
            self.dict_valeur_carte[self.nombre_carte]=self.dict_valeur_carte[self.nombre_carte].resize((184,260), Image.ANTIALIAS)
            self.dict_valeur_carte[self.nombre_carte]=ImageTk.PhotoImage(self.dict_valeur_carte[self.nombre_carte].rotate(90,expand=1))
            self.caneva.delete(self.cartedouble)
            self.dictionnaire[self.nombre_carte] = self.caneva.create_image(660,430 ,image=self.dict_valeur_carte[self.nombre_carte])
            self.image_carte_double=0
            self.caneva.delete(self.text_double)
            compteur=compteur-1
            self.nombre_carte-=1
        while self.nombre_carte>0:
                if self.nombre_carte!=2 and self.nombre_carte!=4:
                    couleur=chaine_carte1[compteur]%4
                    numero=(chaine_carte1[compteur]//4)+1
                    if couleur==0:
                        chaine_temporaire=str(numero)+"C.png"
                    elif couleur==1:
                        chaine_temporaire=str(numero)+"T.png"
                    elif couleur==2:
                        chaine_temporaire=str(numero)+"P.png"
                    elif couleur==3:
                        chaine_temporaire=str(numero)+"CO.png"
                    self.dict_valeur_carte[self.nombre_carte]=Image.open(chaine_temporaire)
                    self.dict_valeur_carte[self.nombre_carte]=self.dict_valeur_carte[self.nombre_carte].resize((184,260), Image.ANTIALIAS)
                    self.dict_valeur_carte[self.nombre_carte]=ImageTk.PhotoImage(self.dict_valeur_carte[self.nombre_carte])
                    self.caneva.delete(self.dictionnaire[self.nombre_carte])
                    self.dictionnaire[self.nombre_carte] = self.caneva.create_image(611+(20*compteur),441 ,image=self.dict_valeur_carte[self.nombre_carte])
                    compteur=compteur-1
                self.nombre_carte=self.nombre_carte-1
        self.nombre_carte=save_nombre_carte
        self.split_ok=self.nombre_carte-1

    def split_joueur(self,numerojoueur,carte1=0,carte2=0,carte3=0,carte4=0):
        """Sépare les cartes d'un joueur IA en deux jeux de cartes. (Le joueur doit avoir deux cartes)"""
        if numerojoueur==0:
            selection_carte1=1
            selection_carte2=2
            posx=938
            posy=316
            self.nombre_carte_joueur0=2
        elif numerojoueur==1:
            selection_carte1=3
            selection_carte2=4
            posx=830
            posy=500+24
            self.nombre_carte_joueur1=2
        elif numerojoueur==3:
            selection_carte1=5
            selection_carte2=6
            posx=220
            posy=500
            self.nombre_carte_joueur3=2
        elif numerojoueur==4:
            selection_carte1=7
            selection_carte2=8
            posx=84
            posy=318
            self.nombre_carte_joueur4=2
        compteur_movement=0
        while compteur_movement<8:
            compteur_movement = compteur_movement+1
            self.caneva.move(self.dictjoueur[selection_carte2], 10,0)
            self.fenetre.after(5,None)
            self.fenetre.update()
        self.split_ok_joueur=2
        couleur=carte3%4
        numero=(carte3//4)+1
        self.carte_joueur(numerojoueur,couleur,numero)
        self.split_ok_joueur=-2
        couleur=carte4%4
        numero=(carte4//4)+1
        self.carte_joueur(numerojoueur,couleur,numero)
        selection_carte4=self.nombre_carte_joueur
        selection_carte3=selection_carte4-1
        compteur_movement=0
        while compteur_movement<7:
            compteur_movement = compteur_movement+1
            self.caneva.move(self.dictjoueur[selection_carte2], 0,-10)
            self.caneva.move(self.dictjoueur[selection_carte4], 0,-10)
            self.fenetre.after(5,None)
            self.fenetre.update()
        couleur=carte2%4
        numero=(carte2//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_joueur[selection_carte2]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_joueur[selection_carte2]=self.dict_valeur_carte_joueur[selection_carte2].resize((184,260), Image.ANTIALIAS)
        self.dict_valeur_carte_joueur[selection_carte2]=ImageTk.PhotoImage(self.dict_valeur_carte_joueur[selection_carte2])
        self.caneva.delete(self.dictjoueur[selection_carte2])
        self.dictjoueur[selection_carte2] = self.caneva.create_image(posx+110,posy-90 ,image=self.dict_valeur_carte_joueur[selection_carte2])
        couleur=carte4%4
        numero=(carte4//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_joueur[selection_carte4]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_joueur[selection_carte4]=self.dict_valeur_carte_joueur[selection_carte4].resize((184,260), Image.ANTIALIAS)
        self.dict_valeur_carte_joueur[selection_carte4]=ImageTk.PhotoImage(self.dict_valeur_carte_joueur[selection_carte4])
        self.caneva.delete(self.dictjoueur[selection_carte4])
        self.dictjoueur[selection_carte4] = self.caneva.create_image(posx+118,posy-90 ,image=self.dict_valeur_carte_joueur[selection_carte4])
        self.split_ok_joueur=3
        self.selection_carte1=selection_carte1
        self.selection_carte2=selection_carte2
        self.selection_carte3=selection_carte3
        self.selection_carte4=selection_carte4
        self.save_nombre_carte_to_split=self.nombre_carte_joueur

    def split_movement_joueur(self, numerojoueur=0, chaine_carte1=[0,0], chaine_carte2=[0,0]):
        """Lors d'un split pour un joueur IA, echange le jeu de carte devant avec celui de derriere"""
        if numerojoueur==0:
            nombre_carte_temporaire=self.nombre_carte_joueur0
            limite_compteur=self.nombre_carte_joueur1+self.nombre_carte_joueur3+self.nombre_carte_joueur4+4
            limite=self.nombre_carte_joueur0-2
            posx=938
            posy=316
            self.nombre_carte_joueur0=2
        elif numerojoueur==1:
            nombre_carte_temporaire=self.nombre_carte_joueur1
            limite_compteur=self.nombre_carte_joueur0+self.nombre_carte_joueur3+self.nombre_carte_joueur4+4
            limite=self.nombre_carte_joueur1-2
            posx=830
            posy=500
            self.nombre_carte_joueur1=2
        elif numerojoueur==3:
            nombre_carte_temporaire=self.nombre_carte_joueur3
            limite_compteur=self.nombre_carte_joueur1+self.nombre_carte_joueur0+self.nombre_carte_joueur4+4
            limite=self.nombre_carte_joueur3-2
            posx=220
            posy=500
            self.nombre_carte_joueur3=2
        elif numerojoueur==4:
            nombre_carte_temporaire=self.nombre_carte_joueur4
            limite_compteur=self.nombre_carte_joueur1+self.nombre_carte_joueur3+self.nombre_carte_joueur0+4
            limite=self.nombre_carte_joueur4-2
            posx=84
            posy=318
            self.nombre_carte_joueur4=2
        self.sauvegarde_nombre_carte_postsplit=nombre_carte_temporaire
        save_nombre_carte_joueur=self.nombre_carte_joueur
        compteur_movement=0
        while compteur_movement<8:
            while self.nombre_carte_joueur>limite_compteur:
                self.caneva.move(self.dictjoueur[self.nombre_carte_joueur], 10,0)
                self.nombre_carte_joueur=self.nombre_carte_joueur-1
            self.caneva.move(self.dictjoueur[self.selection_carte3], 10,0)
            self.caneva.move(self.dictjoueur[self.selection_carte1], 10,0)
            self.caneva.move(self.dictjoueur[self.selection_carte2], -10,0)
            self.caneva.move(self.dictjoueur[self.selection_carte4], -10,0)
            self.fenetre.after(5,None)
            self.fenetre.update()
            compteur_movement=compteur_movement+1
            self.nombre_carte_joueur=save_nombre_carte_joueur

        couleur=chaine_carte2[0]%4
        numero=(chaine_carte2[0]//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_joueur[self.selection_carte2]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_joueur[self.selection_carte2]=self.dict_valeur_carte_joueur[self.selection_carte2].resize((368,521), Image.ANTIALIAS)
        self.dict_valeur_carte_joueur[self.selection_carte2]=ImageTk.PhotoImage(self.dict_valeur_carte_joueur[self.selection_carte2])
        self.caneva.delete(self.dictjoueur[self.selection_carte2])
        self.dictjoueur[self.selection_carte2] = self.caneva.create_image(posx,posy-70 ,image=self.dict_valeur_carte_joueur[self.selection_carte2])
        couleur=chaine_carte2[1]%4
        numero=(chaine_carte2[1]//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_joueur[self.selection_carte4]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_joueur[self.selection_carte4]=self.dict_valeur_carte_joueur[self.selection_carte4].resize((368,521), Image.ANTIALIAS)
        self.dict_valeur_carte_joueur[self.selection_carte4]=ImageTk.PhotoImage(self.dict_valeur_carte_joueur[self.selection_carte4])
        self.caneva.delete(self.dictjoueur[self.selection_carte4])
        self.dictjoueur[self.selection_carte4] = self.caneva.create_image(posx+20,posy-70 ,image=self.dict_valeur_carte_joueur[self.selection_carte4])
        compteur_movement=0
        self.nombre_carte_joueur=save_nombre_carte_joueur
        while compteur_movement<7:
            while self.nombre_carte_joueur>limite_compteur:
                self.caneva.move(self.dictjoueur[self.nombre_carte_joueur], 0,-10)
                self.nombre_carte_joueur=self.nombre_carte_joueur-1
            self.caneva.move(self.dictjoueur[self.selection_carte3], 0,-10)
            self.caneva.move(self.dictjoueur[self.selection_carte1], 0,-10)
            self.caneva.move(self.dictjoueur[self.selection_carte2], 0,10)
            self.caneva.move(self.dictjoueur[self.selection_carte4], 0,10)
            self.fenetre.after(5,None)
            self.fenetre.update()
            compteur_movement=compteur_movement+1
            self.nombre_carte_joueur=save_nombre_carte_joueur
        if numerojoueur==1:
            posy=500+24
        compteur=len(chaine_carte1)-1
        while self.nombre_carte_joueur>self.save_nombre_carte_to_split:
            couleur=chaine_carte1[compteur]%4
            numero=(chaine_carte1[compteur]//4)+1
            if couleur==0:
                chaine_temporaire=str(numero)+"C.png"
            elif couleur==1:
                chaine_temporaire=str(numero)+"T.png"
            elif couleur==2:
                chaine_temporaire=str(numero)+"P.png"
            elif couleur==3:
                chaine_temporaire=str(numero)+"CO.png"
            self.dict_valeur_carte_joueur[self.nombre_carte_joueur]=Image.open(chaine_temporaire)
            self.dict_valeur_carte_joueur[self.nombre_carte_joueur]=self.dict_valeur_carte_joueur[self.nombre_carte_joueur].resize((184,260), Image.ANTIALIAS)
            self.dict_valeur_carte_joueur[self.nombre_carte_joueur]=ImageTk.PhotoImage(self.dict_valeur_carte_joueur[self.nombre_carte_joueur])
            self.caneva.delete(self.dictjoueur[self.nombre_carte_joueur])
            self.dictjoueur[self.nombre_carte_joueur] = self.caneva.create_image(posx+110+(8*compteur+1),posy-90 ,image=self.dict_valeur_carte_joueur[self.nombre_carte_joueur])
            self.nombre_carte_joueur=self.nombre_carte_joueur-1
            compteur=compteur-1
        couleur=chaine_carte1[1]%4
        numero=(chaine_carte1[1]//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_joueur[self.selection_carte3]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_joueur[self.selection_carte3]=self.dict_valeur_carte_joueur[self.selection_carte3].resize((184,260), Image.ANTIALIAS)
        self.dict_valeur_carte_joueur[self.selection_carte3]=ImageTk.PhotoImage(self.dict_valeur_carte_joueur[self.selection_carte3])
        self.caneva.delete(self.dictjoueur[self.selection_carte3])
        self.dictjoueur[self.selection_carte3] = self.caneva.create_image(posx+118,posy-90 ,image=self.dict_valeur_carte_joueur[self.selection_carte3])
        couleur=chaine_carte1[0]%4
        numero=(chaine_carte1[0]//4)+1
        if couleur==0:
            chaine_temporaire=str(numero)+"C.png"
        elif couleur==1:
            chaine_temporaire=str(numero)+"T.png"
        elif couleur==2:
            chaine_temporaire=str(numero)+"P.png"
        elif couleur==3:
            chaine_temporaire=str(numero)+"CO.png"
        self.dict_valeur_carte_joueur[self.selection_carte1]=Image.open(chaine_temporaire)
        self.dict_valeur_carte_joueur[self.selection_carte1]=self.dict_valeur_carte_joueur[self.selection_carte1].resize((184,260), Image.ANTIALIAS)
        self.dict_valeur_carte_joueur[self.selection_carte1]=ImageTk.PhotoImage(self.dict_valeur_carte_joueur[self.selection_carte1])
        self.caneva.delete(self.dictjoueur[self.selection_carte1])
        self.dictjoueur[self.selection_carte1] = self.caneva.create_image(posx+110,posy-90 ,image=self.dict_valeur_carte_joueur[self.selection_carte1])
        self.nombre_carte_joueur=save_nombre_carte_joueur
        self.split_ok_joueur=1

    def fin_split_reconfigure(self,numero_joueur):
        """Remet a "zero" le joueur IA apres son split pour que les cartes soit distribuées correctement au autre joueur IA"""
        if numero_joueur==0:
            self.nombre_carte_joueur0=self.nombre_carte_joueur0+self.sauvegarde_nombre_carte_postsplit-2
        if numero_joueur==1:
            self.nombre_carte_joueur1=self.nombre_carte_joueur1+self.sauvegarde_nombre_carte_postsplit-2
        if numero_joueur==3:
            self.nombre_carte_joueur3=self.nombre_carte_joueur3+self.sauvegarde_nombre_carte_postsplit-2
        if numero_joueur==4:
            self.nombre_carte_joueur4=self.nombre_carte_joueur4+self.sauvegarde_nombre_carte_postsplit-2

    def nettoyage(self):
        """Nettoie le tapis de jeu"""
        self.assurance=False
        if self.affichage_gagnant_split!=None:
            self.caneva.delete(self.affichage_gagnant_split)
            self.affichage_gagnant_split=None
        if self.text_points_joueur!=None:
            self.caneva.delete(self.text_points_joueur)
            self.caneva.delete(self.image_fond_point)
            self.text_points_joueur=None
        if self.text_points_croupier!=None:
            self.caneva.delete(self.text_points_croupier)
            self.caneva.delete(self.image_fond_point_croupier)
            self.text_points_croupier=None
        compteur=0
        if self.text_blackjack_joueur0!=None:
            self.caneva.delete(self.text_blackjack_joueur0)
        if self.text_blackjack_joueur1!=None:
            self.caneva.delete(self.text_blackjack_joueur1)
        if self.text_blackjack_joueur2!=None:
            self.caneva.delete(self.text_blackjack_joueur2)
        if self.text_blackjack_joueur3!=None:
            self.caneva.delete(self.text_blackjack_joueur3)
        if self.text_blackjack_joueur4!=None:
            self.caneva.delete(self.text_blackjack_joueur4)
        if self.image_carte_double!=0:
            self.caneva.delete(self.carte_double)
            self.image_carte_double=0
            self.nombre_carte=self.nombre_carte-1
            self.caneva.delete(self.text_double)
        high_carte=self.nombre_carte
        high_carte_croupier=self.nombre_carte_croupier
        self.nombre_carte=self.nombre_carte-1
        while self.nombre_carte>0:
            while compteur<3:
                self.caneva.move(self.dictionnaire[high_carte],-10,0)
                self.fenetre.after(5, None)
                self.fenetre.update()
                compteur=compteur+1
            self.caneva.delete(self.dictionnaire[self.nombre_carte])
            self.nombre_carte=self.nombre_carte-1
            compteur=0
        compteur=0
        self.nombre_carte_croupier=self.nombre_carte_croupier-1
        while self.nombre_carte_croupier>0:
            while compteur<6:
                self.caneva.move(self.dictcroupier[high_carte_croupier],-10,0)
                self.fenetre.after(5, None)
                self.fenetre.update()
                compteur=compteur+1
            self.caneva.delete(self.dictcroupier[self.nombre_carte_croupier])
            self.nombre_carte_croupier=self.nombre_carte_croupier-1
            compteur=0
        while self.nombre_carte_joueur>0:
            self.caneva.delete(self.dictjoueur[self.nombre_carte_joueur])
            self.nombre_carte_joueur=self.nombre_carte_joueur-1
        self.text_nouvelle_partie=self.caneva.create_text(550,200,text="N O U V E L L E   P A R T I E",fill="Blue",font=('arial','13','bold'))
            
        self.nombre_carte=0
        self.nombre_carte_croupier=0
        self.nombre_carte_joueur=0
        self.nombre_carte_joueur0=0
        self.nombre_carte_joueur1=0
        self.nombre_carte_joueur3=0
        self.nombre_carte_joueur4=0
        self.split_ok=1
        self.split_ok_joueur=1
        self.caneva.delete(self.affichage_gagnant)
        self.caneva.delete(self.dictionnaire[high_carte])
        self.caneva.delete(self.dictcroupier[high_carte_croupier])

    def bouton_appa(self,nom):
        """Fait apparaitre le bouton specifié en argument"""
        if nom=="bouton_hit":
            self.bouton_hit=self.caneva.create_image(550,712 ,image=self.image_bouton_hit)
        elif nom=="bouton_stand":
            self.bouton_stand=self.caneva.create_image(630,710 ,image=self.image_bouton_stand)
        elif nom=="bouton_double":
            self.bouton_double=self.caneva.create_image(768,708 ,image=self.image_bouton_double)
        elif nom=="bouton_split":
            self.bouton_split=self.caneva.create_image(855,698 ,image=self.image_bouton_split)
        elif nom=="bouton_aide":
            self.bouton_aide=self.caneva.create_image(940,660 ,image=self.image_bouton_aide)
        elif nom=="bouton_assurance":
            self.bouton_assurance=self.caneva.create_image(390,706 ,image=self.image_bouton_assurance)

    def assurance_oui_non(self):
        """Demande au joueur si il veut prendre une assurance"""
        self.assurance=False
        self.bouton_appa("bouton_assurance")
        self.caneva.bind("<Button-1>", self.gestion_clic_assurance)
        self.fenetre.mainloop()

    def gestion_clic_assurance(self,event):
        """Gere le clic lors de l'assurance pour prendre en compte le choix du joueur"""
        self.clic_posx = event.x
        self.clic_posy = event.y
        fin=0
        if self.clic_posx>317 and self.clic_posx<386 and self.clic_posy<734 and self.clic_posy>665:
            self.assurance=True
            self.placement_jetons_assurance(self.mise/2)
            fin=1
        elif self.clic_posx>390 and self.clic_posx<463 and self.clic_posy<734 and self.clic_posy>665:
            self.assurance=False
            fin=1
        if fin==1:
            self.bouton_disp("bouton_assurance")
            self.caneva.unbind("<Button-1>")
            self.fenetre.quit()

    def placement_jetons_assurance(self,mise):
        """Place les jetons de l'assurance sur le tapis de jeu"""
        temp=int(mise//0.5)
        temp=temp*0.5
        self.nombre_jetons_assurance=0
        if mise//50!=0:
            self.nombre_jetons_assurance+=1
            self.dictjetons_assurance[self.nombre_jetons_assurance]=self.caneva.create_image(565,360,image=self.image_jeton50)
            mise=mise-50
        if mise//10!=0:
            temp=mise//10
            while temp>0:
                self.nombre_jetons_assurance+=1
                self.dictjetons_assurance[self.nombre_jetons_assurance]=self.caneva.create_image(565,365-(5*self.nombre_jetons_assurance),image=self.image_jeton10)
                mise=mise-10
                temp=temp-1
        if mise//5!=0:
            self.nombre_jetons_assurance+=1
            self.dictjetons_assurance[self.nombre_jetons_assurance]=self.caneva.create_image(565,365-(5*self.nombre_jetons_assurance),image=self.image_jeton5)
            mise=mise-5
        if self.nombre_jetons_assurance==5:
            move_x_pile=50
            move_y_pile=25
        else:
            move_x_pile=0
            move_y_pile=0
        if int(mise)!=0:
            temp=int(mise)
            while temp>0:
                self.nombre_jetons_assurance+=1
                self.dictjetons_assurance[self.nombre_jetons_assurance]=self.caneva.create_image(565+move_x_pile,365-(5*self.nombre_jetons_assurance)+move_y_pile,image=self.image_jeton1)
                mise=mise-1
                temp=temp-1
        if mise//0.5!=0:
            self.nombre_jetons_assurance+=1
            self.dictjetons_assurance[self.nombre_jetons_assurance]=self.caneva.create_image(565+move_x_pile,365-(5*self.nombre_jetons_assurance)+move_y_pile,image=self.image_jeton05)
    
    def bouton_disp(self,nom):
        """Fait disparaitre le bouton specifié en argument"""
        if nom=="bouton_hit":
            self.caneva.delete(self.bouton_hit)
        elif nom=="bouton_stand":
            self.caneva.delete(self.bouton_stand)
        elif nom=="bouton_double":
            self.caneva.delete(self.bouton_double)
            self.bouton_double=None
        elif nom=="bouton_split":
            self.caneva.delete(self.bouton_split)
        elif nom=="bouton_aide":
            self.caneva.delete(self.bouton_aide)
        elif nom=="bouton_assurance":
            self.caneva.delete(self.bouton_assurance)

    def action_bouton(self):
        """Attend une action sur un bouton de l'interface"""
        self.bouton_valeur=None
        self.caneva.bind("<Button-1>", self.gestion_clic_bouton)
        self.fenetre.mainloop()

    def gestion_clic_bouton(self,event):
        """Gere le clic dans le cas ou le joueur appuis sur un bouton"""
        self.clic_posx = event.x
        self.clic_posy = event.y
        fin=0
        if self.text_pourcentage!=None:
            self.caneva.delete(self.text_pourcentage)
            self.text_pourcentage=None
        if self.clic_posx>514 and self.clic_posx<581 and self.clic_posy<731 and self.clic_posy>666:
            self.bouton_valeur="H"
            fin=1
        elif self.clic_posx>595 and self.clic_posx<661 and self.clic_posy<731 and self.clic_posy>666:
            self.bouton_valeur="R"
            fin=1
        elif self.clic_posx>733 and self.clic_posx<800 and self.clic_posy<730 and self.clic_posy>667 and self.bouton_double!=None:
            self.bouton_valeur="D"
            fin=1
        elif self.clic_posx>821 and self.clic_posx<886 and self.clic_posy<715 and self.clic_posy>653:
            self.bouton_valeur="S"
            fin=1
        elif self.clic_posx>909 and self.clic_posx<974 and self.clic_posy<680 and self.clic_posy>618:
            self.bouton_valeur="A"
            fin=1
        if fin==1:
            self.caneva.unbind("<Button-1>")
            self.fenetre.quit()
            

    def miser(self,argent):
        """Lance l'etape mise pour le joueur "humain" """
        self.argent=argent
        self.entree2.configure(state=NORMAL)
        self.entree2.delete(0,END)
        self.entree2.insert(0,"00.0€")
        self.entree2.configure(state=DISABLED)
        self.bouton_valider=self.caneva.create_image(330,707 ,image=self.image_bouton_valider)
        self.bouton_annuler=self.caneva.create_image(390,707 ,image=self.image_bouton_annuler)
        self.mise=0
        self.nombre_jetons=0
        self.compteur_posjeton1=0
        self.compteur_posjeton2=1
        self.caneva.bind("<Button-1>", self.gestion_clic_mise)
        self.fenetre.mainloop()

    def gestion_clic_mise(self,event):
        """Quand le joueur mise, gere le clic sur les jetons"""
        self.clic_posx = event.x
        self.clic_posy = event.y
        if self.text!=None:
            self.caneva.delete(self.text)
            self.text=None
        if self.clic_posx>21 and self.clic_posx<65 and self.clic_posy<611 and self.clic_posy>572:
            self.placement_jeton(0.5)
        elif self.clic_posx>65 and self.clic_posx<108 and self.clic_posy<630 and self.clic_posy>591:
            self.placement_jeton(1)
        elif self.clic_posx>108 and self.clic_posx<152 and self.clic_posy<650 and self.clic_posy>611:
            self.placement_jeton(5)
        elif self.clic_posx>152 and self.clic_posx<195 and self.clic_posy<671 and self.clic_posy>630:
            self.placement_jeton(10)
        elif self.clic_posx>196 and self.clic_posx<238 and self.clic_posy<690 and self.clic_posy>651:
            self.placement_jeton(50)
        elif self.clic_posx>240 and self.clic_posx<282 and self.clic_posy<709 and self.clic_posy>670:
            self.placement_jeton(100)
        elif self.clic_posx>303 and self.clic_posx<356 and self.clic_posy<725 and self.clic_posy>673:
            if self.mise<=0.5 or self.mise>100 or self.mise>self.argent:
                a=self.nombre_jetons
                while a>0:
                    self.caneva.delete(self.dictjetons[a])
                    a=a-1
                self.mise=0
                self.compteur_posjeton2=1
                self.compteur_posjeton1=0
                self.entree2.configure(state=NORMAL)
                self.entree2.delete(0,END)
                self.entree2.insert(0,"00.0€")
                self.entree2.configure(state=DISABLED)
                self.text=self.caneva.create_text(560,630,text="Vous devez miser entre 1 et 100 et ne pas depasser votre argent !")
                
            else:
                self.fenetre.quit()
                self.caneva.unbind("<Button-1>")
                self.caneva.delete(self.bouton_valider)
                self.caneva.delete(self.bouton_annuler)
                if self.text_nouvelle_partie!=None:
                    self.caneva.delete(self.text_nouvelle_partie)
                    self.text_nouvelle_partie=None
        elif self.clic_posx>363 and self.clic_posx<415 and self.clic_posy<725 and self.clic_posy>673:
            a=self.nombre_jetons
            while a>0:
                self.caneva.delete(self.dictjetons[a])
                a=a-1
            self.nombre_jetons=0
            self.mise=0
            self.compteur_posjeton1=0
            self.compteur_posjeton2=1
            self.entree2.configure(state=NORMAL)
            self.entree2.delete(0,END)
            self.entree2.insert(0,"00.0€")
            self.entree2.configure(state=DISABLED)

    def placement_jeton(self, valeur_jeton):
        """Place les jetons de mise sur le tapis de jeu"""
        self.nombre_jetons=self.nombre_jetons+1
        self.compteur_posjeton1=self.compteur_posjeton1+1
        if self.compteur_posjeton1>5:
            self.compteur_posjeton1=1
            self.compteur_posjeton2=self.compteur_posjeton2+1
        if valeur_jeton==0.5:
            self.dictjetons[self.nombre_jetons]=self.caneva.create_image(440+50*self.compteur_posjeton2,(425-5*self.compteur_posjeton1) ,image=self.image_jeton05)
            self.mise=self.mise+0.5
        elif valeur_jeton==1:
            self.dictjetons[self.nombre_jetons]=self.caneva.create_image(440+50*self.compteur_posjeton2,(425-5*self.compteur_posjeton1) ,image=self.image_jeton1)
            self.mise=self.mise+1
        elif valeur_jeton==5:
            self.dictjetons[self.nombre_jetons]=self.caneva.create_image(440+50*self.compteur_posjeton2,(425-5*self.compteur_posjeton1) ,image=self.image_jeton5)
            self.mise=self.mise+5
        elif valeur_jeton==10:
            self.dictjetons[self.nombre_jetons]=self.caneva.create_image(440+50*self.compteur_posjeton2,(425-5*self.compteur_posjeton1) ,image=self.image_jeton10)
            self.mise=self.mise+10
        elif valeur_jeton==50:
            self.dictjetons[self.nombre_jetons]=self.caneva.create_image(440+50*self.compteur_posjeton2,(425-5*self.compteur_posjeton1) ,image=self.image_jeton50)
            self.mise=self.mise+50
        elif valeur_jeton==100:
            self.dictjetons[self.nombre_jetons]=self.caneva.create_image(440+50*self.compteur_posjeton2,(425-5*self.compteur_posjeton1) ,image=self.image_jeton100)
            self.mise=self.mise+100
        self.entree2.configure(state=NORMAL)
        self.entree2.delete(0,END)
        self.entree2.insert(0,str(float(self.mise))+"€")
        self.entree2.configure(state=DISABLED)

    def movement_argent(self,condition="perdant"):
        """Fait bouger les jetons de mise vers le croupier ou le joueur suivant l'argument"""
        if condition=="gagnant":
            fin_compteur=23
            move_y=10
        else:
            fin_compteur=35
            move_y=-10
        sauve_nombre_jetons=self.nombre_jetons
        compteur_movement=0
        while compteur_movement<fin_compteur:
            a=sauve_nombre_jetons
            while a>0:
                self.caneva.move(self.dictjetons[a],0,move_y)
                a=a-1
            self.caneva.update()
            self.fenetre.after(5,None)
            compteur_movement=compteur_movement+1
        a=sauve_nombre_jetons
        while a>0:
            self.caneva.delete(self.dictjetons[a])
            a=a-1
        self.nombre_jetons=0
        self.mise=0

    def movement_argent_assurance(self,condition="perdant"):
        """Fait bouger les jetons de l'assurance vers le croupier ou le joueur suivant l'argument"""
        if condition=="gagnant":
            fin_compteur=28
            move_y=10
        else:
            fin_compteur=30
            move_y=-10
        sauve_nombre_jetons_assurance=self.nombre_jetons_assurance
        compteur_movement=0
        while compteur_movement<fin_compteur:
            a=sauve_nombre_jetons_assurance
            while a>0:
                self.caneva.move(self.dictjetons_assurance[a],0,move_y)
                a=a-1
            self.caneva.update()
            self.fenetre.after(5,None)
            compteur_movement=compteur_movement+1
        a=sauve_nombre_jetons_assurance
        while a>0:
            self.caneva.delete(self.dictjetons_assurance[a])
            a=a-1
        self.nombre_jetons_assurance=0
        self.assurance=False

    def pause_nouvelle_partie(self):
        """Permet de faire une pause a la fin d'un tour de jeu"""
        self.caneva.bind("<Button-1>", self.fin_pause)
        self.fenetre.mainloop()
    def fin_pause(self,event):
        """Arrete la pause quand l'uilisateur a cliqué n'importe ou sur la fenetre"""
        self.caneva.unbind("<Button-1>")
        self.fenetre.quit()
