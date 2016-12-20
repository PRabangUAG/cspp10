import random

#This is youur bet, it tells you if you have enough or not, asking how much you would like to bet
def get_bet(bank_account):
    while True:
        bet=int(input("How much would you like to bet? $"))
        if bet<0:
            print("your number must be a postive integer and greater than 0")
        elif bet>100:
            print ("Your bank account balance isnt that high")
        else:
            return bet

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("rolled 2 dice {} {}".format(dice1,dice2))
    print("Total:{}".format(dice1 + dice2))
    return dice_sum
    
def first_dice_result(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        print("you win")
        return(craps())
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print ("you lose")
        return(craps())
    else:
        return dice_sum
    
def second_roll_result(dice_sum,point_roll):
    if dice_sum == point_roll:
        print("you win")
    elif dice_sum == 7:
        print("you lose")
    else:
        while (dice_sum != 7 and dice_sum != point_roll):
            dice_sum=roll2dice()
            return (second_roll_result)
    


        
 
def craps():
    bank_account = 100
    get_bet(bank_account)
    dice = roll2dice()
    first_result = first_dice_result(dice)
    if first_result  == "you win":
        print("you win")
    elif first_result  == "you lose":
        print("you lose")
    else:
        print("point roll")
        diceroll = roll2dice()
        point_roll_result = second_roll_result(dice,first_result)
    return(craps())
        
craps()