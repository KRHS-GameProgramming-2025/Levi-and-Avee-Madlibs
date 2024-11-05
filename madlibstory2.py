from madlibgetword import * 

def story2(debug = False):
    if debug: print("ヾ(0w0`)o welcome!! :3 Story 2")
    
    element1 = getWord("choose the name ;3", debug)
    rocket2 = getWord("choose the name ;3", debug)
    galaxy = getWord("choose the name ;3", debug)
    
    
    
    out = ""
    out +=  "BREAKING NEWS! SCIENTIST DISCOVERS NEW ELEMENT CALLED " + element1
    out += " THIS REVOLUTIONARY ELEMENT IS CAPABLE OF HELPING US SOLVE THE SECRETS TO FASTER THAN LIGHT SPEEEPDS! AND WILL BE USED IN THE NEW EXPERIMENTAL" + rocket2
    out += " ROCKET! TO INVESTIGATE COSMIC MYSTERIES SUCH AS WHATS BEYOND IN THE MORE HIDDEN SECTORS OF OUR GALAXY!!"+ galaxy
    out += " SUCH AS THE STAR CLUSTER OF THE " + rocket2
    out += " WHAT WILL WE FIND?"
    
    
    return out
