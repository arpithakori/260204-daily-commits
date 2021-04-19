# length of the list
nums = [1, 3, 5, 2, 4]
print(len(nums))

# append list
nums.append(6)
print(nums)

# insert at one particular index
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

# to find the index of a list
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))

# other built in functions
print(max(nums))
print(min(nums))
print(letters.count('p'))
letters.remove('s')
print(letters)
print(nums.reverse())
