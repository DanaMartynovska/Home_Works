sum = int(input('Введите сумму'))

text = str

if sum > 4 and sum < 21:
    text = 'копеек'

elif sum == 0:
    text = 'у вас нет денег =('

else:
    sum > 21
    dot = sum / 10
    res = round(dot - int(dot), 1) * 10

    if res == 1:
        text = 'копейка'
    elif res > 1 and res < 5:
        text = 'копейки'
    elif res > 4 and res <= 9 or res == 0:
        text = 'копеек'

print(sum, text)