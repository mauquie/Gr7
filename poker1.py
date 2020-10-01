import random

class Partie:
    
    def __init__(self):
        nombre_joueurs(input("Entrer le nombre de joueur: "))
        for i in range (nombre_joueurs):
            nom=str(input("Entrer le nom du joueur: "))
            nom = Joueur()
    pass
    
class Carte:

    def __init__(self): #Constructeur: Initialisation des couleurs et des rangs des cartes
        self.couleur=["P","C","K","T"]
        self.rang=["2","3","4","5","6","7","8","9","10","V","D","R","A"]

class Croupier(Carte):

    def __init__(self):
        Carte.__init__(self)    #Appel de la classe mère
        self.paquet=[]  #Initialisation du paquet
        
    def rassembler(self):   #Méthode: Créer le paquet
        self.paquet=[[] for i in range(52)] #Créer les 52 places du paquet
        compteur=0
        for i in range (4):
          for j in range (13):
            self.paquet[compteur].append(self.rang[j])
            self.paquet[compteur].append(self.couleur[i])
            compteur=compteur+1
    
    def melanger(self): #Méthode: Mélanger le paquet
        random.shuffle(self.paquet)

    def couper(self):   #Méthode: Couper le paquet
        liste_t1=[]     #Liste temporaire 1
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

    def __init__(self, nom="Joueur", main=0, tapis=500):
        Croupier.__init__(self)
        self.nom=nom
        self.main=main
        self.tapis=tapis

    def vider_main(self):
        for i in range (2):
            self.main.pop()

    def recevoir_main(self):
        if len(self.main)!=0:
            vider_main()
        for i in range (2):
            self.main.append(self.paquet[-1])
            self.main.pop()
            
#Programme principal
test = Croupier()
print(len(test.paquet))
print(test.paquet)

test.rassembler()
print(len(test.paquet))
print("\n",test.paquet)

test.melanger()
print(len(test.paquet))
print("\n",test.paquet)

test.couper()
print(len(test.paquet))
print("\n",test.paquet)