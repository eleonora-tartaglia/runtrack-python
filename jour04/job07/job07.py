# Definir la liste

L = [8, 24, 48, 2, 16]

# Initialiser le compteur à zero car la variable compteur n'a pas encore de valeur initiale

compteur = 0

# Parcourir les elements de la liste 

for i in L:

# Verifier si l'element est un multiple de 3

    if i % 3 == 0:

# Si affirmatif incrementer la valeur

        compteur += 1

print("Il y a", compteur, "multiples de 3 dans la liste")
    