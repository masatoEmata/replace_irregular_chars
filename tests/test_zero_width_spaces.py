import pytest

from irregular_chars.zero_width_spaces import ZERO_WIDTH_SPACES, remove_zero_width_chars


@pytest.mark.parametrize("name, char", ZERO_WIDTH_SPACES.items())
def test_remove_zero_width_chars(name, char):
    test_str = f"Hello{char}World"
    expected_str = "HelloWorld"
    assert remove_zero_width_chars(test_str) == expected_str


def test_remove_zero_width_chars_multiple_and_mixed():
    test_str = f"Hello{ZERO_WIDTH_SPACES['ZERO WIDTH SPACE']}W{ZERO_WIDTH_SPACES['ZERO WIDTH JOINER']}orld"
    expected_str = "HelloWorld"
    assert remove_zero_width_chars(test_str) == expected_str


def test_remove_zero_width_chars_no_change():
    test_str = "Hello World"
    expected_str = "Hello World"
    assert remove_zero_width_chars(test_str) == expected_str
