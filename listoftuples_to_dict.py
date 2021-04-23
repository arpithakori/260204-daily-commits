lists = [("x", 1), ("x", 2), ("x", 3), ("y", 4), ("y", 5), ("z", 6)]
dic = {}
for a, b in lists:
    dic.setdefault(a, []).append(b)
print(dic)
