"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count
from exercises.ex06.dictionaries import invert, favorite_color, count
__author__ = "730396223"


def test_normal_use_invert():
    xs: dict[str, str] = {"cat": "mat", "fat": "tat", "act": "jack"}
    assert invert(xs) == {"mat": "cat", "tat": "fat", "jack": "act"}


def test_one_item():
    xs: dict[str, str] = {"Hello": "Trip"}
    assert invert(xs) == {"Trip": "Hello"}


def test_double_call():
    xs: dict[str, str] = {"hello": "Yellow"}
    invert(invert(xs)) == {"hello": "Yellow"}


def test_normal_use_fav_color():
    xs: dict[str, str] = {"Quest": "red", "Dio": "blue", "Justin": "blue", "Jess": "yellow", "Quess": "blue"}
    assert favorite_color(xs) == "blue"


def test_one_color():
    xs: dict[str, str] = {"Quest": "Blue"}
    assert favorite_color(xs) == "Blue"


def test_all_same_color():
    xs: dict[str, str] = {"Quest": "Blue", "Joe": "Blue", "Hopper": "Blue"}
    assert favorite_color(xs) == "Blue"    


def test_normal_use_count():
    xs: list[str] = ["1", "2", "3", "4", "1", "1", "2"]
    assert count(xs) == {"1": 3, "2": 2, "3": 1, "4": 1}


def test_one_number():
    xs: list[str] = ["1", "1", "1", "1", "1", "1", "1"]
    assert count(xs) == {"1": 7}


def test_all_one_value():
    xs: list[str] = ["1", "2", "3", "4"]
    assert count(xs) == {"1": 1, "2": 1, "3": 1, "4": 1}
