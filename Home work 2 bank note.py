sum = float(input('Введите сумму в формате гривны 00.00 копейки'))

sumh = int(sum)

sumc = round ((sum - sumh) * 100)


if sumh >4 and sumh <21: texth = 'гривен'

elif sum == 00.00: text_0 = 'у вас нет денег =('
    print(sum, text_0)

else:
    dot = sumh / 10
    res = round (dot - int(dot),1) * 10
    if res == 1: texth = 'гривна'
    elif res >1 and res <5: texth = 'гривны'
    elif res >4 and res <=9 or res == 0: texth = 'гривен'

if sumc >4 and sumc <21: text = 'копеек'

else:

    dot = sumc / 10
    res = round (dot - int(dot),1) * 10
    if res == 1: text = 'копейка'
    elif res >1 and res <5: text = 'копейки'
    elif res >4 and res <=9 or res == 0: text = 'копеек'

print(sumh, texth, sumc, text)