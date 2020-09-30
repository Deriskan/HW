# Задание 3

# 3.1
# Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести. Функция
# возвращает введённое число. *Теперь далее для других задач с числами, вы можете пользоваться этой функцией,
# а не простым input!

def ask_number(integer_type=0):
    """
    This function returns a number of a specified type from a user. The default number type is float. Returns an
    Integer number for "1" as an argument.
    """
    assert integer_type in (0, 1), 'The argument is 0 or 1 only!'
    if integer_type == 1:
        while True:
            try:
                number = int(input('Enter number:\n'))
                break
            except ValueError:
                print('It\'s NOT an Integer number!')
    else:
        while True:
            try:
                number = float(input('Enter number:\n'))
                break
            except ValueError:
                print('It\'s NOT a number!')
    return number


# 3.2
# Пишем функцию, которая попросит пользователя ввести слово (строка из буквенных символов без пробелов в
# середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно, просите его ввести. Функция
# возвращает введённое слово.

def ask_word() -> str:
    """
    This function returns a string without spaces from a user.
    """
    while True:
        w = input('Enter word:\n')
        w = w.strip()  # Убираем пробелы, если они есть в начале и конце строки.
        if w.isalpha():  # Проверяем, что все символы в строке буквы.
            break  # Слово введено. Выходим из цикла.
        else:
            print('It\'s NOT a word!')
    return w


# 3.3
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year: int) -> bool:
    """
    This function returns a bool statement for a year as an argument - is it a leap year or not.
    """
    assert int(year) > 0, 'Argument is an Integer and/or greater than 0 only!'
    if (not year % 4 and year % 100) or not year % 400:
        return True
    return False


# 3.4
# Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.

def is_triangle(a: float, b: float, c: float) -> bool:
    """
    This function returns a bool statement - a triangle (with sides length as arguments) exists or not.
    """
    assert float(a) >= 0 and float(b) >= 0 and float(c) >= 0, 'Arguments are real numbers and are not less than 0!'
    if (a + b) > c and (a + c) > b and (c + b) > a:     # Сумма значений любых двух сторон треугольника должна быть
        return True                                     # больше значения третьей стороны.
    return False


if __name__ == "__main__":
    print(ask_word())
    print(ask_number())
    print(ask_number(1))
    print(is_year_leap(2024))
    print(is_triangle(2, 8, 10))
