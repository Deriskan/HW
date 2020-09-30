# Задание 1
# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
#
# 1-е число – сколько строк будет в песне. По умолчанию 3 2-е число – сколько «la» будет в строке («la» в строке
# объединяются дефисом). По умолчанию 3 3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка,
# если 1, то в конце стоит «!». По умолчанию 0.

def la_song(string_count=3, word_count=3, ending_mark=0) -> str:
    """
    This function returns a string that can be separated by "\n" and ends with "." or "!".
    """
    assert int(string_count) >= 0 and int(word_count) >= 0, '"Count" arguments are natural numbers only!'
    assert ending_mark in (0, 1), 'The argument for the end of a string is 0 or 1 only!'
    lst = []  # Используем список слов для вставки "-" между словами при преобразовании в строку.
    ending = ['.', '!', '\n']  # Список возможных последних симовлов строки.
    if string_count == 0 or word_count == 0:  # Если нет ни одной строчки ни одного слова в песне.
        return ''
    else:
        for i in range(word_count):  # Добавляем все слова в список слов.
            lst.append('la')
    return ('-'.join(lst) + f'{ending[2]}') * (string_count - 1) + ('-'.join(lst) + f'{ending[ending_mark]}')


print(la_song())
print(la_song(10, 5, 1))
