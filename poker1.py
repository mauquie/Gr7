import random

class Carte:
    """
    Constructeur qui initialisation les couleurs et les rangs des cartes
    """
    def __init__(self):
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

    def distribuer(self):   #Méthode: Distribuer au joueur
        pass

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
