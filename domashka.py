# a = [1, 2, 3]
# b = []
# for i in range(len(a)):
#     b.append(a[i]*2)
# print(b)

# a = [1, 2, 3]
# b = []
# for i in range(len(a)):
#     print(a[i]**2)
#     b.append(a[i]**2)
# print(sum(b))

# time1 = 3
# time2 = 6.7
# time3 = 11.8
#
# print(int(time1*0.5))
# print(int(time2*0.5))
# print(int(time3*0.5))

# s = 'Hello world!'
# for i in s:
#     if i == " ":
#         print(s.upper())
#     else:
#         print(s.lower())

# n = int(input())
#
# for x in range(1, n):
#     if x % 3 == 0 and x % 5 == 0:
#         print("SoloLearn")
#     elif x % 2 == 0:
#         continue
#     elif x % 3 == 0:
#         print(f"Solo{x}")
#     elif x % 5 == 0:
#         print(f"Learn{x}")
#     else:
#         print(x)

# def func(x):
#     num = 0
#     for i in range(x):
#         num += i
#     return num
#
# print(func(6))

# def get_names(names):
#     new_names = []
#     for i in names:
#         if len(i) == 4:
#             new_names.append(i)
#     return new_names
#
#
#
# names = ['Rayan', 'Sema', 'Kieran', 'Mark', 'Anna', 'David', 'Paul', 'Abba']

# print(get_names(names))

# def odd_ball(arr):
#     x = arr.index('odd')
#     if x in arr:
#         return True
#     else:
#         return False
#
#
# massive = ['even', 4, 'even', 'odd', 5, 'even', 7,'even', 3, 10, 'even', 8]
#
# print(odd_ball(massive))

# def find_sum(n):
#     x = 0
#     for i in range(n + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             x += i
#     return x
#
#
# def find_sum2(n):
#     return sum(i for i in range(n+1) if i % 3 == 0 or i % 5 == 0)
#
# print(find_sum(500000000))

import os

def catalog(arg):
    # dir1 = arg
    num = 0
    for i in os.walk(arg):
        num += 1
        print(num, i[0], file=file)
        for k in i[1]:
            print('\t', k, file=file)
            for l in i[2]:
                print('\t'*2, l, file=file)

file = open('out.txt', 'a+')

catalog('/Users/anatoly/Desktop/маленькая черная рабочая')
# print(catalog('/Users/anatoly/'), file=file)
file.close()

