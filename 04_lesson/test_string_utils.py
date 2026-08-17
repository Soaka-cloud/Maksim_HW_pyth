import pytest
from string_utils import StringUtils

utils = StringUtils()


# Преобразование первой буквы в заглавную

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("SKYPRO", "Skypro"),
    ("sKyPrO", "Skypro"),
    ("123", "123"),
    ("", ""),
])
def test_capitalize(input_str, expected):
    """Первый символ становится заглавным, остальные строчными"""
    assert utils.capitalize(input_str) == expected


# Удаление пробелов в начале

@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("skypro", "skypro"),
    ("  ", ""),
    ("", ""),
])
def test_trim(input_str, expected):
    """Пробелы в начале строки удаляются"""
    assert utils.trim(input_str) == expected


# Проверка наличия символа в строке

@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "s", True),
    ("skypro", "z", False),
    ("", "a", False),
    ("123", "2", True),
])
def test_contains(string, symbol, expected):
    """Проверяет, содержит ли строка заданный символ"""
    assert utils.contains(string, symbol) == expected


# Удаление символа из строки

@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "s", "kypro"),
    ("skypro", "k", "sypro"),
    ("skypro", "z", "skypro"),
    ("", "a", ""),
    ("skypro", "", "skypro"),
])
def test_delete_symbol(string, symbol, expected):
    """Все вхождения символа удаляются из строки"""
    assert utils.delete_symbol(string, symbol) == expected


# Дополнительные тесты для методов, которых нет в классе,
# но они могут быть реализованы позже

def test_trim_with_spaces_at_end():
    """Проверка: trim удаляет пробелы только в начале"""
    # В текущей реализации trim не удаляет пробелы в конце
    # Это ожидаемое поведение, так как в документации сказано:
    # "удаляет пробелы в начале, если они есть"
    result = utils.trim("  skypro  ")
    assert result == "skypro  "  # пробелы в конце остаются
