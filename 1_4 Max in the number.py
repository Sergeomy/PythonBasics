# Находим макимальное число в введённом
n = int(input("Введите любое число: "))
m = n % 10
n = n // 10
while n > 0:
    if n % 10 > m:
        m = n % 10
    n = n // 10
print('Самая большая цифра в введённом значении:', m)
