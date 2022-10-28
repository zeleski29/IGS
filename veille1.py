import numpy as np

nb= int(input(" entrer le nombre a classer"))

tab= np.zeros(nb,int)

for i in range(nb):
    tab[i]=int(input("Entrer une valeur"))
print(tab)
