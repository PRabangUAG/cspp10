import random
#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    pmove = input("Choose Rock, Paper or Scissors? ")
    return pmove.lower()

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    cpumove = random.randint(1,3)
    if cpumove == 1:
        return 'rock'
    elif cpumove == 2:
        return 'paper'
    elif cpumove == 3:
        return 'scissors'
    
    return cpumove
    
#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    rounds = input(int("How many rounds?: "))
    return rounds


#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move, cmove):
    if p1move == 'rock' and cmove == 'paper':
        return("comp wins!")
    elif p1move == 'scissors' and cmove == 'rock':
        return("comp wins!")
    elif p1move == 'paper' and cmove == 'scissors':
        return ("comp wins!")
    elif p1move == 'paper' and cmove == 'rock':
        return("player wins!")
    elif p1move == 'rock' and cmove == 'scissors':
        return("player wins!")
    elif p1move == 'scissors' and cmove == 'paper':
        return ("player wins!")
    elif p1move == 'paper' and cmove == 'paper':
        return("tie!")
    elif p1move == 'rock' and cmove == 'rock':
        return("tie!")
    elif p1move == 'scissors' and cmove == 'scissors':
        return ("tie!")
    else:
        print("Error")



#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    return 1

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    return 1

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none
def test():
    return 1
print(get_rounds())
print(get_p1_move())
print(get_comp_move())
rps()