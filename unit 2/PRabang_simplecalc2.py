equation = input("what is your equation without any spaces ")
Num = [0]
op = [1]
Numx = [2]
U = 0


if op == '+':
    U = Num + Numx
    
elif op == '*':
    U = Num * Numx
    
elif op == '/':
    U = Num / Numx
     
elif op == '-':
    U = Num - Numx
    
print ("Your answer is "+ str(U))
    