oper = input("what is your equation without any spaces ")
Num = int(oper[0]) #first number
op = str(oper[1]) #operation
Numx = int(oper[2]) #second number
U = 0


if op == '+': 
    U = Num + Numx
    
elif op == '*':
    U = Num * Numx
    
elif op == '/':
    U = Num / Numx
     
elif op == '-':
    U = Num - Numx

elif op == '%':
    U = Num % Numx
    
print ("Your answer is "+ str(U))
    