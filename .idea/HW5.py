debit = float(input('Пожалуйста введите значение выручки: '))
credit = float(input('Пожалуйста введите значение расходов: '))
profit = debit - credit
profitability = profit / debit

if debit == credit:
    print('Вы ничего не заработали')
elif debit >= credit:
    print('Вы заработали: ', profit)
    print('Рентабельность составила: ', profitability, '%')
    staff = int(input('Сколько сотрудников работает? '))
    print('Прибыль в расчете на одного сотрудника составляет: ', '%.2f' % (profit / staff))
else:
    print('Убыток составил: ', profit)
