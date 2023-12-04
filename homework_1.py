from collections import Counter


def date(day: int, month: int, year: int) -> str:
    """Задача №1"""
    months = [
        "января",
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря",
    ]
    try:
        return f"{day} {months[month - 1]} {year} года"
    except (ValueError, TypeError):
        return "Дата введена неверно"


def count_names_in_tuple(names: tuple) -> dict:
    """Задача №2"""
    return dict(Counter(names))


def full_name(name_in_dict: dict) -> str:
    """Задача №3"""
    first_name = name_in_dict.get("first_name", "")
    last_name = name_in_dict.get("last_name", "")
    middle_name = name_in_dict.get("middle_name", "")
    if not first_name and not last_name:
        return "Нет данных"
    if not first_name:
        return last_name
    return " ".join([last_name, first_name, middle_name]).rstrip(" ")


def num_is_prime(n: int) -> bool:
    """Задача №4"""
    if n < 2:
        return False
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False
    return True


def set_of_increasing_numbers(*args) -> list[int]:
    """Задача №5"""
    s = set()
    for i in args:
        if isinstance(i, int) and not isinstance(i, bool):
            s.add(i)
    return sorted(list(s))
