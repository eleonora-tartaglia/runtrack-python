# afficher la valeur de L[1]

L = [2,4,8,16,18]
print(" la deuxième valeur de L est",L[1])

# remplacer L[3] par la somme des cases voisines L[2] & L[4]

def remplacer_valeur():
    L[3] = L[2] + L[4]
    print(L[3])
    print(L)
    
remplacer_valeur()

# afficher la derniere valeur

print("la derniere valeur de L est",L[-1])


