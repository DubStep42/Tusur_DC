# 3. Рефакторинг.
# Дано: неоптимальный код.
#
# Задание: оптимизировать следующий код.
"""sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('капитан')

print(cap_count)"""

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = sum(sentence.count('капитан') for sentence in sentences)

print(cap_count)