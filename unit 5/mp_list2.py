userinput = 1
userlist = []
print ("Please choose print, sum, clear,length,exit")
while userinput is not 0:
    userinput = input("What number would you like to add to the list? ")

    if userinput == "print":
        print (userlist)
    elif userinput == "clear":
        userlist = []
        print (userlist)
    elif userinput == "sum":
        print (sum(userlist))
    elif userinput == "length":
        print(len(userlist))
    elif userinput == "exit":
        print ("gameover")
        break
    else:
        userinput = int(userinput)
        userlist.append(userinput)
        