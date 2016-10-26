password = "1234"
user_guess = input ("Enter the password ")

while True:
    if user_guess == password:
        break
    else:
        user_guess = input ("Enter the password ")

print ("Access Granted")