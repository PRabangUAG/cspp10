import random

def get_bet(bank_account):
    while True:
        print("You have ${} in your bank account.".format(bank_account))
        bet=int(input("How much would you like to bet?: $"))
        if bet < 0:
            print("Your bet must be a positive integer higher than $0")
        elif bet> bank_account:
            print("You only have ${} to bet, you can't bet anymore!".format(bank_account))
        else:
            return bet

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} + {}".format(dice1,dice2))
    print("Dice roll total: {}".format(dice1+dice2))
    return dice_sum
    
    


def first_roll_result(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        return "You won!"
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return "You lose!"
        
    else:
        return dice_sum

        
def second_roll_result(dice_sum,point_roll):
    if dice_sum == 7:
        return("You lose!")
        
    elif dice_sum == point_roll:
        return("You won!")
        
    else:
        while(dice_sum != 7 and dice_sum != point_roll):
            dice_sum=roll2dice()
            if dice_sum == 7:
                return "You lose!"
            elif dice_sum == point_roll:
                return "You won!"
        
        


        

def craps():
    bank_account=100
    while  bank_account > 0:
        bet = get_bet(bank_account)
        dice = roll2dice()
        first_result = first_roll_result(dice)
        if first_result == "You won!":
            print("You won!")
            bank_account = bank_account+bet
        elif first_result == "You lose!":
            print ("You lose!")
            bank_account = bank_account-bet
        else:
            print("point roll")
            dice = roll2dice()
            point_roll_result = second_roll_result(dice,first_result)
            if point_roll_result == "You lose!":
                print("You lose!")
                bank_account= bank_account-bet
            if point_roll_result == "You won!":
                print("You won!")
                bank_account= bank_account+bet
            
            
        print("____________________________________")
    
         
        
        
craps()