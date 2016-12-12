import random

def get_p1_move():
    pmove = input("Choose rock, paper or scissors?(all lower case please) ")
    return pmove.lower()


def get_comp_move():
    cpumove = random.randint(1,3)
    if cpumove == 1:
        return 'rock'
    elif cpumove == 2:
        return 'paper'
    elif cpumove == 3:
        return 'scissors'
    
    return cpumove
    
def get_rounds():
    rounds = int(input("How many rounds?: "))
    return rounds


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
        
def print_score(pscore, cscore, ties):
    print("Player: {} ".format(pscore))
    print("      ")
    print("Computer: {} ".format(cscore))
    print("      ")
    print("Ties {} ".format(ties))
    print("      ")
 


def rps(): 
    pscore = 0
    cscore = 0
    ties = 0
    
    rounds = get_rounds()
    for rounds in range(int(rounds)):
        p1move = get_p1_move()
        comp_move = get_comp_move()
        print("comp chose {} ".format(comp_move))
        print("      ")
        winner = get_round_winner(p1move,comp_move)
        if winner == "player wins!" :
            print("Player Won")
            print ("      ")
            pscore= pscore+1
        elif winner == "comp wins!":
            print("Comp won")
            print ("      ")
            cscore= cscore+1
        else:
            print ("its a tie")
            print ("      ")
            ties= ties+1
        print_score(pscore,cscore,ties)
    print ("      ")
    if pscore < cscore:
        print("comp wins")
    elif cscore < pscore:
        print("player wins")
    else:
        print("Its a tie!")


def test():
    return 1

rps()