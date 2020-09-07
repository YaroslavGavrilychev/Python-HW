sec = int(input('Пожалуйста, введите время в секундах: '))
min = sec // 60
hours = min // 60
print(f"%02d:%02d:%02d" % (hours, min % 60, sec % 60))
