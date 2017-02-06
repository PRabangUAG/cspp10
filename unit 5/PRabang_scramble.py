import random

word = "orange"
def scramble_word(word):
 if len(word) > 3:
    alist = list(word)
    firstletter = word[1]
    lastletter = word [-1]
    xlist = word[1:-1]
    random.shuffle(xlist)
    xlist.insert(0,firstletter)
    xlist.append(lastletter)
    final =''.join(xlist)
    print(final)
    
    
scramble_word(word)
    
#getting users input
#make a list
 
#making users input = to a list

#scrambling the list that you made with the users input

#printing users input
