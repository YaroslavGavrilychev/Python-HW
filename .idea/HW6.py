result = float(input('Введите ваш результат: '))
max_result = float(input('Введите желаемый результат: '))
day = 1

while max_result >= result:  # вот тут если ставлю <= то код не работает не могу понять почему
    print(day, '- й день: ', '%.2f' % result)
    result = result + (result * 0.1)
    day += 1
print('На ', day, '- й день спортсмен достигнет результата близкому к ', max_result, ' км')
