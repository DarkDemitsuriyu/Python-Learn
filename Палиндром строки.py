# объявление функции
def draw_triangle():
    x = 8
    for i in range(1, 15 + 1, 2):
        print((" " * int((15 - i)/2)) + ("*" * i))
    

# основная программа
draw_triangle()  # вызов функции