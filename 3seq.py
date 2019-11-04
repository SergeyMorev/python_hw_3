

def ask_a_number_list(ask_str):
    print(ask_str)
    input_str = input()

    str_list = input_str.split(',')
    num_list = list()

    for s in str_list:
        if s.strip().isnumeric():
            num_list.append(int(s))
    return num_list


list1 = ask_a_number_list('Введите список чисел через запятую:')
list2 = ask_a_number_list('Введите второй список чисел через запятую:')

for i in list2:
    while i in list1:
        list1.remove(i)

print(f'Результат: {list1}')

