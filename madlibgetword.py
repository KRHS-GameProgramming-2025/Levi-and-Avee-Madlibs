def getMenuOption(debug = False):
    if debug: print("getMenuOption function")
    
    goodinput = False 
    
    while not goodinput:
        option = input ("select an optwion pwease :3: ")
        option = option.lower()
        
        if (option == "q" or
        option == "quit" or
        option == "x" or
        option == "exit"):
            option = "q"
            goodinput = True
            
             
        if (option == "1" or
        option == "one" or
        option == "story1" or
        option == "loadS1" or
            option == "1"):
            goodinput = True
            
        if (option == "2" or
        option == "two" or
        option == "story2" or
        option == "loadS2" or
            option == "2"):
            goodinput = True
            
        if (option == "3" or
        option == "three" or
        option == "story3" or
        option == "loadS3" or
        option == "3"):
            goodinput = True
            
        if (option == "4" or
        option == "four" or
        option == "story4" or
        option == "loadS4" or
        option == "4"):
            goodinput = True
            
        else:
            print("Pwease make a valid chowice! or get out!")
            
    return option 


def getWordWithscience(prompt, debug = False):
    if debug: print("getMenuOption function")
    
    goodinput = False 
    
    science = ["earth science",
        "medical",
        "physics", 
        "nuclear",
        "astronomy",
        "astrophysics", 
        "geology",
        "meteorlogy",
        "aagriculture",]
        
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug):
           goodinput = False
           print("gwet owrginal dangit!!")
        elif word.lower() in science: 
            goodinput = False
            print("gwet owrginal dangit!!")
    return word 


def getWordWithElement(prompt, debug = False):
    if debug: print("getMenuOption function")
    
    goodinput = False 
    
    elements = ["uranium",
        "cobalt-60",
        "antimatter", 
        "el nasir",
        "tesla cybertruck",
        "plutonium", 
        "cadnium",
        "mercury",
        "arsenic",]
        
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug):
           goodinput = False
           print("gwet outta my gwame or lword help me i will find you-")
        elif word.lower() in elements: 
            goodinput = False
            print("whyYY???? WUoULD YWOU CHOOSE THAT??")

    return word 

def getWord(prompt, debug = False):
    if debug: print("getMenuOption function")
    
    goodinput = False 
        
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug):
           goodinput = False
           print("gwet outta my gwame or lword help me i will find you-")

    return word 
    
def getfood(prompt, debug=False):
    if debug: print("get foodFunction")
    goodinput = False
    
    foods=["pizza",
            "icecream",
            "watermelon",
            "cookies",
            "hotdogs",
            "cake",
            "french fries",
            "jello",
            "chips",
            "eggs",
            "pie",
            "donuts",
            "steak",
            "mac n cheese",
            "pasta",
            "tacos",
            
            ]
            
    while not goodinput:
        word = input(prompt)
        if isSwear (word, debug):
            goodinput = False
            print("don't use language like that")
        elif word.lower() in foods:
            goodinput = True
        else:
            print ("ive never heard of that")
    return word
    
def getrestaurant(prompt, debug=False):
    if debug: print("get restaurantFunction")
    goodinput = False
    
    restaurant=["pizza hut",
                "burger king",
                "wendys",
                "kfc",
                "chickfla",
                "sonic",
                "in and out",
                "subway",
                "five guys",
                "taco bell",
                "dairy queen",
                "dunkin",
                "papa johns",
                "applebees",
                ]
    while not goodinput:
        word = input(prompt)
        if isSwear (word, debug):
            goodinput = False
            print("lword hwelp me i will find you")
        elif word.lower() in restaurant:
            goodinput = True
        else:
            print ("ive nevah hweard of thwat before!")
    return word
    
    
def isSwear(word, debug = False):
        if debug: print("isSwear function")
        if word.lower() in swearlist:
            return True
        else:
            return False 

swearlist = ["shit", 
             "fuck", 
             "bitch", 
             "son of a bitch", 
             "sonofvabitch", 
             "cunt",
             "vile imbicile", 
             "nazi", 
             "fucker", 
             "fuckinghell", 
             "midget", 
             "Machine, i will cut you down, break you apart, splay the gore of your profane form across the STARS! I will grind you down until the very SPARKS CRY FOR MERCY! My hands shall RELISH ENDING YOU… HERE AND NOW!", 
             "INSIGNIFICANT FUCK!", 
             "me omw to beat your ass to death", 
             "500 cigarretes", 
             "Britan", 
             "long live the queen", 
             "long live the old gods",
             ] 

#note these do not represent anything i would say alright? this is for the task at hand only 

#dev2. STOP REMOVING THE CHARACTER!!!
