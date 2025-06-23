a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j] and a[i] not in c:
            c += [a[i]]
        else:
            continue
for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j] and b[i] not in c:
            c += [b[i]]
        else:
            continue
c.sort()
print(c)