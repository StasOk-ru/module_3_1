# Задача "Счётчик вызовов":

# Пункты задачи:

# Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)
# Вывод на консоль:
# (8, 'CAPYBARA', 'capybara')
# (10, 'ARMAGEDDON', 'armageddon')
# True
# False
# 4
# Примечания:
# Для использования глобальной переменной внутри функции используйте оператор global.
# Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.

calls = 0 # Создать переменную calls = 0 вне функций.

def count_calls(): # подсчитывающая вызовы остальных функций.
    global calls
    calls = calls + 1
    #print('зашёл на подсчет заходов других ф-ий', calls)

def string_info(string): # принимает аргумент - строку
    # и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    # .string_info с параметром string и реализовать логику работы по описанию
    count_calls()
    string = len(string), string.upper(), string.lower()
    print(f"Строка преобразована: {string}")
    #print('Строка преобразована:', len(string), string.upper(), string.lower())
    #print(f"Строка преобразована: ({len(string)}, '{string.upper()}', '{string.lower()}')")
    return string

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        fl = 0
        a = list_to_search[i].lower().find(string.lower())
        if a >= 0:
            fl += 1
    if fl > 0:
        print('Есть совпадение: True')
    else:
        print('Нет совпадений: False')

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)
