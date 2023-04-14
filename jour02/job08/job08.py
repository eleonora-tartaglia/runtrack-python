def compote(type,saison):
    if type == 'fruits' and saison == 'hiver':
        print('ce sont ces ingredients' , "orange,mandarine,kiwi")
        
    
    elif type == 'fruits' and saison == 'été':
        print('ce sont ces ingredients' , "poire,fraise,cassis")
        
    
    elif type =='legumes' and saison == 'hiver':
        print('ce sont ces ingredients' , "carotte,topinambour,endive")


    elif type == 'legumes' and saison == 'été':
        print('ce sont ces ingredients' , "artichaut,aubergine,navet")
    
    else:
        print("inconnu au bataillon")


compote('fruits','hiver')
compote('legumes', 'été')
compote('graines','automne')
