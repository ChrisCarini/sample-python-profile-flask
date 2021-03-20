import pytest

from webapp import get_pow_2, pow_wrapper


@pytest.mark.parametrize("test_input,expected", [
    (1, 1),
    (2, 4),
    (100, 10000),
])
def test_get_pow_2(test_input: int, expected: int):
    # given - inputs

    # when
    result = get_pow_2(test_input)

    # then
    assert result == expected


@pytest.mark.parametrize("num,power,expected", [
    (1, 1, 1),
    (2, 2, 4),
    (100, 2, 10000),
    (10, 100, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000),
])
def test_pow_wrapper(num: int, power: int, expected: int):
    # given - inputs

    # when
    result = pow_wrapper(num, power)

    # then
    assert result == expected
