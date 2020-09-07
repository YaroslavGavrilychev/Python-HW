num = int(input('Введите целое положительное число: '))
max_num = 0
num0 = num

while num0 > 0:
    num1 = num0 % 10
    num0 //= 10
    if num1 > max_num:
        max_num = num1

print('Самая большая цифра в числе ', num, ' равна ', max_num)
# посмотрел решение по проверке с 9 даже не подумал
