# coding: utf8

# Функция находит какой разделитель использовал пользователь для ввода последовательности.
def find_sep(some_str):
    seps = set(',;/')
    symbols = []

    # Выберем из строки все символы кроме цифр и букв
    for i in str(some_str):
        if i.isalnum():
            continue
        else:
            symbols.append(i)

    # Из оставшихся сделаем set
    uniq_sym = set(symbols)
    sep = uniq_sym.intersection(seps)

    if not sep:         # Если нет разделителей, по умолчанию выдаем ','
        return ','
    if len(sep) == 1:   # Если один разделитель, то его и выдаем
        return list(sep)[0]   # ?? Как получить элемент из множества ?
    else:
        print("Ошибка. Нельзя использовать разные разделители вперемешку.")
        return None


print('Введите элементы списка через разделитель:')
input_str = input()
sep = find_sep(input_str)
if sep:
    numbers_list = input_str.split(sep)
    numbers_set = set()

    for num in numbers_list:
        if num.strip().isnumeric():
            numbers_set.add(int(num))

    print(f'Вывод: {numbers_set}')




