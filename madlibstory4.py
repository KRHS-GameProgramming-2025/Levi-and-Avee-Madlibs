from madlibgetword import *

def story4(debug=False):
    if debug: print("welcome to story 4")
    
    
    
    
    friendname1 = getWord("enter a name :", debug)
    food1 = getfood("enter a food :", debug)
    restaurant1 = getrestaurant("enter a reataurant :", debug)
    
    out=""
    out+="one day me and my friend " +friendname1
    out+=" were eatting " +food1
    out+=" at the new " +restaurant1
    out+=" in town " 
    return out

