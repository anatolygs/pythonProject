import random
# a = 7
a = random.randrange(1, 10)
for chislo_popitok in range(1, 6):
    user_digit = int(input('введите число : '))
    if user_digit == a:
        print(f'угадал, это {a}')
        break
    elif user_digit < a:
        print(f'не угадал число больше, осталось {5-chislo_popitok} попыток')
    elif user_digit > a:
        print(f'не угадал число меньше, осталось {5-chislo_popitok} попыток')

