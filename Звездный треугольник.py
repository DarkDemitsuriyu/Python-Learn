# объявление функции
def number_to_words(num):
    s = ""
    a = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    b = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    if num < 20:
        s += a[num]
    else:
        x = num % 10
        y = (num // 10) % 10
        s = b[y - 2]
        if x > 0:
            s += " " + a[x]
    return s       

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))