# объявление функции
def is_palindrome(text):
    a1 = [w.lower() for w in text if w.isalpha()]
    a2 = a1[::-1]
    if a1 == a2:
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))