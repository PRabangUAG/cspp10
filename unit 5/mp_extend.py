original = [1,2,3]
extension = [6,7,8]

def extend(original,extension):
    for element in extension:
        original.append(element)
        
extend (original,extension)
print ("original {}".format(original))
