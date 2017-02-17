from pprint import pprint
def dictionary():
    d = {}
    while True:
        u = input("What would you like to do? add? delete? modify or exit? ")
        if u == "add":
            x = input("What would you like the key to be called? ")
            if x in (d):
                print("this is already a key sorry ")
            v = input("What would you like the value of the key to be? ")
            d [x] = v
            pprint (d)
        if u == "delete":
            k = input("What key would you like to delete? ")
            if k in (d):                
                del d[k]
            else:
                print ("sorry this isnt a key")
            pprint (d)
        if u == "modify":
            x = input("Which key would you like to modify? ")
            if x in (d):
                t =  input("What would you like to change the vaulue to? ")
                d [x] = t
                
            
        if u == "exit":
            print("EXIT")
            break
    
dictionary()

    
    
#while loop
#ask the user what they would like to do.
#create task for add or delete and exit
#if statements for all task
#put if statements inside of while loop
#ask user each time what they would like to do.