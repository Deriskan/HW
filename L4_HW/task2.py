# Задание 2
# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов (неопределенное
# количество). Учитываем, что может быть повторяющиеся значения аргументов.

def second_min(*args):
    """
    This function returns a second unique element from an ascending list of arguments.
    """
    lst = list(args)  # Формируем список из аргументов
    lst.sort()  # Сортируем список "на месте"
    for i in lst:
        if lst.index(i) != 0:  # Ищем первый попавшийся елемент для которого index() не 0.
            return i


print(second_min('7', '2', '2', '8', '2', '2'))
print(second_min('f', 'c', 'a', 'c', 'a'))
