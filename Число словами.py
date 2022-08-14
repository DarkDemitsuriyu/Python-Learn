# объявление функции
def is_pangram(text):
    s = "abcdefghijklmnopqrstuvwxyz"
    for c in s:
        if c not in text.lower():
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))