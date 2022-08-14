a1, b1, a2, b2 = 1, 6, 7, 2
x = a2 - a1
y = b2 - b1
if (x % 2 != 0 and y % 2 != 0) or ((a2 == a1 or x % 2 == 0) and (b2 == b1 or y % 2 == 0)):
    print("YES")
else:
    print("NO")