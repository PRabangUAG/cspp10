from pprint import pprint

x = input("What would you like the key to be called?")
v = input("what would you like the value of the key to be?")
d [x] = v

d = {
    "name":"phoenix",
    "birthmonth":"january",
    "grade": 10
}
d ['x'] = "cutie"

if "name" in d:
    print("is in d")
else:
    print ("not in d")
    