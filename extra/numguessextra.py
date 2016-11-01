import random
rand = random.randint(0,1000001)
uguess = int(input("Pick a number between 1-1000000 "))
guesstaken = 0
while(uguess >= 1 or uguess <= 100):
    if uguess > rand:
        print ("too high, try again ")
        uguess = int(input("Pick a number between 1-100 "))
        guesstaken = guesstaken + 1 
        
    elif uguess < rand:
        print ("too low, try again ")
        uguess = int(input("Pick a number between 1-100 "))
        guesstaken = guesstaken + 1 
    elif uguess == rand:
        guesstaken = guesstaken + 1 
        print ("You're correct its {}".format (rand))
        if guesstaken > 1:
            print ("it took you {} tries.".format(guesstaken))
            break
        elif guesstaken == 1:
            print ("it took you {} try.".format(guesstaken))
            break
        break