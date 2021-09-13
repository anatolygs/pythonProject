s1 = {'one', 'two', 'three', 'four', 'one'}
s2 = {1, 2, 3, 3, 2, 4, 6, 9}
s3 = {2, 3, 3, 2, 4, 6, 9, 11, 12, 13}
print(id(s1))
# s3 = s1.copy()
print(id(s3))
s1.add('test')
s4 = s3 | s2
# s1.remove('one')
print(s4)

for i in s3:
    print(i, type(i))
    if 13 in i:
        print('stop')
        break
