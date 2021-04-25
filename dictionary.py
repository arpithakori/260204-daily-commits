# dictionary value access by keys
ages = {"Dave":25, "Mary":65,}
print(ages["Dave"])
print(ages["Mary"])

# dictionary type 2
prim = {"red":[255,0,0],
        "blue":[0,0,255],
        "green":[0,255,0],}
print(prim["red"])
# giving a key which is not present in the dictionary gives keyerror
print(prim["yellow"])

#running a bad dictionary
bad_dict = {[1,2,3]:"one two three",}

