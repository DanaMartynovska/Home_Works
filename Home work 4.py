def binary_num(num):
    change = ''
    while num > 0:
        if num % 2 == 0:
            print('0', end='')
        else:
            print('1' + change, end='')
        num //= 2
    return change


while True:
    a = int(input('Введите число'))
    if a != 0:
        print(binary_num(a))
    else:
        break



