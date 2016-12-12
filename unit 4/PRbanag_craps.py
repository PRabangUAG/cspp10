import random


def get_bet(bank_account):
    bet=int(input("How much would you like to bet?"))
    if bet<0:
        return("your number must be a postive integer and greater than 0")
    if bet>100:
        return ("Your bank account balance isnt that higher")
        bank_account=bank_account
        return bank_account
    return bet

def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("rolled 2 dice {} {}".format(dice1,dice2))
    return rolldice()
    
def first_roll(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        return("you win")
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return ("you lose")
    else:
        return dice_sum
    
def second_roll 