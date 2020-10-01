import pokerlib

class Joueur:

    def __init__(self,Nom='',Main=[],Tapis=50,Combinaison=Combinaison):
        self.Nom=Nom
        self.Main=Main
        self.Tapis=Tapis
        self.Combinaison=Combinaison

    def Nouvelle_donne(self):
        #réinitialise la main du joueur(le plus de carte en main)

    
    
    
    def Evaluer():
       if Combinaison1 > Combinaison2: 
           print("La Main1 est plus forte que la Main2") 
       elif Combinaison1 == Combinaison2 : 
             print("La Main1 et Main2 ont la même valeur") 
       else: 
           print("La Main2 est plus forte que la Main1")
           # ou encore combinaison_max = max([combinaison1, combinaison2]) 
        
    

    def Recevoir(self):
        #Donne de nouvelles cartes au joueur (fournies par Croupier)
        #En attente de croupier


Main1 = [Carte(), Carte(), Carte(), Carte(), Carte()]
Main2 = [Carte(), Carte(), Carte(), Carte(), Carte()] 
Combinaison1 = pokerlib.Combinaison(Main1) 
Combinaison2 = pokerlib.Combinaison(Main2) 
print(Combinaison1.name() , Combinaison2.name())