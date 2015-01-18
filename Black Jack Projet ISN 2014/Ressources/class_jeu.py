from class_joueur import*
import module_carte as carte

class Jeu:          #Classe qui s'occupe de notre jeux de carte
    """Classe qui représente un jeu de carte, un même joueur peut en avoir 2 s'il prend un split"""
    def __init__(self,parie,x=False):       #Initialisation avec en argument notre mise
        self.bet=parie      #Ce que nous avons miser sur ce jeu de carte
        self.pts=0          #Sa valeur
        self.pts_min=0
        self.cartes=[]      #Les cartes qu'il aura
        if x==False:
            self.cartes.append(carte.tirer())
        else:
            self.cartes.append(x)           #Dans le cas ou nous avons deja une carte (cas des split)
        self.cartes.append(carte.tirer())


    def points(self):           #Permet de calculer nos points
        """Calcul les points pour un joueur et garde en plus les points minimum pour les stats"""
        tab_pts=[0]             #Toujours l'appeler avant de demander les points car la valeur peut changer lorsquon tire une carte
        for i in range (len(self.cartes)):
            if (self.cartes[i])//4==0:
                for j in range(len(tab_pts)):
                    tab_pts.append(tab_pts[j])
                    tab_pts[j]+=1
                    tab_pts[j+1]+=11
            elif (self.cartes[i])//4>=9:
                for j in range(len(tab_pts)):
                    tab_pts[j] +=10
            else:
                for j in range(len(tab_pts)):
                    tab_pts[j] +=((self.cartes[i])//4)+1

        self.pts_min=tab_pts[0]
        if tab_pts[0]<=21:
            for i in range (len(tab_pts)):
                if tab_pts[len(tab_pts)-i-1]<=21:
                    self.pts=tab_pts[len(tab_pts)-i-1]
                    break
        else:
            self.pts=tab_pts[0]
            
                
        
