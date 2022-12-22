count = 0
while True:
    a = input('Введите возраст посетителя: ')
    if a == '':
        break
    try:
        a = int(a)
        if 0 < a < 3:
            count += 0
        elif 2 < a < 12:
            count += 14
        elif a > 65:
            count += 18
        elif 13 < a < 66:
            count += 23
        else:
            print('Вы вообще родились?')

    except:
        print('Некорректное значение возраста')

print(f'К оплате с Вас:\n{count}.00 $')
