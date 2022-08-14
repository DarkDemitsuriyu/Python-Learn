n = int(input())
x = n // 2
for i in range(n):
    if i <= x:
        for j in range(i + 1):
            print("*", end="")
    else:
        for z in range(x, 0, -1):
            print("*", end="")
        x -= 1
    print()
