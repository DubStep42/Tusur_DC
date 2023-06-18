# 2. Длинномер.
# Дано: список строковых значений.
#
# Задание: написать функцию, которая возвращает список длин каждой строки.
#
# Пример:
# ['Tina', 'Raj', 'Tom'], результат: [4, 3, 3]

def lengths(strings):
    return list(map(len, strings))

# Тестовый случай
Name_Len_list = lengths(['Tina', 'Raj', 'Tom'])
print(Name_Len_list)  # Ожидаемый результат: [4, 3, 3]