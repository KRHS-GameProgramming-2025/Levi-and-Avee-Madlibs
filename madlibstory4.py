from madlibgetword import *

def story4(debug=False):
    if debug: print("welcome to story 4 :3")
    
    
    
    
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
    out+=" were eating " +food1
    out+=" at the new " +restaurant1
    out+=" in town " 
    out+=" after that we got into a " +car1
    out+=" we then drove home and watched the new episode of " +tvshow1
    out+=" he went home and i played " +videogame1
    out+=" then i had " +food2+" for dinner "
    out+=" after that i went to bed at " +time1
    return out

#wip  Me and my friend = name FN1 and my other friend FN2, went to the ballpark and got some hotdogs and FD1 along with SE1 to season it!
#it was awfully delicious! im glad i know what kind of food it was! itd be a shame if i didnt.. oh well! me and FN1 + FN2 had a lovely time!
#notes from Dev1, FN1 = friendname1 and FN2 is friend name two, and FD1 is food1 and SE1 is seasoning1, and ive included a hint for the easteregg, and you can use the comments
#just put yourself as Dev2
