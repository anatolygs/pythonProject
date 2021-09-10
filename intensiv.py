a = 0
x = []
for i in range(10):
    ai = 'a' + str(i)
    ai = int(input())
    x.append(ai)
print(sum(x))

for i in range(a):
    ai = 'a' + str(i)
    ai = int(input('input digit: '))
    x.append(ai)
print(sum(x))

for i in range(1,10):
    for n in range(1,10):
        print(f'{i} * {n} = {i*n}\t', end=' ')
    print(end='\n')

n = int(input())
m = []
for i in range(n + 1):
    m.append(i ** 3)
print(sum(m))

n = 10
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
    print(sum)

print(sum)
