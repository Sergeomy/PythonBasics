# Достижение цели

a = float(input('Введите Ваш первоначальный результат: '))
b = float(input('Какой результат Вы хотите достичь?: '))
i = 1
while a <= b:
    #   print(i,'-й день:', a, 'км')
    i = i + 1
    a = a + a * 0.1
else:
    print('Вы достигните своей цели на ', i, '-й день')
