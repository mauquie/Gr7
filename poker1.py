class Carte:

  def __init__(self,paquet):
    self.paquet=paquet

  def initialisation(self): #Méthode: Création du paquet de carte
    couleur=["P","C","K","T"]
    rang=["2","3","4","5","6","7","8","9","10","V","D","R","A"]
    paquet=[[] for i in range(52)]
    compteur=0
    for i in range (4):
      for j in range (13):
        paquet[compteur].append(rang[j])
        paquet[compteur].append(couleur[i])
        compteur=compteur+1
    self.paquet = paquet
