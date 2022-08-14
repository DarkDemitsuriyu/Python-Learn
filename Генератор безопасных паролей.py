import random
def get_data_int(text):
    x = ""
    while True:
        x = input(text)
        if x.isdigit():
            break
        else:
            print("Вы ввели некорректное значение. Попробуйте еще раз")        
    return int(x)   
def get_data_bool(text):
    while True:
        x = input(text + " Введите да или нет:\n")
        if x.lower() == "да":
            return True
        elif x.lower() == "нет":
            return False
        else:
            print("Вы ввели некорректные данные. Попробуйте снова")
def cleaning(chars):
    a = list(chars)
    for c in "il1Lo0O":
        if a.count(c) > 0:
            a.remove(c)
    return "".join(a)    
def pass_gen(length, chars):
    pwd = ""
    for _ in range(length):
        pwd += random.choice(chars)
    return pwd

print("Добро пожаловать в генератор паролей.")
chars = ""
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
n = get_data_int("Введите количество паролей, которое необходимо сгенерировать:\n")
length = get_data_int("Введите длинну генерируемых паролей:\n")
is_digit = get_data_bool("Включать ли цифры?")
is_lower = get_data_bool("Включать ли прописные буквы?")
is_upper = get_data_bool("Включать ли строчные буквы?")
is_punct = get_data_bool('Включать ли символы "!#$%&*+-=?@^_"?')
is_not = get_data_bool('Исключать ли неоднозначные символы "il1Lo0O"?')
if is_digit:
    chars += digits
if is_lower:
    chars += lowercase_letters
if is_upper:
    chars += uppercase_letters
if is_punct:
    chars += punctuation
if is_not:
    chars = cleaning(chars)
while True:
    print("Ваш список паролей:")
    for _ in range(n):
        print(pass_gen(length, chars))
    if not get_data_bool("Сгенерировать еще паролей с теми же условиями?"):
        break