sent = input('Введите предложение')

norm = (sent.split())

answer = ''

for i in norm:
    if len(i) > len(answer):
        answer = i

print(answer)