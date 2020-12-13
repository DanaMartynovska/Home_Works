def res(p):
    for d in p:
        print(d)

staff = [
{'num': 10001, 'name': 'spoon', 'price': 8, 'quantity': 2}, {'num': 10002, 'name': 'fork', 'price': 10, 'quantity': 4}
]
res(staff)
ask = int(input("введите 0 для создания нового словаря или 1 для измений значений в сущестующих"))
while ask != 1:
    ask = int(input("введите 0 для создания нового словаря или 1 для измений значений в сущестующих"))
    if ask == 0:
#new_dict = {k:input('введити значение') for k in staff[0]}
        new_dict = {'num': int(input('введити значение')), 'name' : input('введити название') ,'price' : int(input('введити цену')), 'quantity' : int(input('введите количество'))}
        staff.append(new_dict)
        res(staff)
    else:
        ask_2 = staff[int(input('Виберите номер словаря'))]
        while True:

            conf = int(input('Введите 0 для потверждения изменений, либо другую цифру для отмены'))
            if conf == 0:
                res(staff)




"""
while True:
    num_1 = int(input('Введите номер товара spoon'))
    quantity_1 = int(input('Введите количество товара spoon'))
    num_2 = int(input('Введите номер товара fork'))
    quantity_2 = int(input('Введите количество товара fork'))
    conf = int(input('Введите 0 для потверждения изменений, либо другую цифру для отмены'))
    if conf == 0:
        goods_1['num'] = num_1
        goods_1['quantity'] = quantity_1
        goods_2['num'] = num_2
        goods_2['quantity'] = quantity_2
        break
print(staff)
"""