import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print (dice_sum)
    return dice_sum
    # generate another random number from 1 to 6
   
    # get the sum of the two rolls
   
    # print the sum
   
    # return the sum
 
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    bank_account = 100
    bet = input(int("How much would you like to bet?"))
    print ("you bet {}".format(bet))
    while bet <= bank_account:
        print ("you bet {}".format(bet))
    else:
        print("you dont have enough money.")
    return bet
    # ask the player how much they want to bet
   
    # if player's bet is more than they have
    #   available in bank, then get new bet
   
    # if player's bet is valid, then return
    #   the bet

# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    if dice_sum > 7:
        return "over7"
    if dice_sum < 7:
        return "under7"
    
    if dice_sum == 7:
        return "equal7"
   
    return get_range(dice_sum)
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    print("If you win for over 7 you get a pay out of 1:1")
    print("If you win for under 7 you get a pay out of 1:1")
    print("If you win for equal to 7 you get a pay out rate of 4:1")
    pchoice =input("please choose over7,under7,equal7")
    return pchoice
    
 
# function for the main game
def roll2dice():
def get_bet(bank):
def get_range(dice_sum):
def get_range(dice_sum):