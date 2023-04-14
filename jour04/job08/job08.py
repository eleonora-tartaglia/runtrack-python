# Definir la liste 
 
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

# Initialiser la variable somme a zero

somme = 0

# Parcourir chaque element de la liste

for i in L:

# Verifier si l'element est pair

    if i % 2 == 0:

# Si affirmatif incrementer la valeur

        somme += i
        
# Afficher la somme des elements pairs

print("la somme des elements pairs de la liste est ", somme )


