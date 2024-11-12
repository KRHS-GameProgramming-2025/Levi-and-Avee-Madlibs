from madlibgetword import *

def story4(debug=False):
    if debug: print("welcome to story 4")
    
    
    
    
    friendname1 = getWord("enter a name :", debug)
    food1 = getfood("enter a food :", debug)
    restaurant1 = getrestaurant("enter a reataurant :", debug)
    car1 = getcar("enter a car :", debug)
    tvshow1 = gettvshow("enter a tvshow  :", debug)
    videogame1 = getvideogame("enter a videogame :", debug)
    food2 = getfood("enter a food :", debug)
    time1 = gettime("enter a time :", debug)
    out=""
    out+="one day me and my friend " +friendname1
    out+=" were eatting " +food1
    out+=" at the new " +restaurant1
    out+=" in town " 
    out+=" after that we got into a " +car1
    out+=" and drove home and watched the new episode of " +tvshow1
    out+=" he went home and i played " +videogame1
    out+=" then i had " +food2+" for dinner "
    out+=" then i went to bed at " +time1
    return out

