t = (1, 2, 4, 5, 3, 6, 5, 3, 6, 5, 3, 4, 5, 2, 4)
l = []
for i in t:
    if t.count(i) > 1 and i not in l:
        l.append(i)
for i in l:
    print(i)
