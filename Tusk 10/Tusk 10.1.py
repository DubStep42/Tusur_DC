# 1. Градусник.
# Дано: список градусов Цельсия.
#
# Задание: написать функцию, которая преобразовывает исходный список градусов Цельсия в список градусов Фаренгейта
# Пример:
#  [39.2, 36.5, 37.3, 37.8], результат:
#  [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
def celsius_to_fahrenheit(celsius_degrees):
    return [c * 9/5 + 32 for c in celsius_degrees]

# Тестовый случай
celsius_temp = [39.2, 36.5, 37.3, 37.8]
fahrenheit_temp = map(lambda x: round(x, 2), list(celsius_to_fahrenheit(celsius_temp)))
print(list(fahrenheit_temp))

# Ожидаемый результат: [102.56, 97.7, 99.14, 100.04]