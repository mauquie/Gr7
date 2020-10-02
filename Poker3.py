import pokerlib

class Joueur(Croupier
             ):

    def __init__(self,Nom=input("Entrez votre nom : "),Main=[],Tapis=1000):
        self.Nom=Nom
        self.Main=Main
        self.Tapis=Tapis
        
    
        
        
    
    def Nouvelle_donne(self):
        # réinitialise la main du joueur (le plus de carte en main)
    
    
    def Evaluer(self,Combinaison):
        if Combinaison1 > Combinaison2:
            print("La Main 1 est plus forte que la Main 2") 
        elif combinaison1 == combinaison2 :
            print("La Main 1 et la Main 2 ont la même valeur") 
        else:
            print("La Main 2 est plus forte que la Main 1")
            # ou encore combinaison_max = max([combinaison1, combinaison2])
        
        
    def Recevoir_carte(self):  
        
        
    
Main1 = [Carte(), Carte(), Carte(), Carte(), Carte()] 
Main2 = [Carte(), Carte(), Carte(), Carte(), Carte()]
Combinaison1 = pokerlib.Combinaison(main1)
Combinaison2 = pokerlib.Combinaison(main2)
print(Combinaison1.name(), Combinaison2.name())



