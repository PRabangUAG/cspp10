noun = input("What noun would you like to pluralize? ")
numnoun = input("How many of {}? ".format(noun))
    

if numnoun == "1":
    print("1 " + noun)
else:
    if noun[-2:] == "fe":
        print(numnoun + " " + noun[:-2] + "ves") 
        
    elif noun[-2:] == "ay" or noun[-2:] == "oy" or noun[-2:] == "ey" or noun[-2:] == "uy":
        print(numnoun + " " + noun + "s")
        
    elif noun[-2:] == "sh" or noun[-2:] ==  "ch":
        print(numnoun + " " + noun + "es")        

    elif noun[-1] == "y":
        print(numnoun + " " + noun[:-1] + "ies")
 
    elif noun[-2:] == "us":
        print(numnoun + " " + noun[:-2] + "i")
    else: 
        print(numnoun + " " + noun + "s")
