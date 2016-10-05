div = "Division"
add = "Additon"
sub = "Subrtraction"
multi = "Multipication"



NumX = int(input("Whats your first number? "))
NumY = int(input("Whats your second Number? "))
op = str(input("What order of opertations? Additon, Subrtraction, Multipication, Division? "))

divv = NumX / NumY
added = NumX+NumY
subed = NumX-NumY
multiply = NumX*NumY


if op == 'div':
    print ('divv')