bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while(bank_account == 10000): #student completes while loop
    if choice == "1": #user chooses 'withdraw'
        amount = input("how much would you like to withdraw? ")
        bank_account = bank_account - amount
    elif choice == "2": #user chooses deposit
        amount = input("How much to deposit: ")
        bank_account = bank_account + amount
    elif choice == "3": #user chooses 'exit'
        break
        #student does this part too
    print("1. Withdraw \n2. Deposit \n3. Exit")
    choice = input("Pick from above [1|2|3]:")