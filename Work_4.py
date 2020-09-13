history = input("Расскажи историю: ")
my_str = []
num_str = 1

for el in range(history.count(' ') + 1):
    my_str = history.split()

    if len(str(my_str)) <= 10:
        print(f" {num} {my_str[el]}")
        num_str += 1

    else:
        print(f" {num_str} {my_str[el][0:10]}")
        num_str += 1