from itertools import chain


def lazy_concatenate(list1, list2):
    result = list(chain(list1, list2))
    return result


list_A = [1, 2]
list_B = [3, 4]
print(lazy_concatenate(list_A, list_B))
