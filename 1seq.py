
def input_a_number(ask_str):
    print(ask_str)
    res = input()
    while not res.isdigit():
        print(f'"{res}" не является числом')
        print(ask_str)
        res = input()
    return int(res)


count = input_a_number('Введите количество элементов:')
i = 1
numbers = list()

while i <= count:
    numbers.append(input_a_number(f'Введите {i} элемент:'))
    i += 1

numbers.sort()
print(f'Вывод:{numbers}')

