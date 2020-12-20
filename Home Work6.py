file = open("input.txt","r", encoding='UTF-8')
data = file.readlines()
print(data)
file.close()

for i in data:
    print(i, end='')
    print(len(i), '- символов')
    print(len(i.split(' ')), "- строки")
    print('')

print('Количество строк -', len(data))
