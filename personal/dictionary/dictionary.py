from pprint import pprint



d = {
    "name":"phoenix",
    "birthmonth":"january",
    "grade": 10
}
del d ['name']
pprint (d)
if "name" in d:
    print("is in d")
else:
    print ("not in d")