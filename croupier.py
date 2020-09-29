import random

class Croupier(Carte):

  def __init__(self):
    pass

  def nouvelle_donne():
    nd = Carte()

  def melanger():
    paquet=[]
    paquet_m=[]

    while len(paquet_m)!=52:
      a=random.randint(0,51)
      if paquet[a]!=0:
        paquet_m.append(paquet[a])
        paquet[a]=0

    return paquet
  
  def couper():
    paquet=[]
    l1=[]
    l2=[]
    a=random.randint(0,51)
    
    for i in range(0,a):
      l1.append(paquet[i])
    for i in range (a,51):
      l2.append(paquet[i])
    
    paquet=l2+l1
    return paquet

  def distribuer():
    pass
