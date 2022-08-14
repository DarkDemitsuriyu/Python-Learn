import random
print("Добро пожаловать в числовую угадайку")
def lets_go():
    n = 100
    count = 0
    while True:
        s = input("Введите максимальное допустимое число или просто нажмите Enter. По умолчанию задано число - 100\n")
        if s.isdigit():
            n = int(s)
            break
        elif len(s) == 0:
            break
        else:
            print("Вы ввели некорректное значение. Попробуйте еще раз.")
    x = random.randint(1, 100)
    print("Я загадал число. Попробуйте угадать")
    while True:
        y = input()
        if y.isdigit():
            y = int(y)
        else:
            print("Вы ввели некорректное значение. Попробуйте еще раз.")
            continue
        if y == x:
            print("Вы угадали, поздравляем! Количество попыток -", count)
            break
        elif y < x:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        else:
            print("Ваше число больше загаданного, попробуйте еще разок")
        count += 1
    S = input("Хотите сыграть еще раз? Введите да или нет\n")
    if S.lower() == "да":
        lets_go()
    else:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")

lets_go()