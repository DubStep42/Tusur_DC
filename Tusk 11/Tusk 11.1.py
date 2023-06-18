# 1. Случайности не случайны.
# Дано: n - целое число.
#
# Задание: написать функцию-генератор, которая возвращает n дробных чисел из диапазона [0, n]. Используйте функцию random.uniform для генерации случайных чисел.
#
# Пример:
from random import uniform
def generate_random_numbers(n):
    for _ in range(n):
        yield uniform(0, n)

# Тестовый случай
random_num = list(map(lambda x: round(x, 4), list(generate_random_numbers(3))))
print(" 3 случайных числа в диапазоне от 0 до 3: ", random_num) # Ожидаемый результат: 3 случайных числа в диапазоне от 0 до 3