def merge(di, dic):
    res = di | dic
    return res


# Driver code
di = {'x': 10, 'y': 8}
dic = {'a': 6, 'b': 4}
dict3 = merge(di, dic)
print(dict3)
