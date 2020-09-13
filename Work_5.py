my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите положительное число (Закончить программу - 0): "))
# Хотел назначить букву на выход, например q, но не могу сообразить как перевести в строку одну и ту же строку, чтоб он и ИНТ принимал и выход мог сделать

while digit != 0:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
        print(f"Tекущий рейтинг - {my_list}")
        digit = int(input("Введите число: "))