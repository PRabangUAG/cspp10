print ("How it works")
print("      ")
print("Enter 0 to end the program")
print("any postive interger to add to the list")
print("any negative number to subtract one of the numbers you added")
userinput = 1
userlist = []
while userinput is not 0:
    userinput = int(input("What number would you like to add to the list? "))
    if userinput > 0:
        userlist.append(userinput)
    print (userlist)
    if userinput < 0:
        userlist.remove(userinput * -1)
        print (userlist)