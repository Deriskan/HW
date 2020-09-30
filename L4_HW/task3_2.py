# Задание 3

from task3_1 import is_triangle, ask_number


# 3.5
# Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами и
# если существует, то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle (
# равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).

def triangle_type(a: float, b: float, c: float) -> str:
    """
    This function returns a type of a triangle (with sides length as arguments) if it exists.
    """
    if not is_triangle(a, b, c):  # внутри функции is_triangle() есть assert на позитивные данные.
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral triangle'
    elif a == b or b == c or a == c:
        return 'Isosceles triangle'
    return 'Scalene triangle'


# 3.6
# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющую
# расстояние между точками с координатами (x1, y1) и (x2, y2).

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    This function returns a length of a line segment between (x1,y1) and (x2,y2). Endpoints coordinates as arguments.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


triangle_sides_length = (6, 13, 8)
print(f'This polygon is {triangle_type(*triangle_sides_length)!r}.')

# *Считайте четыре действительных числа от пользователя (перед запуском функции distance(), не внутри функции) и
# выведите результат работы функции distance().

line_segment_coordinates = []
print('Enter points coordinates x1,y1,x2,y2:')
while len(line_segment_coordinates) < 4:  # Запрашиваем координаты (4 значения) точек у пользователя.
    line_segment_coordinates.append(ask_number())  # С аргументом по умолчанию функция вернет float число.

print(f'The distance between two points is: {distance(*line_segment_coordinates)}')
