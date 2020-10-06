import random
import pokerlib

class Partie:

    joueurs = [] #Initilisation de la liste des joueurs
    
    def __init__(self):
        pass

    def jouer(self, nom="Joueur", tapis="500"): #Méthode: Initilisation des joueurs
        joueur = Joueur(tapis,nom)
        Partie.joueurs.append(joueur)

class Carte:

    def __init__(self, couleur, rang): #Constructeur: Initialisation des couleurs et des rangs des cartes
        self.rang=rang
        self.couleur=couleur

    def __repr__(self):
        return f"{self.rang}{self.couleur}"

class Croupier:

    def __init__(self):
        #Carte.__init__(self)    #Appel de la classe mère
        self.paquet=[]  #Initialisation du paquet
        
    def rassembler(self):   #Méthode: Crée le paquet
        for couleur in ["P","C","K","T"]:
          for rang in ["2","3","4","5","6","7","8","9","X","V","D","R","A"]:
            carte = Carte(couleur, rang)
            self.paquet.append(carte)

    def melanger(self): #Méthode: Mélange le paquet
        random.shuffle(self.paquet)

    def couper(self):   #Méthode: Coupe le paquet
        liste_t1=[]     #Liste temporaire 1
        liste_t2=[]     #Liste temporaire 2
        a=random.randint(0,52)  #Valeur aléatoire
        for i in range(0,a):
          liste_t1.append(self.paquet[i])   #Ajoute de [0] à [a] les éléments de paquet à la liste temporaire 1
        for i in range (a,52):
          liste_t2.append(self.paquet[i])   #Ajoute de [a] à [52] les éléments de paquet à la liste temporaire 2

        self.paquet=liste_t2+liste_t1       #Paquet est maintenant égal à liste temporaire 2 plus liste temporaire 1

    def nouvelle_donne(self):   #Méthode: Crée un paquet en le mélangeant puis en le coupant
        self.rassembler()
        self.melanger()
        self.couper()

    def distribuer(self, n): #Méthode: Distribue 5 cartes à chaque joueurs
        for i in range(len(Partie.joueurs)):
            for j in range(n):
                Partie.joueurs[i].recevoir_main(self.paquet[0])
                self.paquet.pop(0)

class Joueur(Croupier):

    def __init__(self, tapis, nom):
        Croupier.__init__(self)
        self.nom=nom
        self.main=[]
        self.tapis=tapis

    def vider_main(self): #Méthode: Supprime la main du joueur
        self.main.clear()

    def recevoir_main(self, carte):
        self.main.append(carte)

    def evaluer(self): #Méthode: Permet de savoir quel main est la plus forte
        if Combinaison1 > Combinaison2:
            print("La Main 1 est plus forte que la Main 2") 
        elif Combinaison1 == Combinaison2 :
            print("La Main 1 et la Main 2 ont la même valeur") 
        else:
            print("La Main 2 est plus forte que la Main 1")
            # ou encore combinaison_max = max([combinaison1, combinaison2])

    def __repr__(self):
        return f"{self.nom}"

class Coup(Croupier,Partie):

    def __init__(self):
        Croupier.__init__(self)
        Partie.__init__(self)

    def nouvelle_donne(self):
        pass

"""
Test:
- Croupier
- Initialisation de 2 joueurs
- Comparaison de deux mains (joueur 1 et 2)
"""

def test_paquet():
    return print(f"{a.paquet}\nLongeur du paquet: {len(a.paquet)}\n")
    
new = Partie()
new.jouer("Tony")
new.jouer("Alexandre")

a = Croupier()
a.nouvelle_donne()
test_paquet()

a.distribuer(5)
test_paquet()

for i in range (0,len(new.joueurs)):
    print(f"Le joueur n°{i} est {new.joueurs[i]} et sa main est {new.joueurs[i].main}\n")

Combinaison1 = pokerlib.Combinaison(new.joueurs[0].main)
Combinaison2 = pokerlib.Combinaison(new.joueurs[1].main)
print("Main 1:",Combinaison1.name(),"\nMain 2:",Combinaison2.name())

new.joueurs[0].evaluer()
