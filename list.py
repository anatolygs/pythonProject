l = [1, 2, 3, ['test', .5], True,5,6,5]
print(len(l))
# print(type(l))
# print(l)
# l3 = 'hello ags!'
#
# l2 = [i for i in l3 if i != ' ']
print(l.count(l[4]))
print(*l[:3],l[4])
l[0] = (999,str(888))
print(*l)
# for i in range(len(l)):

print(l)
