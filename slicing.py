# slicing version 1
sq = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sq[2:6])
print(sq[3:8])
print(sq[0:1])

# slicing version 2
print(sq[:7])
print(sq[7:])

# slicing version 3
print(sq[::2])
print(sq[2:8:3])

# slicing version 4
print(sq[1:-1])

# test
lists = [1, 1, 2, 3, 5, 8, 3]
print(lists[lists[4]])

print("************************")
# reverse a list
print(lists[::-1])

