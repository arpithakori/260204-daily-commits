def find_len(lis):
    length = len(lis)
    lis.sort()
    print("Second Smallest:", lis[1])


lis = [12, 45, 2, 41, 31, 10, 8, 6, 4]
smallest = find_len(lis)


