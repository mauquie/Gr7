import as poker1

class Joueur:

    def __init__(self,Nom='',Main=#???,Tapis=50,Combinaison=Combinaison):
        self.Nom=Nom
        self.Main=#???
        self.Tapis=Tapis
        self.Combinaison=Combinaison

    def Nouvelle_donne(self):
        #réinitialise la main du joueur(le plus de carte en main)

    
    
    
    
    def Evaluer():
        
        
    

    def Recevoir(self):
        #donne de nouvelles Cartes au joueur (fournies par Croupier)
        
import pokerlib

main1 = [Carte(), Carte(), Carte(), Carte(), Carte()] 

main2 = [Carte(), Carte(), Carte(), Carte(), Carte()] 

combinaison1 = pokerlib.Combinaison(main1) 

combinaison2 = pokerlib.Combinaison(main2) 

print(combinaison1.name(), combinaison2.name())

if combinaison1 > combinaison2: 
    print(‘main1 est plus forte que main2’) 

elif combinaison1 == combinaison2 : 
    print(‘main1 et main2 ont la même valeur’) 

else: 
    print(‘main2 est plus forte que main1’)
# ou encore combinaison_max = max([combinaison1, combinaison2])