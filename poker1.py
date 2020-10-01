import random

class Partie:

    def __init__(self):
        pass

    def joueurs(self):
        self.liste_joueurs=[]
        self.nombre_joueurs=int(input("Entrer le nombre de joueur: "))
        k=0
        for i in range (nombre_joueurs):
            k=k+1
            self.liste_joueurs.append(str(input("Entrer le nom du joueur {0}: ".format(k))))

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

    def __init__(self, nom="Joueur", main=None, tapis=500):
        Croupier.__init__(self)
        self.nom=nom
        self.main=main
        self.tapis=tapis

    def vider_main(self):
        self.main=[]

    def recevoir_main(self):
        if len(self.main)!=0:
            vider_main()
        for i in range (5):
            self.main.append(self.paquet[-1])
            self.paquet.pop()

class Coup(Croupier,Partie):

    def __init__(self):
        Joueur.__init__(self)
        Croupier.__init__(self)
        Partie.__init__(self)

    def nouvelle_donne(self):
        for i in range (0,self.nombre_joueurs):
            liste_joueurs[i]=Joueurs(liste_joueurs[i])
            liste_joueurs[i].recevoir_main()
    
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
