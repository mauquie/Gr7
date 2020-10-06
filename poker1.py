import random
import pokerlib

class Partie:

    joueurs = []
    
    def __init__(self):
        pass

    def jouer(self, tapis="500", nom="Joueur"):
        joueur = Joueur(tapis,nom)
        Partie.joueurs.append(joueur)

class Carte:

    def __init__(self): #Constructeur: Initialisation des couleurs et des rangs des cartes
        self.rang=["2","3","4","5","6","7","8","9","10","V","D","R","A"]
        self.couleur=["P","C","K","T"]  

class Croupier(Carte):

    def __init__(self):
        Carte.__init__(self)    #Appel de la classe mère
        self.paquet=[]  #Initialisation du paquet
        
    def rassembler(self):   #Méthode: Créer le paquet
        for couleur in self.couleur:
          for rang in self.rang:
            self.paquet.append([rang+couleur])

    def melanger(self): #Méthode: Mélanger le paquet
        random.shuffle(self.paquet)

    def couper(self):   #Méthode: Couper le paquet
        liste_t1=[]     #Liste temporaire  1
        liste_t2=[]     #Liste temporaire 2
        a=random.randint(0,52)  #Valeur aléatoire
        for i in range(0,a):
          liste_t1.append(self.paquet[i])   #Ajouter de [0] à [a] les éléments de paquet à la liste temporaire 1
        for i in range (a,52):
          liste_t2.append(self.paquet[i])   #Ajouter de [a] à [52] les éléments de paquet à la liste temporaire 2

        self.paquet=liste_t2+liste_t1       #Paquet est maintenant égal à liste temporaire 2 plus liste temporaire 1

    def nouvelle_donne(self):   #Méthode: Créer un paquet en le mélangeant puis en le coupant
        self.rassembler()
        self.melanger()
        self.couper()

class Joueur(Croupier):

    def __init__(self, tapis, nom, combinaison):
        Croupier.__init__(self)
        self.nom=nom
        self.main=[]
        self.tapis=tapis

    def vider_main(self):
        self.main.clear()

    def Evaluer(self,Combinaison):
        if Combinaison1 > Combinaison2:
            print("La Main 1 est plus forte que la Main 2") 
        elif combinaison1 == combinaison2 :
            print("La Main 1 et la Main 2 ont la même valeur") 
        else:
            print("La Main 2 est plus forte que la Main 1")
            # ou encore combinaison_max = max([combinaison1, combinaison2])

    def recevoir_main(self):
        if len(self.main)!=0:
            Joueur.vider_main()
        for i in range (5):
            self.main.append(self.paquet[-1])
            self.paquet.pop()

class Coup(Croupier,Partie):

    def __init__(self):
        Croupier.__init__(self)
        Partie.__init__(self)

    def nouvelle_donne(self):
        pass

"""   
def test_croupier():
    a = Croupier()
    paquet=a.paquet
    def afficher_paquet(paquet):
        print("Longeur du paquet: ",len(a.paquet))
        print("\n",a.paquet,"\n")

    afficher_paquet(paquet)

    a.rassembler()
    afficher_paquet(paquet)

    a.melanger()
    afficher_paquet(paquet)

    a.couper()
    afficher_paquet(paquet)

test_croupier()
"""

Main1 = [Carte(), Carte(), Carte(), Carte(), Carte()] 
Main2 = [Carte(), Carte(), Carte(), Carte(), Carte()]
Combinaison1 = pokerlib.Combinaison(main1)
Combinaison2 = pokerlib.Combinaison(main2)
print(Combinaison1.name(), Combinaison2.name())
