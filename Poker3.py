class Joueur(carte):

    def __init__(self,Nom=input("Entrez votre nom : "),Main=[],Tapis=50):
        self.Nom=Nom
        self.Main=Main
        self.Tapis=Tapis
        
    
    def Nouvelle_donne(self):
        # réinitialise la main du joueur (le plus de carte en main)
    
    
    def Evaluer(self,couleur,rang):
        
        
        
        CarteForte=(,,,,) # la main la plus faible (FACULTATIF POUR L'INSTANT)
        Paire=(,,,,)
        DeuxPaires=(,,,,)
        Brelan=(,,,,)
        Suite=(,,,,)
        Couleur=(,,,,)
        Full=(,,,,)
        Carré=[P,A],[C,A],[K,A],[T,A],[]
        
        QuinteFlush11=[[P,2],[P,3],[P,4],[P,5],[P,6]]
        QuinteFlush12=[[C,2],[C,3],[C,4],[C,5],[C,6]]
        QuinteFlush13=[[K,2],[K,3],[K,4],[K,5],[K,6]]
        QuinteFlush14=[[T,2],[T,3],[T,4],[T,5],[T,6]]
        
        QuinteFlush21=[[P,3],[P,4],[P,5],[P,6],[P,7]]
        QuinteFlush22=[[C,3],[C,4],[C,5],[C,6],[C,7]]
        QuinteFlush23=[[K,3],[K,4],[K,5],[K,6],[K,7]]
        QuinteFlush24=[[T,3],[T,4],[T,5],[T,6],[T,7]]
        
        QuinteFlush31=[[P,4],[P,5],[P,6],[P,7],[P,8]]
        QuinteFlush32=[[C,4],[C,5],[C,6],[C,7],[C,8]]
        QuinteFlush33=[[K,4],[K,5],[K,6],[K,7],[K,8]]
        QuinteFlush34=[[T,4],[T,5],[T,6],[T,7],[T,8]]
    
        QuinteFlush41=[[P,5],[P,6],[P,7],[P,8],[P,9]]
        QuinteFlush42=[[C,5],[C,6],[C,7],[C,8],[C,9]]
        QuinteFlush43=[[K,5],[K,6],[K,7],[K,8],[K,9]]
        QuinteFlush44=[[T,5],[T,6],[T,7],[T,8],[T,9]]
        
        QuinteFlush51=[[P,6],[P,7],[P,8],[P,9],[P,10]]
        QuinteFlush52=[[C,6],[C,7],[C,8],[C,9],[C,10]]
        QuinteFlush53=[[K,6],[K,7],[K,8],[K,9],[K,10]]
        QuinteFlush54=[[T,6],[T,7],[T,8],[T,9],[T,10]]
        
        QuinteFlush61=[[P,7],[P,8],[P,9],[P,10],[P,V]]
        QuinteFlush62=[[C,7],[C,8],[C,9],[C,10],[C,V]]
        QuinteFlush63=[[K,7],[K,8],[K,9],[K,10],[K,V]]
        QuinteFlush64=[[T,7],[T,8],[T,9],[T,10],[T,V]]
        
        QuinteFlush71=[[P,8],[P,9],[P,10],[P,V],[P,D]]
        QuinteFlush72=[[C,8],[C,9],[C,10],[C,V],[C,D]]
        QuinteFlush73=[[K,8],[K,9],[K,10],[K,V],[K,D]]
        QuinteFlush74=[[T,8],[T,9],[T,10],[T,V],[T,D]]
        
        QuinteFlush71=[[P,8],[P,9],[P,10],[P,V],[P,D]]
        QuinteFlush72=[[C,8],[C,9],[C,10],[C,V],[C,D]]
        QuinteFlush73=[[K,8],[K,9],[K,10],[K,V],[K,D]]
        QuinteFlush74=[[T,8],[T,9],[T,10],[T,V],[T,D]]
        
        QuinteFlush81=[[P,9],[P,10],[P,V],[P,D],[P,R]]
        QuinteFlush82=[[C,9],[C,10],[C,V],[C,D],[C,R]]
        QuinteFlush83=[[K,9],[K,10],[K,V],[K,D],[K,R]]
        QuinteFlush84=[[T,9],[T,10],[T,V],[T,D],[T,R]]
        
        QuinteFlushRoyale11=[[P,10],[P,V],[P,D],[P,R],[P,A]]
        QuinteFlushRoyale12=[[C,10],[C,V],[C,D],[C,R],[C,A]]
        QuinteFlushRoyale13=[[K,10],[K,V],[K,D],[K,R],[K,A]]
        QuinteFlushRoyale14=[[T,10],[T,V],[T,D],[T,R],[T,A]]
        
        
        
        
       
        
        
        
        
    def Recevoir(self):
        #Donne de nouvelles cartes au joueur (fournies par Croupier)
        #En attente de croupier
        
    





