digit = input('введите число: ')
if digit.isdigit() != True:
    print('это строка')
    exit()
else:
    print('это число')
    if int(digit) % 2 == False:
        print('четное')
    elif int(digit) % 2 == True:
        print('НЕ ЧЕТНОЕ')
