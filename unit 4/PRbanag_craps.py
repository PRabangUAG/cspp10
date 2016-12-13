import random


def get_bet(bank_account):
    while True:
        bet=int(input("How much would you like to bet?"))
        if bet<0:
            return("your number must be a postive integer and greater than 0")
        elif bet>100:
            return ("Your bank account balance isnt that higher")
        else:
            return bet

def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("rolled 2 dice {} {}".format(dice1,dice2))
    print("Total:{}".format(dice1 + dice2))
    return rolldice()
    
def first_roll(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        return("you win")
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return ("you lose")
    else:
        return dice_sum
    
def second_roll(dice_sum,point_roll):
    if dice_sum ==7 or dice_sum ==11:
        return("you win")
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return ("you lose")



def craps():
    bank_account = 100
    get_bet(bank_account)
    first_rol = first_roll(dice_sum)
    if first_rol == "you win":
        print("you win")
    elif first_rol == "you lose":
        print("you lose")
    else:
        print("point roll")
        
craps()