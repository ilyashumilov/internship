class Counter:
    """Класс счётчика"""

    def __init__(self, initial_value: int) -> None:
        self.value = initial_value

    def inc(self) -> int:
        self.value += 1
        return self.value

    def dec(self) -> int:
        self.value -= 1
        return self.value


class ReverseCounter(Counter):
    """Класс обратного счётчика"""

    def inc(self) -> int:
        self.value -= 1
        return self.value

    def dec(self) -> int:
        self.value += 1
        return self.value


def get_counter(number: int) -> Counter or ReverseCounter:
    """Функция создания счётчика по заданному числу"""

    if number >= 0:
        counter = Counter(number)
    else:
        counter = ReverseCounter(number)
    return counter
