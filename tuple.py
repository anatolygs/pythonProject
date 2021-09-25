worlds = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'Ароза упала на лапу Азора', 'Около миши молоко']


new_worlds = []
for i in range(len(worlds)):
    if worlds[i] == worlds[i][::-1]:
        new_worlds.append(worlds[i])
print(new_worlds)


new_str = str()
end_str = []
for i in range(len(my_str)):
    if ' ' in my_str[i]:
        new_str = my_str[i].replace(' ', '')
        if new_str.lower() == new_str[::-1].lower():
            print(my_str[i])
            end_str.append(my_str[i])
print(end_str)
