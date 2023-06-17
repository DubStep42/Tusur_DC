# 1.
# Список из числа.
# Дано: натуральное число N.
#
# Задание: написать функцию, которая возвращает список всех цифр
# этого числа в обратном порядке.
#
# Пример:
#
# 123, результат: [3, 2, 1]


def reverse_digits(n):
    num_str = str(n)
    reversed_digits = [int(digit) for digit in num_str[::-1]]
    return reversed_digits

number = 123
result = reverse_digits(number)
print(result)