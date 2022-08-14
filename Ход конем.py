a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
x = a2 - a1
y = b2 - b1
if -2 <= x <= 2 and -2 <= y <= 2 and a1 != a2 and b1 != b2:
    if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
