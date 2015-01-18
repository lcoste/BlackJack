from class_jeu import*
import module_carte as carte
from random import*

class Joueur:
    """Classe pour les différents joueurs de blackjack"""

    def __init__(self,argent_debut):
        self.argent=argent_debut    #L'argent du joueur
        self.blackjack=False        #S'il a un blackjack
        self.en_jeu=False       #S'il a fini avec son/un de ses jeu(x)
        self.jouer=False        #Il me semble inutiles a voir
        self.assurance_prise=False      #Si on na pris une assurance

    def play(self,montant):    
        """Permet de parier, et ainsi tirer des cartes"""
        self.jeu_de_carte=[]    #Les differents jeux qu'on peut avoir (dans les cas de split)
        self.jeu_de_carte.append(Jeu(montant))  #On cree notre jeu(On tire les cartes
        self.argent -=montant       
        self.jeu_de_carte[0].points()
        self.en_jeu=True
        self.blackjack=False
        if self.jeu_de_carte[0].pts==21:        #On verifie si blackjack
            self.blackjack=True
            self.en_jeu=False
        self.assurance_prise=False
        

    def hit(self,i=0):          
        """Action de tirer une carte, HIT"""
        self.jouer=True         #En argument le jeu sur lequel on joue (ne concerne que l'IA)
        self.jeu_de_carte[i].cartes.append(carte.tirer())
        self.jeu_de_carte[i].points()
        if self.jeu_de_carte[i].pts==21:        #On verifie si on atteint 21 ou plus, dans ce cas on a fini
            #BLACKJACK (plus ou moins)
            self.en_jeu=False
        if self.jeu_de_carte[i].pts > 21:
            #BUSTED
            self.en_jeu=False
            
    def stay(self):     #Lorsqu'on veut s'arreter
        """Action de s"arreter de jouer, STAY"""
        self.jouer=True
        self.en_jeu=False
        ##fin jeu##
        
    def double(self,i=0):
        """Action du double, DOUBLE"""
        self.jouer=True         #En argument le jeu sur lequel on joue (ne concerne que l'IA)
        self.argent -= self.jeu_de_carte[i].bet
        self.jeu_de_carte[i].bet=self.jeu_de_carte[i].bet*2
        self.jeu_de_carte[i].cartes.append(carte.tirer())
        self.en_jeu=False
        ##fin jeu##
        
    def split(self):
        """Action de split, SPLIT"""
        self.jouer=True
        montant=self.jeu_de_carte[0].bet
        carte1=self.jeu_de_carte[0].cartes[0]
        carte2=self.jeu_de_carte[0].cartes[1]
        self.jeu_de_carte.append(Jeu(montant,carte1))   #Creation de nouveaux jeu de cartes
        self.jeu_de_carte.append(Jeu(montant,carte2))
        self.jeu_de_carte.pop(0)
        self.argent -= montant

             
    def assurance(self):
        """Appeler lorsqu'on prend l'assurance"""
        self.argent -= (self.jeu_de_carte[0].bet)/2
        self.assurance_prise=True


    ###def AI###            #Les fonctions qui determine ce que l'IA fait
        
    def IA_parie(self):
        """Permet a l'IA de déterminer son parie avec une chance de parier plus que d'habitude"""
        parie=self.argent/50        #En fonction de son argent
        if parie < 1:
            parie=1
        elif parie < 10:
            parie=round(parie)
        elif parie <= 100:
            parie=10*round(parie/10)
        else:
            parie=100
        if randrange(15)==0:        #De temps en temps il est pris d'un coup de folie
            x=randint(2,5)
            if parie*x<=self.argent:
                parie=parie*x
            if parie>100:
                parie=100
        #print("IA parie",parie)
        self.play(parie)

    def IA_assurance(self):
        """Determine si l'IA va prendre ou pas une assurance"""
        self.jeu_de_carte[0].points #En fonction de son argent et de ses cartes
        x=round((self.jeu_de_carte[0].pts/4)+round(self.argent/100))+1
        if randrange(x)==0:
            #print("Assurance prise")
            self.assurance()
        #else:
            #print("Assurance pas prise")
            

    def IA_split(self):
        """Determine si l'IA va prendre un split"""
        x=round(self.argent/200)+1  #En fonction de son argent
        if randrange(x)!=0:
            #print("IA split")
            self.split()
            return True
        return False

    def IA_double(self,i):
        """Determine si l'IA va prendre un double"""
        self.jeu_de_carte[i].points()   #En fonction de son argent et ses cartes
        x=self.jeu_de_carte[i].pts
        y=16-int(self.jeu_de_carte[i].bet/21)
        #print("y:",y)
        x=round((abs((x-y)/1.5)**2.5)+4)
        if randrange(x)==0:
            #print("IA double")
            self.double()
            return True
        return False

    def IA_hit(self,i):
        """Determine si l'IA va tirer une carte"""
        self.jeu_de_carte[i].points()   #En fonction de ses cartes
        intervalle=21-self.jeu_de_carte[i].pts
        if intervalle<=0:
            intervalle=10e-20
        x=int(500*(intervalle**-3))
        if randrange(x+1)==0:
            #print("IA hit")
            self.hit(i)
            return True
        else:
            #print("IA stay")        #Sinon il s'arrete
            self.stay()
            return False
