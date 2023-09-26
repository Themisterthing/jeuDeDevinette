#Thomas Parent
# 12 septembre 2023
# TP2
from random import *
Essai = 0

nombre = randint(0, 1)

print("J’ai choisi un nombre au hasard entre 1 et 1000.\n À vous de le deviner...")

choix = int(input("Entrer un nombre: "))
Essai = Essai +1
while nombre!= choix:
   if choix < nombre:
       print("Trop bas")
       Essai = Essai + 1
       choix = int(input("Entrer un nouveau nombre: "))
   elif choix > nombre:
       print("Trop haut!")
       Essai = Essai + 1
       choix = int(input("Entrer un nouveau nombre: "))
   else:
     break
print("Tu l'a trouvé en",Essai,"essais!!")
