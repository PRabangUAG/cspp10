def replace_all(original,to_replace,replace_with):
    for index in range(len(original)):
        if original[index] == to_replace:
            original[index] = replace_with
original = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,]
to_replace = 1
replace_with = "a"
replace_all(original,to_replace,replace_with)
print(original)