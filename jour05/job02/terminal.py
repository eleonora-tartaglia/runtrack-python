# La fonction draw_rectangle() permet de dessiner un rectangle en utilisant deux paramètres : 
# width et height, qui définissent respectivement la largeur et la hauteur

width = int(input("Entrez la largeur du rectangle : "))
height = int(input("Entrez la hauteur du rectangle : "))    
 
 # Utilisez deux boucles imbriquées pour dessiner le rectangle dans le terminal :

    # La première boucle for h in range(1, height+1) parcourt chaque ligne du rectangle, 
    # Tandis que la seconde boucle for w in range(1, width+1) parcourt chaque colonne de chaque ligne.

# Dans chaque itération de la boucle intérieure, le programme utilise des instructions conditionnelles (if, elif, else) 
# pour déterminer quel caractère doit être affiché dans la case actuelle. 


    # Si la colonne est la première ou la dernière : if w == 1 or w == width, le programme affiche un caractère de barre verticale (|) 
    # pour former les bords gauche et droit du rectangle. 

    # Si la ligne est la première ou la dernière elif h == 1 or h == height, le programme affiche un caractère de tiret (-) 
    # pour former les bords supérieur et inférieur du rectangle. 

    # Sinon = else : le programme affiche un espace ( ) pour remplir l'intérieur du rectangle.

def draw_rectangle(width,height):
    
    for h in range (1, height+1):
        
        for w in range (1, width+1):
            if w == 1 or w == width:
                print ("| " , end="")
                
            elif h == 1 or h == height:
                print ("- ", end="")
                
            else: 
                print ("  " , end = "")
            
        print()

draw_rectangle(width,height)
        
