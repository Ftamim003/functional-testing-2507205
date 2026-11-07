
import pytest

from target import (
    average,
    celsius_to_fahrenheit,
    common_items,
    count_vowels,
    divide,
    factorial,
    find_max,
    get_price,
    greet,
    invert,
    is_adult,
    is_leap_year,
    power,
    square_root,
    swap,
    to_int,
)

# =====================================================
# 1. is_adult(age)
# =====================================================

@pytest.mark.parametrize(
    "age, expected",
    [
        (0, False),
        (1, False),
        (17, False),
        (18, True),
        (19, True),
        (100, True),
    ],
)
def test_is_adult_valid(age, expected):
    result = is_adult(age)
    assert result is expected
    assert isinstance(result, bool)


def test_is_adult_negative():
    with pytest.raises(ValueError, match="age cannot be negative"):
        is_adult(-1)


def test_is_adult_wrong_type():
    with pytest.raises(TypeError):
        is_adult("18")


# =====================================================
# 2. celsius_to_fahrenheit(celsius)
# =====================================================

@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
        (25.5, 77.9),
        (-273.15, -459.67),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    result = celsius_to_fahrenheit(celsius)
    assert result == expected
    assert isinstance(result, float)


def test_celsius_to_fahrenheit_wrong_type():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("25")


# =====================================================
# 3. count_vowels(text)
# =====================================================

@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 2),
        ("HELLO", 2),
        ("Python", 1),
        ("AEIOU", 5),
        ("xyz", 0),
        ("", 0),
        ("Education", 5),
        ("Tamim 123!", 2),
    ],
)
def test_count_vowels(text, expected):
    result = count_vowels(text)
    assert result == expected
    assert isinstance(result, int)


def test_count_vowels_wrong_type():
    with pytest.raises(TypeError, match="text must be a string"):
        count_vowels(123)


# =====================================================
# 4. invert(flag)
# =====================================================

@pytest.mark.parametrize(
    "flag, expected",
    [
        (True, False),
        (False, True),
    ],
)
def test_invert(flag, expected):
    result = invert(flag)
    assert result is expected
    assert isinstance(result, bool)


@pytest.mark.parametrize(
    "value",
    [1, 0, "True", "False", None, [], {}],
)
def test_invert_wrong_type(value):
    with pytest.raises(TypeError, match="flag must be True or False"):
        invert(value)


# =====================================================
# 5. greet(name)
# =====================================================

@pytest.mark.parametrize(
    "name, expected",
    [
        (None, "Hello, Guest!"),
        ("", "Hello, Guest!"),
        ("   ", "Hello, Guest!"),
        ("Tamim", "Hello, Tamim!"),
        (" Tamim ", "Hello, Tamim!"),
        ("Alice", "Hello, Alice!"),
    ],
)
def test_greet(name, expected):
    result = greet(name)
    assert result == expected
    assert isinstance(result, str)


def test_greet_wrong_type():
    # Current implementation calls strip() on the supplied value.
    with pytest.raises(AttributeError):
        greet(123)


# =====================================================
# 6. find_max(numbers)
# =====================================================

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 3),
        ([10, 5, 2], 10),
        ([-10, -5, -20], -5),
        ([5], 5),
        ([1.5, 2.5, 3.5], 3.5),
        ([0, 0, 0], 0),
    ],
)
def test_find_max(numbers, expected):
    assert find_max(numbers) == expected


def test_find_max_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        find_max([])


def test_find_max_wrong_type():
    with pytest.raises(TypeError):
        find_max(None)


def test_find_max_mixed_types():
    with pytest.raises(TypeError):
        find_max([1, "2"])


# =====================================================
# 7. get_price(prices, item)
# =====================================================

def test_get_price_existing_item():
    prices = {"apple": 100, "banana": 50}

    result = get_price(prices, "apple")

    assert result == 100
    assert isinstance(result, int)


def test_get_price_another_item():
    prices = {"apple": 100, "banana": 50}

    assert get_price(prices, "banana") == 50


def test_get_price_missing_item():
    prices = {"apple": 100}

    with pytest.raises(KeyError, match="orange not found"):
        get_price(prices, "orange")


def test_get_price_wrong_type():
    with pytest.raises(TypeError):
        get_price(None, "apple")


# =====================================================
# 8. swap(pair)
# =====================================================

@pytest.mark.parametrize(
    "pair, expected",
    [
        ((1, 2), (2, 1)),
        (("a", "b"), ("b", "a")),
        ((10, 20), (20, 10)),
        ((None, "hello"), ("hello", None)),
        ((1.5, 2.5), (2.5, 1.5)),
    ],
)
def test_swap_valid(pair, expected):
    result = swap(pair)
    assert result == expected
    assert isinstance(result, tuple)


@pytest.mark.parametrize(
    "pair",
    [
        (),
        (1,),
        (1, 2, 3),
    ],
)
def test_swap_invalid_length(pair):
    with pytest.raises(ValueError, match="pair must have exactly 2 values"):
        swap(pair)


def test_swap_wrong_type():
    with pytest.raises(TypeError):
        swap(None)


