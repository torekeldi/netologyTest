import pytest


def check_month(month: int):
    if month in [12, 1, 2]:
        result = 'Зима'
    elif month in [3, 4, 5]:
        result = 'Весна'
    elif month in [6, 7, 8]:
        result = 'Лето'
    elif month in [9, 10, 11]:
        result = 'Осень'
    else:
        result = 'Некорректный номер месяца'
    return result


@pytest.mark.parametrize(
    'month, expected',
    (
        [0, 'Некорректный номер месяца'],
        [5, 'Весна'],
        [-5, 'Некорректный номер месяца'],
        [10, 'Осень'],
        ['555', 'Некорректный номер месяца'],
    )
)
def test_check_month(month, expected):
    actual = check_month(month)
    assert actual == expected


def solve(receipts: list):
    result = receipts[2::3]
    return result


@pytest.mark.parametrize(
    'receipts, expected',
    (
        [[123, 145, 346, 246, 235, 166, 112, 351, 436], [346, 166, 436]],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 6, 9]],
    )
)
def test_solve(receipts, expected):
    actual = solve(receipts)
    assert actual == expected


def longest_film(*films):
    return max(films, key=len)


@pytest.mark.parametrize(
    'films, expected',
    (
        [['Аладин', 'Мадагаскар', 'Бетховен'], 'Мадагаскар'],
        [['Гарри Поттер', 'Пираты Карибского моря', 'ВАЛЛ·И'], 'Пираты Карибского моря'],
        [['Cross Fireball', 'Double Cross', 'Cross Spin', 'Heartless Cross'], 'Heartless Cross'],
    )
)
def test_longest_film(films, expected):
    actual = longest_film(*films)
    assert actual == expected
