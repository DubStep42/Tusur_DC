class Friends:
    def __init__(self, connections):
        # Инициализируем множество связей
        self.connections = set(map(frozenset, connections))
        """Функция frozenset преобразует каждое множество в connections в неизменяемое
        множество, или frozenset. Это делается потому, что множества в Python
         не могут содержать изменяемые объекты, такие как другие множества.
        frozenset - это неизменяемый вариант множества, который может быть элементом другого множества."""

    def add(self, connection):
        # Если связь уже существует, возвращаем False
        if frozenset(connection) in self.connections:
            return False
        # Иначе добавляем связь и возвращаем True
        self.connections.add(frozenset(connection))
        return True

    def remove(self, connection):
        # Если связи нет, возвращаем False
        if frozenset(connection) not in self.connections:
            return False
        # Иначе удаляем связь и возвращаем True
        self.connections.remove(frozenset(connection))
        return True

    def names(self):
        # Возвращаем множество всех имен
        return set(name for connection in self.connections for name in connection)

    def connected(self, name):
        # Возвращаем множество имен, связанных с данным именем
        # После создания множества из него удаляется имя name, т.к. человек не знаком сам с собой
        return set(friend for connection in self.connections for friend in connection if name in connection) - {name}


f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))

# Проверяем метод add
print(f.add({"a", "b"}))  # Ожидаемый результат: False
print(f.add({"b", "d"}))  # Ожидаемый результат: True

# Проверяем метод remove
print(f.remove({"a", "b"}))  # Ожидаемый результат: True
print(f.remove({"b", "d"}))  # Ожидаемый результат: True
print(f.remove({"e", "f"}))  # Ожидаемый результат: False

# Проверяем метод names
print(f.names())  # Ожидаемый результат: {'a', 'b', 'c'}

# Проверяем метод connected
print(f.connected("a"))  # Ожидаемый результат: {'b', 'c'}
print(f.connected("d"))  # Ожидаемый результат: set()