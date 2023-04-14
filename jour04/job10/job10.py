# Definir ma liste

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser la variable produit à 1 car c'est la valeur neutre pour une multiplication

produit = 1

# Parcourir chaque valeur dans la liste à l'aide d'une boucle for

for i in L:
    
# Verifier si elle rentre dans l'intervalle à l'aide d'une condition if

    if i >= 25 and i <= 90:
        
# Mise à jour de la variable produit : si affirmatif on multiplie la valeur actuelle par la nouvelle valeur
        produit = produit * i
        
# Afficher le resulat

print ("le produit des valeurs comprises dans l'intervalle [25 ; 90] est", produit )