nn = int(input("Whats your last number?"))

for n in range (1,nn):
    if n % 3==0 and n % 5 ==0:
        fb = n
        fb = "Fizzbuzz"
        print (fb)
    elif n % 3 == 0:
        f = n
        f = "Fizz"
        print (f)
    elif n % 5 == 0:
        b = n
        b = "Buzz"
        print (b)
    else:
        print (n)