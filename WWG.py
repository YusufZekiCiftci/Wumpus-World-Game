#Wumpus World Game

"""
wumpus hayaleti oyununun amacı 4x4 16 birimlik haritada Altın(G) ı bulmaktır.
Bunlardan ayrı olarak oyunda wumpus hayaleti ve çukurlar bulunmaktadır.
Çukurların olduğu karelerin hemen yanındaki karelerde rüzgar(B) esmekte, 
Wumpus hayaleti olduğu karenin hemen yanındaki karelerde ise kötü bir
koku hissedilmektedir(S). Eğer oyuncu altına yakın ise altının bulunduğu karenin
hemen yanındaki karelerde parıltı gözükür. Oyuncu(P) ,Wumpus(W) dur.
"""

import random

def gameArea():
    line=[0,0]
    shape1="*****************************************"
    shape2="*         *         *         *         *" 
    
    print("            Wumpus World Game            ", end="\n\n")
    while True:
        if line[0]==21:
            break
        elif line[0]%5==0:
            print(shape1)
            line[0]+=1
        else :
            print(shape2)
            line[0]+=1


def coordinate(x,y):
    a=0
    b=0
#x koordinatı
    if 0<x<10 :
        a=1
    elif 10<x<20 :
        a=2
    elif 20<x<30 :
        a=3
    elif 30<x<40 :
        a=4
#y koordinatı
    if 0<y<5 :
        b=4
    elif 5<y<10 :
        b=3
    elif 10<y<15 :
        b=2
    elif 15<y<20 :
        b=1
        
    print(a,b)
    
def randomCoord():
    x=random.randint(1, 4)
    y=random.randint(1, 4)
    return x,y
    
gameArea()

#Objeleri atamak için kullandım.
while True:
    playerCoordX, playerCoordY=1,1
    wumpusCoordX, wumpusCoordY=randomCoord()
    goldCoordX, goldCoordY=randomCoord()
    pitCoordX, pitCoordY=randomCoord()
    
    if (playerCoordX !=wumpusCoordX or playerCoordY !=wumpusCoordY) and (playerCoordX !=goldCoordX or playerCoordY !=goldCoordY) and (playerCoordX !=pitCoordX or playerCoordY !=pitCoordY) and (goldCoordX !=wumpusCoordX or goldCoordY !=wumpusCoordY) and (goldCoordX !=pitCoordX or goldCoordY !=pitCoordY) and (wumpusCoordX !=pitCoordX or wumpusCoordY !=pitCoordY):
        break
    
        


