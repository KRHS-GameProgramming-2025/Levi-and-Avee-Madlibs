from madlibscreen import *
from madlibgetword import *
from madlibstory1 import *
from madlibstory2 import *
from madlibstory3 import * 
#dont forget to put in the new stories here okay?
def madlibs(debug = False):
    if debug: print ("DEBUG ACTIVE, WELCOME AUTHORIZED USER")
    
    print(titlescreen(debug)) 
    try:
        input("press enter to continue")
    except:
        pass 

    done = False
    while not done:
        print(menuscreen(debug))
        choice = getMenuOption(debug)
        
        if choice == "q":
            exit();
        if choice == "1":
            print("story fouar selected!1!")
            print(story1(debug))
            print("\n")
            input("press enter to continue")
        if choice == "2":
            print("story three selected!1!")
            print(story2(debug))
            input("press enter to continue")
        if choice == "3":
            print("story two selected!1!")
            print(story3(debug))
            input("press enter to continue")
    
    
    
    
    
madlibs (False)

