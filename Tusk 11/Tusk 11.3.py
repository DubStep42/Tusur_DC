# 3. Рефакторинг.
# Дано: неоптимальный код.
#
# Задание: оптимизировать следующий код.

"""def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids

    responses = []
    for item_id in item_ids:
        new_response = dict(item_id=item_id)
        responses.append(new_response)
    return responses"""
def responses_creator(item_ids):
    return [{'item_id': item_id} for item_id in (item_ids or [None])]

# Тестовый случай
print(responses_creator([1, 2, 3]))
print(responses_creator([]))