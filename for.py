# # a = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
# #      'y', 'z']
#
# for i in range(10,1,-1):
#     print(i, end='')
# a=input('enter a: ')
# b=input('enter b: ')
#
# for i in range(int(a),int(b)):
#     print(i)

# a = input('enter a: ')
# b = input('enter b: ')
# if int(a) <= int(b):
#     for i in range(int(a), int(b) + 1):
#         print(i)
# else:
#     for i in range(int(a), int(b) - 1, -1):
#         print(i)
a=int(19)
b=int(1)
print(a - (a + 1)%2)
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')
