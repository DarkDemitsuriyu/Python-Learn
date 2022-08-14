n = int(input())
f = 0
for i in range(1, n + 1):
    count = 1
    flag = True
    for j in range(i + f):
        print(count, end="")
        if count == i:
            flag = False
        if flag:
            count += 1
        else:
            count -= 1
    f = i
    print()