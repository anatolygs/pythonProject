import random
a = []
b = []
for i in range(101):
    if random.randint(1, 10000000) % 2 == 0:
        a.append('1')
    else:
        b.append('2')
if len(a) > len(b):
    print('орел')
else:
    print('решка')