userinput = 1
userlist = []
while userinput is not 0:
    userinput = int(input("What number would you like to add to the list? "))
    if userinput > 0:
        userlist.append(userinput)
    print (userlist)
    if userinput < 0:
        userlist.remove(userinput* -1)
        print (userlist)