

import random

for xxx in range(1, 2):
    puntos=0




    for xxx in range(4):
        numerito = random.randint(1, 4)


        if(numerito==1):
            print("💛")
            puntos=puntos+1

        if(numerito==2):
            print("🍬")  
            puntos=puntos+2

        if(numerito==3):
            print("🎁")
            puntos=puntos+3

        if(numerito==4):
            print("✨") 
            puntos=puntos+4

    print(puntos) 