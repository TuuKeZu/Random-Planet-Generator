import random

class generateRandomName:
    def __init__(self):
        result = ""

    def generateName(self):
        vowels = ['o', 'i', 'y', 'e', 'a','u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm' ,'n' ,'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        construct = "";

        seed = [random.randrange(0, 2), random.randrange(0, 2), random.randrange(0, 5)]

        if(seed[0] == 0):
            construct += "VC"
        elif(seed[0] == 1):
            construct += "CV"

        if(construct[1] == "C"):
            if(seed[1] == 0):
                construct += "C"

        construct += "VC"
        name = ""

        if(seed[2] == 0):
            construct += "E1" #n
        if(seed[2] == 1):
            construct += "E2" #s
        if(seed[2] == 2):
            construct += "E3" #thus
        if(seed[2] == 3):
            construct += "E4" #r
        if(seed[2] == 4):
            construct += "E5"
        if(seed[2] == 5):
            construct += "E6"
        
        # decompile
        for char in construct:
            if(char == "V"):
                i = random.randrange(0, len(vowels))
                name += vowels[i]
            elif(char == "C"):
                i = random.randrange(0, len(consonants))
                name += consonants[i]

        if(construct[-1] == "1"):
            i = random.randrange(0, len(vowels))
            name += f"{vowels[i]}n"

        elif(construct[-1] == "2"):
            i = random.randrange(0, len(vowels))
            name += f"{vowels[i]}s"

        elif(construct[-1] == "3"):
            i = random.randrange(0, len(vowels))
            e = random.randrange(0, len(vowels))
            name += f"{vowels[i]}th{vowels[e]}s"

        elif(construct[-1] == "4"):
            i = random.randrange(0, len(vowels))
            name += f"{vowels[i]}r"
            
        elif(construct[-1] == "5"):
            i = random.randrange(0, len(vowels))
            name += f"{vowels[i]}"

        elif(construct[-1] == "5"):
            i = random.randrange(0, len(vowels))
            name += f"{vowels[i]}"
        return name


    