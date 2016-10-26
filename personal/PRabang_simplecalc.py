div = "/"
add = "+"
sub = "-"
multi = "*"



NumX = float(input("Whats your first number? "))
NumY = float(input("Whats your second Number? "))
op = str(input("What order of opertations? +, -, *, /? "))

divv = NumX / NumY
added = NumX + NumY
subed = NumX - NumY
multiply = NumX * NumY


if op == div:
    print (divv)
    
elif op == add:
    print (added)
    
elif op == sub:
    print (subed)
    
elif op == multi:
    print (multiply)