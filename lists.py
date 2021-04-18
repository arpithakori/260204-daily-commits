# basic list
words = ["hi", "hello", "how"]
print(words[0])
print(words[1])

# indexing string
s = "Hello World"
print(s[6])

# list operations
num = [1, 2, 3]
print(num + [4, 5, 6])
print(num * 3)

# in operator
print("hi" in words)
print("why" in words)

# not in operator
print(7 not in num)

# for loop
for w in words:
    print(w + "!")

# for loop for strings
st = "testing for loops"
count = 0
for x in st:
    if x == 't':
        count += 1
print(count)
