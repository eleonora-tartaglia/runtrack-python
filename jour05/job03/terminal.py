# La première boucle for parcourt les n+1 lignes du tapis, et la seconde boucle for parcourt les n+1 colonnes de chaque ligne. 
# Pour chaque case (a,b) du tapis, le programme utilise une instruction conditionnelle pour décider si elle doit contenir un caractère x 
# (pour les cases traversées par la diagonale) ou un tiret (-) pour les autres cases.

# La première boucle for parcourt les lignes du tapis, de 0 à n inclus. 
# La deuxième boucle for parcourt les colonnes du tapis, également de 0 à n inclus.


n = 10


def dessine_moi_un_tapis(n):
    
    for a in range (n):
        
        for b in range (n):
            if a == 0 and b == 0:
                print ("+" , end="")
            
            elif a == 0 and b == n-1:
                print ("+", end="")
            
            elif a == n-1 and b == 0:
                print ("+", end="")
            
            elif a == n-1 and b == n-1:
                print ("+", end="")
        
            elif b == 1 or b == n-1:
                print ("|" , end="")
                
            elif a == 0 or a == n-1:
                print ("-", end="")
            
            elif a == b or a == n-b:
                print (" ", end="")
                
            else:
                print ("#" , end = "")
            
        print()

dessine_moi_un_tapis(n)

