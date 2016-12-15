import random

#This is youur bet, it tells you if you have enough or not, asking how much you would like to bet
def get_bet(bank_account):
    while True:
        bet=int(input("How much would you like to bet?"))
        if bet<0:
            print("your number must be a postive integer and greater than 0")
        elif bet>100:
            print ("Your bank account balance isnt that higher")
        else:
            return bet

def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("rolled 2 dice {} {}".format(dice1,dice2))
    print("Total:{}".format(dice1 + dice2))
    return dice_sum
    
def first_roll(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        print("you win")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print ("you lose")
    else:
        return dice_sum
    
def second_roll(dice_sum,point_roll):
    if dice_sum ==7 or dice_sum ==11:
        print("you win")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print ("you lose")
    else:
        print("try again")
    return second_roll
    
def point_roll(roll, point_roll):
    while (roll != 7 and roll != point_roll):
        print(get_bet(bank_account))
        
 
def craps():
    bank_account = 100
    get_bet(bank_account)
    diceroll = rolldice()
    first_roll = first_roll(dice_sum)
    if first_roll == "you win":
        print("you win")
    elif first_roll == "you lose":
        print("you lose")
    else:
        print("point roll")
        dice = rolldice()
        point_roll_score = second_roll(dice_sum,first_())
        return(craps())
        
craps()