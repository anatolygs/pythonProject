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

s = 'Hello world!'
for i in s:
    if i == " ":
        print(s.upper())
    else:
        print(s.lower())