# =====================================================
# 9. common_items(set_a, set_b)
# =====================================================

@pytest.mark.parametrize(
    "set_a, set_b, expected",
    [
        ({1, 2, 3}, {2, 3, 4}, {2, 3}),
        ({1, 2}, {3, 4}, set()),
        ({1, 2}, {1, 2}, {1, 2}),
        (set(), {1, 2}, set()),
        ({"a", "b"}, {"b", "c"}, {"b"}),
    ],
)
def test_common_items(set_a, set_b, expected):
    result = common_items(set_a, set_b)
    assert result == expected
    assert isinstance(result, set)


def test_common_items_wrong_type():
    with pytest.raises(TypeError):
        common_items({1, 2}, [1, 2])


# =====================================================
# 10. is_leap_year(year)
# =====================================================

@pytest.mark.parametrize(
    "year, expected",
    [
        (2024, True),
        (2020, True),
        (2000, True),
        (2400, True),
        (2023, False),
        (1900, False),
        (2100, False),
        (2025, False),
        (1, False),
        (4, True),
    ],
)
def test_is_leap_year(year, expected):
    result = is_leap_year(year)
    assert result is expected
    assert isinstance(result, bool)


def test_is_leap_year_zero():
    with pytest.raises(ValueError, match="year must be 1 or more"):
        is_leap_year(0)


def test_is_leap_year_negative():
    with pytest.raises(ValueError):
        is_leap_year(-2024)


def test_is_leap_year_wrong_type():
    with pytest.raises(TypeError):
        is_leap_year("2024")


# =====================================================
# 11. to_int(value)
# =====================================================


@pytest.mark.parametrize(
    "value, expected",
    [
        ("10", 10),
        ("-5", -5),
        (10.8, 10),
        (-10.8, -10),
        (0, 0),
    ],
)
def test_to_int_valid(value, expected):
    result = to_int(value)
    assert result == expected
    assert isinstance(result, int)



@pytest.mark.parametrize("value", [True, False])
def test_to_int_boolean(value):
    with pytest.raises(TypeError, match="bool is not allowed"):
        to_int(value)


def test_to_int_invalid_string():
    with pytest.raises(ValueError):
        to_int("hello")


def test_to_int_wrong_type():
    with pytest.raises(TypeError):
        to_int(object())


# =====================================================
# 12. divide(a, b)
# =====================================================

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (5, 2, 2.5),
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (0, 5, 0.0),
        (7, 2, 3.5),
    ],
)
def test_divide_valid(a, b, expected):
    result = divide(a, b)
    assert result == expected
    assert isinstance(result, float)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        divide(10, 0)


def test_divide_wrong_type():
    with pytest.raises(TypeError):
        divide("10", 2)


# =====================================================
# 13. power(base, exponent)
# =====================================================

@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 3, 8),
        (2, 0, 1),
        (5, 1, 5),
        (3, 2, 9),
        (2, -2, 0.25),
        (10, 2, 100),
        (0, 5, 0),
        (-2, 3, -8),
        (-2, 2, 4),
    ],
)
def test_power(base, exponent, expected):
    result = power(base, exponent)
    assert result == expected


def test_power_wrong_type():
    with pytest.raises(TypeError):
        power("2", 3)


# =====================================================
# 14. square_root(x)
# =====================================================

@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0.0),
        (1, 1.0),
        (4, 2.0),
        (9, 3.0),
        (25, 5.0),
        (2, 2 ** 0.5),
        (100, 10.0),
    ],
)
def test_square_root(x, expected):
    result = square_root(x)
    assert result == pytest.approx(expected)
    assert isinstance(result, float)


def test_square_root_negative():
    with pytest.raises(
        ValueError,
        match="cannot take the square root of a negative number",
    ):
        square_root(-1)


def test_square_root_wrong_type():
    with pytest.raises(TypeError):
        square_root("4")


# =====================================================
# 15. factorial(n)
# =====================================================

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial(n, expected):
    result = factorial(n)
    assert result == expected
    assert isinstance(result, int)


def test_factorial_negative():
    with pytest.raises(
        ValueError,
        match="factorial is not defined for negative numbers",
    ):
        factorial(-1)


def test_factorial_wrong_type():
    with pytest.raises(TypeError):
        factorial("5")


# =====================================================
# 16. average(numbers)
# =====================================================

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 2.0),
        ([10, 20, 30], 20.0),
        ([5], 5.0),
        ([1, 2, 3, 4, 5], 3.0),
        ([1.5, 2.5, 3.5], 2.5),
        ([-1, -2, -3], -2.0),
        ([0, 0, 0], 0.0),
    ],
)
def test_average(numbers, expected):
    result = average(numbers)
    assert result == pytest.approx(expected)
    assert isinstance(result, float)


def test_average_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        average([])


def test_average_wrong_type():
    with pytest.raises(TypeError):
        average(None)


def test_average_mixed_types():
    with pytest.raises(TypeError):
        average([1, "2"])



# def test_intentional_ci_failure():
#     assert 1 == 2