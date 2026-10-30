
# Codigo 1

# for xxxx in range(15):
#     print("Teño fame")
# print("Vou comer")    

# for numElefantes in range(6):
# 	print(numElefantes, " elefantes se balanceaban sobre la tela... ")


# for cuenta in range(1,51): 
# 	print(cuenta,"cuenta")

# resp =   input("Quieres que te cuente “El cuento de la buena pipa” ?")

import random
secreto = random.randint(0, 100)



for xxx  in range(5):
    contestado = input("Que número dis? Entre 1 e 100   "  )
    resp = int(contestado)

    if(resp == secreto):
        print("Correcto") 
        break
    if(resp<secreto):
        print("el numero secreto es Mayor")

    if(resp>secreto):
        print("el numero secreto es menor")  


